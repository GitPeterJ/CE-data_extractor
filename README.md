
# Circle Economy Data Extractor

A pipeline to extract information from articles based on a list of URLs, in order to make the Knowledge Hub as complete as possible.




## Used Technologies

+ [spaCy](https://github.com/explosion/spaCy)
+ [trafilatura](https://github.com/adbar/trafilatura)
+ [mordecai](https://github.com/openeventdata/mordecai)
+ [spaCy Universal Sentence Encoder](https://github.com/MartinoMensio/spacy-universal-sentence-encoder)
+ [PyTorch](https://github.com/pytorch/pytorch)


## Installation

Clone the project locally:

```bash
git clone git@github.com:GitPeterJ/CE-url_extractor.git
cd CE-url_extractor
```

Install the requirements:
```bash
pip install -r requirements.txt
```

Download the required spaCy NLP model:
```bash
python -m spacy download en_core_web_lg
```

Set up a geonames gazetteer in Elasticsearch (via Docker):
```bash
docker pull elasticsearch:5.5.2
wget https://andrewhalterman.com/files/geonames_index.tar.gz --output-file=wget_log.txt
tar -xzf geonames_index.tar.gz
docker run -d -p 127.0.0.1:9200:9200 -v $(pwd)/geonames_index/:/usr/share/elasticsearch/data elasticsearch:5.5.2
```
## Run Locally

Just run the Python script:

```bash
python frameworker.py
```

*Make sure you put the articles to scrape in the `Frameworker`.*
## Example

Input:
```
https://www.bbc.co.uk/learningenglish/features/6-minute-english/ep-200305
```

Output:

*Note: the output has been truncated for readability in this example.*
```json
{
   "name":"BBC Learning English - 6 Minute English / The circular economy|",
   "text":"The amount of waste we produce around the world is huge and it’s a growing problem. Recycling has partly been the solution to the issue but it hasn't been enough. Now there are calls to develop a circular economy which makes manufacturers responsible for what happens to the goods they produce. We discuss this in 6 minutes and teach some new - not recycled - vocabulary!\nThis week's question\nWhich country recycles the highest percentage of its waste? Is it:\nA: Sweden\nB: Germany\nC: New Zealand\nListen to the programme to find out the answer.\nVocabulary\nto separate to divide or split different things into different categories or groups\nto treat to process or deal with, for example, recycled waste\nout of sight, out of mind a phrase that means we ignore or don’t think about what we don’t see\nmanufacturer the person or company that makes a product\nconsumer a person that buy a product\nlifecycle the length of time a product is designed to work for\nTranscript\nNote: This is not a word-for-word transcript\nNeil Hello. This is 6 Minute English with me, Neil.\nSam And me, Sam.\nNeil Today, we’re talking rubbish.\nSam Ooh, that’s a bit harsh – I thought it was going to be interesting.\nNeil I mean our topic is about rubbish, not that we are rubbish.\nSam I see. Do go on.\nNeil Thank you. So the amount of waste we produce around the world is huge and it’s a growing problem.\nSam But, there are some things that we can do, like recycling. Where I live, I can recycle a lot, and I’m always very careful to separate - to split my rubbish into paper, metal, food, plastic and so on.\nNeil But is that enough, even if we all do it? We’ll look a little more at this topic shortly, but first, as always, a question. Which country recycles the highest percentage of its waste? Is it:\nA: Sweden\nB: Germany\nC: New Zealand\nWhat do you think, Sam?\nSam I’m not sure, but I think it could be Germany so I’m going to go with that - Germany.\nNeil OK. We’ll see if you’re right a little bit later on. The BBC radio programme, Business Daily, recently tackled this topic. They spoke to Alexandre Lemille, an expert in this area. Does he think recycling is the answer? Let’s hear what he said.\nAlexandre Lemille Recycling is not the answer to waste from an efficient point of view because we are not able to get all the waste separated properly and therefore treated in the background. The main objective of our model is to hide waste so we don’t see as urban citizens, or rural citizens, we don’t see the waste, it is out of sight and therefore out of mind.\nNeil What’s his view of recycling?\nSam I was a bit surprised, because he said recycling wasn’t the answer. One reason is that it’s not always possible to separate waste you can recycle from waste you can’t recycle, and that makes treating it very difficult. Treating means handling it and using different processes, so it can be used again.\nNeil And the result is a lot of waste, including waste that could be recycled but which is just hidden. And as long as we don’t see it, we don’t think about it.\nSam And he uses a good phrase to describe this – out of sight, out of mind. And that’s true, at least for me. My rubbish and recycling is collected and I don’t really think about what happens to it after that. Is as much of it recycled as I think, or is it just buried, burned or even sent to other countries? It’s not in front of my house, so I don’t really think about it – out of sight, out of mind.\nNeil Let’s listen again\nAlexandre Lemille Recycling is not the answer to waste from an efficient point of view because we are not able to get all the waste separated properly and therefore treated in the background. The main objective of our model is to hide waste so we don’t see as urban citizens, or rural citizens, we don’t see the waste, it is out of sight and therefore out of mind.\nNeil One possible solution to this problem is to develop what is called a circular economy. Here’s the presenter of Business Daily, Manuela Saragosa, explaining what that means.\nManuela Saragosa The idea then at the core of a circular economic and business model is that a product, like say a washing machine or even a broom, can always be returned to the manufacturer to be reused or repaired before then sold on again. The point is the manufacturer retains responsibility for the lifecycle of the product it produces rather than the consumer assuming that responsibility when he or she buys it.\nNeil So it seems like a simple idea – though maybe very difficult to do.\nSam Yes, the idea is that the company that makes a product, the manufacturer, is responsible for the product, not the person who bought it, the consumer.\nNeil So, if the product breaks or reaches the end of its useful life, its lifecycle, then the manufacturer has to take it back and fix, refurbish or have it recycled.\nSam I guess this would make manufacturers try to make their products last longer!\nNeil It certainly would. Let’s listen again.\nManuela Saragosa The idea then at the core of a circular economic and business model is that a product, like say a washing machine or even a broom, can always be returned to the manufacturer to be reused or repaired before then sold on again. The point is the manufacturer retains responsibility for the lifecycle of the product it produces rather than the consumer assuming that responsibility when he or she buys it.\nNeil That’s just about all we have time for in this programme. Before we recycle the vocabulary …\nSam Oh very good Neil!\nNeil Before we - thank you Sam - before we recycle the vocabulary, we need to get the answer to today’s question. Which country recycles the highest percentage of its waste? Is it:\nA: Sweden\nB: Germany\nC: New Zealand\nSam, what did you say?\nSam I think it’s Germany.\nNeil Well I would like to offer you congratulations because Germany is the correct answer. Now let’s go over the vocabulary.\nSam Of course. To separate means to divide or split different things, for example, separate your plastic from your paper for recycling.\nNeil Treating is the word for dealing with, for example, recycled waste.\nSam The phrase out of sight, out of mind, means ignoring something or a situation you can’t see.\nNeil A manufacturer is the person or company that makes something and the consumer is the person who buys that thing.\nSam And the length of time you can expect a product to work for is known as its lifecycle.\nNeil Well the lifecycle of this programme is 6 minutes, and as we are there, or thereabouts, it’s time for us to head off. Thanks for your company and hope you can join us again soon. Until then, there is plenty more to enjoy from BBC Learning English online, on social media and on our app. Bye for now.\nDo you chew gum and what do you do with it when you've finished? Listen to Rob and Finn discussing the history and chemical properties of gum and why it's messing up our streets whilst explaining some related vocabulary\nA London apartment block has front and back entrances for private and social housing - or so-called rich and poor doors. Does it make sense to you? Listen to a discussion whilst learning some housing-related vocabulary\nFifty years ago, on 18 March 1965, Soviet astronaut Alexei Leonov took the first space walk. Listen to Rob and Neil describing the struggles of that ground-breaking space mission whilst explaining some related vocabulary.\nFurniture with built-in wireless charging technology - like a coffee table is now being sold. 'Built-in' means the technology is included as part of the table. So you just pop your phone on the table, and technology does the rest!\nThe UK has become the first country to approve legislation allowing the creation of babies with genetic material from three people. Listen to Neil and Harry’s conversation and learn some related vocabulary.\nAn electronic device under your skin?! Workers in Sweden take part in experiment which allows them to get in and out of their office without a key, ID or password. Listen to Neil and Harry’s chat and learn some related vocabulary.\nThis year marks the 50th anniversary of Winston Churchill’s death. He is known throughout the world for his role in defeating Nazi Germany but he also made mistakes. Listen to Neil and Mike’s discussion, and learn new vocabulary.\nThe price of vaccines has escalated and some poor countries are struggling to prevent children from catching certain life-threatening diseases, says Medecins Sans Frontieres. Listen to Rob and Neil’s discussion, and learn some related vocabulary.\nAbout 37,000 tourists are expected to visit Antarctica this season. But should they be going to a region with such a sensitive environment? Listen to Rob and Neil’s conversation and learn some new vocabulary.\nAt a time when more people compete for fewer jobs, are you sure you present your skills and abilities well to a potential employer? Listen to Rob and Neil's conversation and learn some related vocabulary.\n\n",
   "length":8922,
   "wordcount":1920,
   "organisations":{
      "Business Daily":{
         "count":2,
         "label":"ORG"
      },
      "BBC":{
         "count":1,
         "label":"ORG"
      },
      [...]
   },
   "locations":[
      {
         "word":"Sweden",
         "spans":[
            {
               "start":463,
               "end":469
            }
         ],
         "country_predicted":"SWE",
         "country_conf":0.821003,
         "geo":{
            "admin1":"NA",
            "lat":"62",
            "lon":"15",
            "country_code3":"SWE",
            "geonameid":"2661886",
            "place_name":"Kingdom of Sweden",
            "feature_class":"A",
            "feature_code":"PCLI"
         }
      },
      {
         "word":"Germany",
         "spans":[
            {
               "start":473,
               "end":480
            }
         ],
         "country_predicted":"DEU",
         "country_conf":0.82085973,
         "geo":{
            "admin1":"NA",
            "lat":"51.5",
            "lon":"10.5",
            "country_code3":"DEU",
            "geonameid":"2921044",
            "place_name":"Federal Republic of Germany",
            "feature_class":"A",
            "feature_code":"PCLI"
         }
      },
      [...]
   ],
   "tags":"None",
   "frameworks":{
      "Key elements":{
         "Reusable, recyclable materials and inputs":{
            "description":"Using materials that can be easily reused or recycled after use",
            "similarity_score":0.18493474270532373,
            "id":188
         },
         "Using closed loop recycled materials":{
            "description":"Using waste materials that have been processed and recycled to produce new products within the same industry",
            "similarity_score":0.15232106609606666,
            "id":205
         },
         [...]
      },
      "Impacts":{
         "Reduce Material Consumption (SDG12)":{
            "description":"Reduced use of virgin materials and/or an increase of the use of secondary and bio-based materials",
            "similarity_score":0.1359634478611993,
            "id":74
         },
         "Minimise Waste (SDG12)":{
            "description":"Minimise waste through diversion: Instead of sending waste to landfill, it is redirected into other industrial processes for handling, treatment, recycling, recovery, or reuse in various forms. \n\nMinimise waste through design: At the outset of a process of project, plan and design such that there is zero waste or minimal waste during production, use, and at end of life. ",
            "similarity_score":0.10311407687906401,
            "id":75
         },
         [...]
      },
      "Industries":{
         "Fashion and Textiles":{
            "description":"Producing textile and leather products and processing them into apparel and accessories",
            "similarity_score":0.14508342641987992,
            "id":99
         },
         "Construction Materials and Products":{
            "description":"Producing building materials and finished and semi-finished building products for construction",
            "similarity_score":0.1449247980765617,
            "id":108
         },
         [...]
      },
      "Materials":{
         "Metal & ores":{
            "description":"<strong>What is it?</strong>\n<br>\nMetals are chemical elements that are extracted and processed from mineral ores. Metals, such as aluminum, iron, zinc, gold, silver, tin, and mercury represent a significant fraction of total material flows in the economy.\n<br>\n<strong>How is it produced? </strong>\n<br>\nMetals are elementary substances extracted from mineral ores. Ores are extracted from the environment through mining and quarrying activities. Metlas can be extracted from the ore by three main methods: reduction of the ore with carbon, reduction of the molten ore by electrolysis, and reduction of the ore with a more reactive metal (1). The process of refining uses a significant amount of energy, and consequently produces a large carbon footprint. \n<br>\n<strong>Where/how is it used in our economy (main sectors, main products, ingredients)?</strong>\n<br>\nMetals are omnipresent in common products across industries due to their wide range of functionalities and performance characteristics. Metals are essential for many of our product production processes. Over the 20th century demand has risen steeply, and this is expected to continue over the next decades.  The UN Environment Programme (UNEP) calculated that low-carbon technologies would need over 600 million tonnes (Mt) more metal resources up to 2050 (2).  Alongside the usual suspects of cobalt, lithium and rare-earth-metals, this includes aluminium, silver, steel, nickel, lead and zinc.\n<br>\n<strong>Why should we care from a circular economy perspective? (How is it un-circular?)</strong>\n<br>\n- Mining is energy and carbon intensive (3)\n- Scarce metals are mismanaged and are associated with social impacts (conflict minerals)\n- Given their recyclability and durability, circular economy solutions are a top priority. \n<br>\n\n(1) https://revisionscience.com/a2-level-level-revision/chemistry-level-revision/bonding-and-structure/reduction-metals-extraction-ore#:~:targetText=There%20are%203%20main%20methods,with%20a%20more%20reactive%20metal.\n<br>\n(2)  https://www.carbonbrief.org/explainer-these-six-metals-are-key-to-a-low-carbon-future\n<br>\n(3) Tost, M., Bayer, B., Hitch, M., Lutter, S., Moser, P., & Feiel, S. (2018). Metal Mining’s Environmental Pressures: A Review and Updated Estimates on CO2 Emissions, Water Use, and Land Requirements. Sustainability, 10(8), 2881.\n",
            "similarity_score":0.2284559500386977,
            "id":117
         },
         "Biomass":{
            "description":"<strong>What is it?</strong>\n<br>\nBiomass is the biodegradable fraction of products, waste and residues of biological origin from agriculture (including vegetal and animal substances), forestry, fisheries and aquaculture, as well as the biodegradable fraction of industrial and municipal waste. Includes bioliquids and biofuels. (1)\n<br>\n<strong>How is it produced? </strong>\n<br>\nBiomass is generated through the biocycle. (2) The cycling of nutrients is critical for the growth of all plant and animal life on the planet. At its most basic level, the natural cycle sees nutrients such as nitrogen, phosphorus and potassium absorbed from the soil by plants, which are then consumed by animals (including humans). These nutrients are subsequently excreted and returned to the soil, where plants can take them in again. Throughout the biocycle, biomass absorbs CO2 from the atmosphere while growing. This effect can be magnified when these materials are subsequently reused or recycled. (3)\n<br>\n<strong>Where/how is it used in our economy (main sectors, main products, ingredients)?</strong>\n<br>\nEvery year, people harvest roughly 13 billion tonnes of biomass globally to use as food, energy and materials. Biomass accounts for roughly 9% of world total primary energy supply today. (4) \nAdditionally, cities produce about 650 million tonnes of solid organic waste per year. (5)\n<br>\n<strong>Why should we care from a circular economy perspective?</strong>\n<br>\nBiomass use is confronted with some dilemmas, such as the use of biomass as an energy source by means of combustion or fermentation, versus a more high-value application (e.g. the processing of residual wood for furniture). For every application, the highest value must be recovered. A general rule of thumb is that the fewer process steps a material has to go through for reuse, the higher the quality of the material it can contain. This means that it is important to direct the use of renewable materials to applications where they contribute the most to sustainability.\n<br>\n(1) Source: https://www.ellenmacarthurfoundation.org/assets/downloads/publications/Urban-Biocycles_Ellen-MacArthurFoundation_30-3-2017.pdf\n<br>\n(2) Source: https://stats.oecd.org/glossary/detail.asp?ID=201\n<br>\n(3) Source: https://www.ellenmacarthurfoundation.org/assets/galleries/ce100/CE100-Renewables_Co.Project_Report.pdf\n<br>\n(4)  Source: https://www.iea.org/topics/renewables/bioenergy/\n<br>\n(5) Source: https://www.ellenmacarthurfoundation.org/assets/downloads/publications/Urban-Biocycles_Ellen-MacArthurFoundation_30-3-2017.pdf\n\n\n",
            "similarity_score":0.17078155376359366,
            "id":116
         },
         [...]
      },
      "Policies":{
         "Circular use of public-owned assets (land, buildings and equipment)":{
            "description":"None",
            "similarity_score":0.1442724794396174,
            "id":390
         },
         "Circular Economy in school programmes":{
            "description":"None",
            "similarity_score":0.12504899529179694,
            "id":335
         },
         [...]
      }
   }
}
```
## Authors

- [GitPeterJ](https://www.github.com/GitPeterJ)
- [Bowero](https://www.github.com/Bowero)
- [sranon](https://www.github.com/sranon)
## Feedback

If you have any feedback, please reach out to us at 0960634@hr.nl or 0958804@hr.nl.
