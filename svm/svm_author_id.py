#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import svm 

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

def run_svm(kernel, c, data_cut, features_train, features_test, labels_train, labels_test):
    print "Running SMV with c = ", c

    features_train = features_train[:len(features_train)/data_cut]
    labels_train = labels_train[:len(labels_train)/data_cut]  
    
    clf = svm.SVC(kernel=kernel, C=c)
    print "Training the SVM..."
    t0 = time()
    clf.fit(features_train, labels_train)
    print "Finished training."
    print "training time:", round(time()-t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "prediction time:", round(time()-t0, 3), "s"

    accuracy = clf.score(features_test, labels_test)
    print(accuracy)

    return pred

print sum(run_svm('rbf', 10000, 1, features_train, features_test, labels_train, labels_test))


