

import numpy as np

class BernoulliNaiveBayes:
    
    def __init__(self, alpha = 1):
        self.alpha = alpha
        return
    
    def fit(self, X, y):
        
        # count number of occurrences for each label
        y_counts = np.unique(y, return_counts=True)[1]
        
        self.n_classes = len(np.unique(y))
        self.n_features = X.shape[1]
        
        # calculate P(y), the probability of observing any message of class y
        class_prior = y_counts / y_counts.sum()
        self.log_class_prior = np.expand_dims(np.log(class_prior), axis = 1)
        
        # calculate P(x|y), the probability of observing message x given it is class y
        prob_x_given_y = np.zeros([self.n_classes, self.n_features])
        
        # for each class of y
        for i in range(self.n_classes):
            
            # select only rows of class y
            row_mask = (y == i) 
            X_filtered = X[row_mask, :]
            
            # get number of messages of each word appears in ( P(x and y) )
            numerator = (X_filtered.sum(axis = 0) + self.alpha)
            
            # get number messages in class y (scalar) ( P(y) )
            denominator = (X_filtered.shape[0] + 2 * self.alpha)
            
            # P(x|y) = P(x and y) / P(y)
            prob_x_given_y[i, :] = numerator / denominator
            
        # Calculate log probabilities for P(x|y) and P(~x|y)
        self.log_class_conditional_positive = np.log(prob_x_given_y) # k x n matrix
        self.log_class_conditional_negative = np.log(1 - prob_x_given_y) # k x n matrix
            
    def predict(self, X):
        
        #X = X.todense() # m x d matrix
        
        # log P(y|x) is proportional to log P(x|y) + log P(y)
        # each n x 1 column vector is contains a value proportional to P(y|x)
        # for every possible class of y
        log_probs_positive = self.log_class_conditional_positive.dot(X.T) # n x m matrix
        log_probs_negative = self.log_class_conditional_negative.dot(1 - X.T) # n x m matrix        
        log_likelihoods = log_probs_positive + log_probs_negative # n x m matrix
        log_joint_likelihoods = log_likelihoods + self.log_class_prior # n x m matrix
        
        # for each column vector, find class y that maximizes P(y|x)
        preds = np.argmax(log_joint_likelihoods, axis = 0) # 1 x m matrix
        preds = np.array(preds).squeeze() # m-dimensional vector
        return preds

#====================================

#This function predict the new document

    def predict_new(x_new):
        df=pd.DataFrame({"Sentence":[x_new]})
        x,_=preprocessing(df['Sentence'].values,mode="test")
        x_new=new_dataframe(x, f=None,voca=vocabulary, mode="test")
        return bnb.predict(x_new)



































# from utils import bag_of_words

# class BernoulliNB(object):
#     def __init__(self, voc, alpha=1.0):
#         self.alpha=alpha
#         self.voc=voc
#         self.feature_prob=None

#     def fit(self, X,y):
#         count_sample=X.shape[0]
#         separated=[[x for x, t in zip(X,y) if t==c] for c in np.unique(y)]
#         self.class_log_prior_ = [np.log(len(i) / count_sample) for i in separated]
#         count = np.array([np.array(i).sum(axis=0) for i in separated]) + self.alpha
#         smooting = 2*self.alpha
#         n_doc=np.array([len(i) + smooting for i in separated])

#         self.feature_prob = count / n_doc[np.newaxis].T
#         return self

#     def predict_log_proba(self,X):
#         return [(np.log(self.feature_prob) * np.abs(x-1)).sum(axis=1) + self.class_log_prior_ for x in X]

#     def predict(self, X):
#         return np.argmax(self.predict_log_proba(X), axis=1)
    
#     def predict_new(self, x_new):
#         x_new=x_new.split()
#         x_new=[i.lowe() for i in x_new]
#         x_new=bag_of_words(x_new,self.voc)

#         return np.argmax(self.predict(x_new))


