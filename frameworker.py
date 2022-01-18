import json
import os
import spacy
import torch
import trafilatura


class Frameworker:
    def __init__(self,
                 path_frameworks=r"data/frameworks.json",
                 use_gpu=True):

        if use_gpu:
            is_using_gpu = spacy.prefer_gpu()
            if is_using_gpu:
                torch.set_default_tensor_type("torch.cuda.FloatTensor")

        spacymodel = 'en_core_web_lg'

        try:
            model_info = spacy.cli.info(spacymodel)
            spacy_version = spacy.__version__
            lower = model_info['spacy_version'].split(',')[0][2:]
            higher = model_info['spacy_version'].split(',')[1][1:]

            if not higher > spacy_version >= lower:
                spacy.cli.download(spacymodel)

        except SystemExit:
            spacy.cli.download(spacymodel)

        self.nlp = spacy.load(spacymodel)
        self.nlp.add_pipe('universal_sentence_encoder')

        # Should be changed according to amount of ram/vram
        self.nlp.max_length = 2000000

        # import after download of model
        from mordecai import Geoparser
        self.geoparser = Geoparser(nlp=self.nlp)

        assert os.path.exists(path_frameworks)

        with open(path_frameworks, 'r', encoding='utf-8') as json_file:
            self.frameworks = json.load(json_file)

    def __call__(self, urls: list) -> dict:
        downloads = self.scrape(urls)
        title = ""
        text = ""
        for d in downloads:
            download = json.loads(d)
            title = title + download["title"] + '|'
            text = text + download["text"] + '\n\n'

        return self.extract(title, text)

    def scrape(self, urls: list) -> list:
        """
        Give back a list of text extracted from the list of url's
        """

        result = []
        for url in urls:
            downloaded = trafilatura.fetch_url(url)
            assert downloaded
            extracted_text = trafilatura.extract(downloaded, output_format='json')

            result.append(extracted_text)

        return result

    def extract(self, name, text) -> dict:
        """

        """

        result = {"name": name, "text": text, "length": len(text)}

        doc = self.nlp(text)

        result["wordcount"] = len(doc)
        result["organisations"] = self.organisations(doc)
        result["locations"] = self.locations(doc)
        result["tags"] = self.tags(doc)
        result["frameworks"] = self.frameworker(doc)

        return result

    def tags(self, doc) -> dict:
        pos_tag = ["PROPN", "ADJ", "NOUN", "VERB"]
        result = {}
        for token in doc:
            if token.pos_ in pos_tag and token.text not in result.keys():
                result[token.text] = {"count": doc.text.count(token.text), "label": token.pos_}

    def frameworker(self, doc) -> dict:
        res = {}
        for framework, frameworkmeta in self.frameworks.items():
            res[framework] = {}
            for element in frameworkmeta["framework_elements"]:
                temp = self.nlp(element["name"])
                sim_score = doc.similarity(temp)
                if element["description"] is not None:
                    temp_des = self.nlp(element["description"])
                    sim_score = sim_score * 0.5 + doc.similarity(temp_des) * 0.5

                res[framework][element["name"]] = {"description": element["description"], "similarity_score": sim_score,
                                                   "id": element["id"]}

            res[framework] = dict(
                sorted(res[framework].items(), key=lambda item: item[1]["similarity_score"], reverse=True))
        return res

    def organisations(self, doc) -> dict:
        ent_list = [ent.text for ent in doc.ents]
        return dict(
            sorted(
                dict(
                    (ent.text, {"count": ent_list.count(ent.text), "label": ent.label_}) for ent in doc.ents if
                    ent.label_ == "ORG"
                ).items(),
                key=lambda item: item[1]["count"],
                reverse=True)
        )

    def locations(self, doc) -> dict:
        return self.geoparser.geoparse(doc.text)


if __name__ == '__main__':
    fw = Frameworker()
    print(fw(['https://www.bbc.co.uk/learningenglish/features/6-minute-english/ep-200305']))
