
#load from kobill
from konlpy.corpus import kobill
docs_ko = [kobill.open(i).read() for i in kobill.fileids()]
#Tokenize
from konlpy.tag import Okt; t = Okt()
pos = lambda d: ['/'.join(p) for p in t.pos(d)]
texts_ko = [pos(doc) for doc in docs_ko]

from gensim.models import word2vec
wv_model_ko = word2vec.Word2Vec(texts_ko)
wv_model_ko.init_sims(replace=True)
wv_model_ko.save('ko_word2vec_e.model')

from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()

want_word = input()
a = pos(want_word)
result = (wv_model_ko.most_similar(a, topn=100))

print(result)