#load from kobill
import csv
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import math
import pandas as pd

from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
from konlpy.corpus import kobill
docs_ko = [kobill.open(i).read() for i in kobill.fileids()]
#Tokenize
from konlpy.tag import Okt; t = Okt()
pos = lambda d: ['/'.join(p) for p in t.pos(d)]
texts_ko = [pos(doc) for doc in docs_ko]

from gensim.models import word2vec
wv_model_ko1 = word2vec.Word2Vec(texts_ko)
wv_model_ko1.init_sims(replace=True)

wv_model_ko2 = word2vec.Word2Vec(texts_ko, size=100, min_count=50, window=3, workers=4, iter=100, sg=1)
wv_model_ko2.init_sims(replace=True)

wv_model_ko3 = word2vec.Word2Vec(texts_ko, size=100, window=3, workers=4, iter=100, sg=1)
wv_model_ko3.init_sims(replace=True)

f1 = open("result1.txt", 'a')
f2 = open("result2.txt", 'a')
f3 = open("result3.txt", 'a')

want_word = input()
a = pos(want_word)
result1 = (wv_model_ko1.most_similar(a, topn=500))
result2 = (wv_model_ko2.most_similar(a, topn=500))
result3 = (wv_model_ko3.most_similar(a, topn=500))

onlyWordList = list()
f1.write(want_word + "\n")
f2.write(want_word + "\n")
f3.write(want_word + "\n")

for i in range(len(result1)):
    word_splited = result1[i][0].split('/')
    if word_splited[1] == "Noun" or word_splited[1] == "KoreanParticle" or word_splited[1] == "Modifier" or \
                    word_splited[1] == "Adjective" or word_splited[1] == "Adverb":

        print(i, ". word: ", result1[i][0], " cos similarity: ", result1[i][1], '\n')
        store_string = str(i) + ". word: " + str(result1[i][0]) + " cos similarity: " + str(result1[i][1]) + "\n"
        f1.write(store_string)

        onlyWordList.append(word_splited)
    elif word_splited[1] == "Verb":
        print(i, ". word: ", result1[i][0], " cos similarity: ", result1[i][1], '\n')
        store_string = str(i) + ". word: " + str(result1[i][0]) + " cos similarity: " + str(result1[i][1]) + "\n"
        f1.write(store_string)
        onlyWordList.append((kkma.pos(word_splited[0]))[0])
print("\n\n")
for i in range(len(result2)):
    word_splited = result2[i][0].split('/')
    if word_splited[1] == "Noun" or word_splited[1] == "KoreanParticle" or word_splited[1] == "Modifier" or \
                    word_splited[1] == "Adjective" or word_splited[1] == "Adverb":
        print(i, ". word: ", result2[i][0], " cos similarity: ", result2[i][1], '\n')
        store_string = str(i) + ". word: " + str(result2[i][0]) + " cos similarity: " + str(result2[i][1]) + "\n"
        f2.write(store_string)
        onlyWordList.append(word_splited)
    elif word_splited[1] == "Verb":
        print(i, ". word: ", result2[i][0], " cos similarity: ", result2[i][1], '\n')
        store_string = str(i) + ". word: " + str(result2[i][0]) + " cos similarity: " + str(result2[i][1]) + "\n"
        f2.write(store_string)
        onlyWordList.append((kkma.pos(word_splited[0]))[0])
print("\n\n")
for i in range(len(result3)):
    word_splited = result3[i][0].split('/')
    if word_splited[1] == "Noun" or word_splited[1] == "KoreanParticle" or word_splited[1] == "Modifier" or \
                    word_splited[1] == "Adjective" or word_splited[1] == "Adverb":

        print(i, ". word: ", result3[i][0], " cos similarity: ", result3[i][1], '\n')
        store_string = str(i) + ". word: " + str(result3[i][0]) + " cos similarity: " + str(result3[i][1]) + "\n"
        f3.write(store_string)

        onlyWordList.append(word_splited)
    elif word_splited[1] == "Verb":
        print(i, ". word: ", result3[i][0], " cos similarity: ", result3[i][1], '\n')
        store_string = str(i) + ". word: " + str(result3[i][0]) + " cos similarity: " + str(result3[i][1]) + "\n"
        f3.write(store_string)
        onlyWordList.append((kkma.pos(word_splited[0]))[0])

f1.wirte("\n\n")
f2.wirte("\n\n")
f3.wirte("\n\n")
f1.close()
f2.close()
f3.close()
print("end")