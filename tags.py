import yake
import letras
import search
import json
import search

text = letras.lirica
language = "en"
max_ngram_size = 1
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 18

custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = str(custom_kw_extractor.extract_keywords(text))

characters = " []-()*''.1234567890"
for x in range(len(characters)):
    keywords = keywords.replace(characters[x],"")

format = keywords.split(',')
print (format)

# descripition = "Original song: " +search.link+ '\n\nLyrics: \n\n'+letras.lirica+'\n\nObrigado Por Estar Aqui♡'
# dados = {
#    "title" : letras.yttitle ,
#    "description" : "Original song: "+ search.link +'\nlyrics:\n'+letras.lirica+'\n\nObrigado Por Estar Aqui♡',
#    "tags" : [ format[0] , format[2] , format[4] , format[6] , format[8] , format[10] , format[12] , format[14] , format[16] , format[18] , format[20] , format[22] , format[24] , format[26] , format[28] , format[0] , format[0] , format[0] ]
# }
# with open('dados.json', 'w') as json_file:
#     json.dump(dados, json_file, indent=4)

# print (dados.json)    