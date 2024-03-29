# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 16:48:50 2019

@author: adeyetob
"""
# Importing the libraies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

# Features Matrix
X = dataset.iloc[:, :-1].values
#Vector of dependent variables
y = dataset.iloc[:, 3].values

#if you can't see the full array, just run np.set_printoptions(threshold = np.nan)

# Taking care of missing data ++ Original Version
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)
#imputer = imputer.fit(X[:, 1:3])
#X[:, 1:3] = imputer.transform(X[:, 1:3])

#Taking care of missing data ++ Future Version
#from sklearn.impute import SimpleImputer
#missingvalues = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose = 0)
#missingvalues = missingvalues.fit(X[:, 1:3])



#Taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="most_frequent")
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])


#Encoding categorical data ++Future Version
#from sklearn.preprocessing import OneHotEncoder, LabelEncoder
#from sklearn.compose import ColumnTransformer
#
#transformer = ColumnTransformer(
#    transformers=[
#        ("OneHot",        # Just a name
#         OneHotEncoder(), # The transformer class
#         [0]              # The column(s) to be applied on.
#         )
#    ],
#    remainder='passthrough' # donot apply anything to the remaining columns
#)
#X = transformer.fit_transform(X.tolist())
#labelencoder_y = LabelEncoder()
#y = labelencoder_y.fit_transform(y)


#Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)












