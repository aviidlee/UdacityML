#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
import operator

sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )

# Remove NaNs 
data_dict = {k: v for k, v in data_dict.iteritems() if v['salary'] != 'NaN'}
# Remove TOTAL 
data_dict.pop('TOTAL',0)

# Print name of the guy getting the biggest salary
biggestEarner = max(data_dict.iteritems(), key= lambda entry : entry[1]["salary"])[0]
print data_dict.iteritems()
print biggestEarner, " earns ", data_dict[biggestEarner]["salary"]

# Find the two people who have 5M+ bonuses 
bigBonus = {k:v for k, v in data_dict.iteritems() if v['bonus'] > 5000000 and v['salary'] > 1000000}
print "The guys with really big bonuses: ", bigBonus.keys()

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter(salary, bonus)

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()