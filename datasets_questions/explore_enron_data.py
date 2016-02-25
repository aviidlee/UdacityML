#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

def get_numPOIs():
    numPOIs = 0
    for features in enron_data.values():
        if(features['poi']):
            numPOIs = numPOIs + 1

    print "The number of persons of interest is ", numPOIs
    return numPOIs

def quantified_salary():
    qSal = 0
    for features in enron_data.values():
        if(features['salary'] !='NaN'):
            qSal = qSal + 1

    return qSal

def known_email():
    emails = 0
    for features in enron_data.values():
        if(features['email_address'] !='NaN'):
            emails = emails + 1

    return emails

def missing_total_payments():
    missing = 0
    for features in enron_data.values():
        if(features['total_payments'] == 'NaN'):
            missing = missing + 1

    return missing
            
def pois_missing_payments():
    missing = 0
    for features in enron_data.values():
        if(features['poi'] and features['total_payments'] == 'NaN'):
            missing = missing + 1

    return missing

