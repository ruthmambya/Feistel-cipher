# import pandas as pd
# import numpy as np
# from argparse import ArgumentParser
from utils import preprocessing, new_dataframe, split_data
from model import BernoulliNaiveBayes
from config import args
from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, confusion_matrix

import pandas as pd
import numpy as np
# import nltk
# nltk.download('stopwords')
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# import nltk.tokenize as tokenize
# import re
# import string
# from collections import defaultdict
# import csv
# from sklearn.feature_extraction.text import CountVectorizer
# from collections import Counter
# from scipy.sparse import csr_matrix
# import plotly
# import plotly.graph_objs as go
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud,STOPWORDS
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix, accuracy_score, f1_score, confusion_matrix

# import pickle
# from sklearn.model_selection import train_test_split





# parser = ArgumentParser()
# parser.add_argument('-t','--text', help='Enter your text', default="patato is sweet", required=True, type=str)
# main_args=vars(parser.parse_args())

# text=main_args["text"]
# print(text)

# corpus=pd.read_csv("./data/datasetProject.csv", header=0)
# corpus=corpus.iloc[:20]

# corpus_clean = corpus.copy()
# # corpus_clean = clean(corpus)

# splitted_corps = split_doc(corpus_clean)
# voc = get_voc(splitted_corps)
# X=np.array([bag_of_words(split_doc(corpus_clean)[i], voc) for i in range(len(split_doc(corpus_clean)))])

# corpus_clean["sentiment"] = corpus_clean["sentiment"].map(conv_label)
# y=corpus_clean[["sentiment"]].values

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

# # nb=BernoulliNB(voc=voc, alpha=args.alpha).fit(np.where(X>0,1),y) #Binarizing X
# nb=BernoulliNaiveBayes(alpha=args.alpha).fit(X_train,y_train) #Binarizing X

# y_pred=nb.predict(X_test)

# print("Test Acc. : ", f'{(np.sum(y_pred.reshape(-1,1)==y_test)/len(X_test)*100):.2f}',"%")

# filename='nb.sav'
# pickle.dump(nb, open(filename, 'wb'))








data=pd.read_csv("./data/datasetProject.csv")
datamini=data.iloc[:10,:]
# print(data.head(20))

clean_data,vocabulary=preprocessing(datamini['review'].values, mode="train")
Good_data=new_dataframe(clean_data, datamini,voca=vocabulary, mode="train")
# print(Good_data.head())

X_train, X_test, y_train, y_test =split_data(Good_data, 0.8)

bnb = BernoulliNaiveBayes(alpha=args.alpha)
bnb.fit(np.array(X_train), np.array(y_train))
y_pred = bnb.predict(X_test)
print('test accuracy:', accuracy_score(y_test, y_pred))
print('macro f1 score:', f1_score(y_test, y_pred, average='macro'))
