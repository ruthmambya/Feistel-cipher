import pandas as pd
import numpy as np
from argparse import ArgumentParser
from config import args
import pickle
from utils import preprocessing, new_dataframe, split_data
from model import BernoulliNaiveBayes
from config import args

parser = ArgumentParser()
parser.add_argument('-t','--text', help='Enter your text', default="AMMI for Bernoulli", required=True, type=str)
main_args=vars(parser.parse_args())

text=main_args["text"]
print(text)


data=pd.read_csv("./data/datasetProject.csv")
datamini=data.iloc[:10,:]

clean_data,vocabulary=preprocessing(datamini['review'].values, mode="train")
Good_data=new_dataframe(clean_data, datamini,voca=vocabulary, mode="train")

X_train, X_test, y_train, y_test =split_data(Good_data, 0.8)


bnb = BernoulliNaiveBayes(alpha=args.alpha)

y_pred=bnb.predict_new(text)

print("Test Acc. : ", f'{(np.sum(y_pred.reshape(-1,1)==y_test)/len(X_test)*100):.2f}',"%")

# filename='nvb.sav'
# pickle.dump(nvb, open(filename, 'wb'))