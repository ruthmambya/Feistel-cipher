import pandas as pd
import numpy as np
from argparse import ArgumentParser
from utils import bag_of_words, split_doc, clean, get_voc, conv_label
from model import BernoulliNB
from confing import args
import pickle

parser = ArgumentParser()
parser.add_argument('-t','--text', help='Enter your text', default="patato is sweet", required=True, type=str)
main_args=vars(parser.parse_args())

text=main_args["text"]
# print(text)

corpus=pd.read_csv("./data/datasetProject.csv", header=0)
corpus_clean = clean(corpus)

splitted_corps = split_doc(corpus_clean)
voc = get_voc(splitted_corps)
X=np.array([bag_of_words(split_doc(corpus_clean)[i], voc) for i in range(len(split_doc(corpus_clean)))])

corpus_clean["sentiment"] = corpus_clean["sentiment"].map(conv_label)
y=corpus_clean[["sentiment"]].values

nb=BernoulliNB(voc=voc, alpha=args.alpha).fit(np.where(X>0,1),y) #Binarizing X

y_pred=nb.predict(X)

print("Test Acc. : ", (np.sum(y_pred.reshape(-1,1)==y)/len(X)*100),"%")

filename='nb.sav'
pickle.dump(nb, open(filename, 'wb'))


