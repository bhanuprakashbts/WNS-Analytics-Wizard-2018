import numpy as np
import pandas as pd
import re

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
sample = pd.read_csv("Sample_Submission.csv")

train.dtypes
test.isnull().sum()
#no profiling for department variable
###########################################################################
#region variable profiling

train.region =train.region.astype(str)
train_region = train.region.tolist()
import re
for i in range(len(train_region)):
    train_region[i] =re.sub("region_34","B",train_region[i])
    train_region[i] =re.sub("region_33","C",train_region[i])
    train_region[i] =re.sub("region_32","C",train_region[i])
    train_region[i] =re.sub("region_31","E",train_region[i])
    train_region[i] =re.sub("region_30","H",train_region[i])
    train_region[i] =re.sub("region_29","C",train_region[i])
    train_region[i] =re.sub("region_28","K",train_region[i])
    train_region[i] =re.sub("region_27","G",train_region[i])
    train_region[i] =re.sub("region_26","E",train_region[i])
    train_region[i] =re.sub("region_25","L",train_region[i])
    train_region[i] =re.sub("region_24","C",train_region[i])
    train_region[i] =re.sub("region_23","K",train_region[i])
    train_region[i] =re.sub("region_22","J",train_region[i])
    train_region[i] =re.sub("region_21","C",train_region[i])
    train_region[i] =re.sub("region_20","E",train_region[i])
    train_region[i] =re.sub("region_19","E",train_region[i])
    train_region[i] =re.sub("region_18","B",train_region[i])
    train_region[i] =re.sub("region_17","M",train_region[i])
    train_region[i] =re.sub("region_16","F",train_region[i])
    train_region[i] =re.sub("region_15","G",train_region[i])
    train_region[i] =re.sub("region_14","F",train_region[i])
    train_region[i] =re.sub("region_13","H",train_region[i])
    train_region[i] =re.sub("region_12","F",train_region[i])
    train_region[i] =re.sub("region_11","E",train_region[i])
    train_region[i] =re.sub("region_10","G",train_region[i])
    train_region[i] = re.sub("region_9","A",train_region[i])
    train_region[i] =re.sub("region_8","G",train_region[i])
    train_region[i] =re.sub("region_7","J",train_region[i])
    train_region[i] =re.sub("region_6","D",train_region[i])
    train_region[i] =re.sub("region_5","D",train_region[i])
    train_region[i] =re.sub("region_4","M",train_region[i])
    train_region[i] =re.sub("region_3","J",train_region[i])
    train_region[i] =re.sub("region_2","G",train_region[i])
    train_region[i] =re.sub("region_1","I",train_region[i])

train.region = train_region
train.region.unique()
########################################################################
#missing values education in train and test
train.education = train.education.fillna("Unknown")
train.education.value_counts()

train.education =train.education.astype(str)
train_education = train.education.tolist()
import re
for i in range(len(train_education)):
    train_education[i] = re.sub("Unknown", "Others", train_education[i])
    train_education[i] = re.sub("Below Secondary", "Others", train_education[i])
    train_education[i] = re.sub("Bachelor's", "Others", train_education[i])

train.education = train_education
train.education.unique()
########################################################################
#no profiling for recruitment_channel variable
#no profiling for no of trainings variable
train.no_of_trainings = train.no_of_trainings.astype('category')

#age variable profiling
train.age =train.age.astype(str)
train_age = train.age.tolist()
for i in range(len(train_age)):
    train_age[i] = re.sub("60","D",train_age[i])
    train_age[i] = re.sub("59","F",train_age[i])
    train_age[i] = re.sub("58","F",train_age[i])
    train_age[i] = re.sub("57","A",train_age[i])
    train_age[i] = re.sub("56","F",train_age[i])
    train_age[i] = re.sub("55","D",train_age[i])
    train_age[i] = re.sub("54","F",train_age[i])
    train_age[i] = re.sub("53","B",train_age[i])
    train_age[i] = re.sub("52","F",train_age[i])
    train_age[i] = re.sub("51","G",train_age[i])
    train_age[i] = re.sub("50","D",train_age[i])
    train_age[i] = re.sub("49","E",train_age[i])
    train_age[i] = re.sub("48","F",train_age[i])
    train_age[i] = re.sub("47","C",train_age[i])
    train_age[i] = re.sub("46","D",train_age[i])
    train_age[i] = re.sub("45","D",train_age[i])
    train_age[i] = re.sub("44","F",train_age[i])
    train_age[i] = re.sub("43","F",train_age[i])
    train_age[i] = re.sub("42","F",train_age[i])
    train_age[i] = re.sub("41","F",train_age[i])
    train_age[i] = re.sub("40","F",train_age[i])
    train_age[i] = re.sub("39","G",train_age[i])
    train_age[i] = re.sub("38","H",train_age[i])
    train_age[i] = re.sub("37","F",train_age[i])
    train_age[i] = re.sub("36","F",train_age[i])
    train_age[i] = re.sub("35","H",train_age[i])
    train_age[i] = re.sub("34","G",train_age[i])
    train_age[i] = re.sub("33","H",train_age[i])
    train_age[i] = re.sub("32","F",train_age[i])
    train_age[i] = re.sub("31","G",train_age[i])
    train_age[i] = re.sub("30","G",train_age[i])
    train_age[i] = re.sub("29","G",train_age[i])
    train_age[i] = re.sub("28","H",train_age[i])
    train_age[i] = re.sub("27","G",train_age[i])
    train_age[i] = re.sub("26","F",train_age[i])
    train_age[i] = re.sub("25","C",train_age[i])
    train_age[i] = re.sub("24","F",train_age[i])
    train_age[i] = re.sub("23","F",train_age[i])
    train_age[i] = re.sub("22","F",train_age[i])
    train_age[i] = re.sub("21","C",train_age[i])
    train_age[i] = re.sub("20","B",train_age[i])


train.age = train_age
train.age.unique()
########################################################################
#previous year rating variable profiling
#missing values previous year rating in train and test

train.previous_year_rating = train.previous_year_rating.fillna(4)
train.previous_year_rating = train.previous_year_rating.astype('category')

########################################################################

#LENGTH OF SERVICE variable profiling
train.length_of_service = train.length_of_service.astype(str)
train.length_of_service.value_counts()
train_length_of_service = train.length_of_service.tolist()
train_length_of_service1 = train.length_of_service.tolist()
for i in range(len(train_length_of_service)):
    train_length_of_service[i] = re.sub("37","L",train_length_of_service[i])
    train_length_of_service[i] = re.sub("34","A",train_length_of_service[i])
    train_length_of_service[i] = re.sub("33","L",train_length_of_service[i])
    train_length_of_service[i] = re.sub("32","B",train_length_of_service[i])
    train_length_of_service[i] = re.sub("31","L",train_length_of_service[i])
    train_length_of_service[i] = re.sub("30","L",train_length_of_service[i])
    train_length_of_service[i] = re.sub("29","D",train_length_of_service[i])
    train_length_of_service[i] = re.sub("28","G",train_length_of_service[i])
    train_length_of_service[i] = re.sub("27","K",train_length_of_service[i])
    train_length_of_service[i] = re.sub("26","L",train_length_of_service[i])
    train_length_of_service[i] = re.sub("25","J",train_length_of_service[i])
    train_length_of_service[i] = re.sub("24","L",train_length_of_service[i])
    train_length_of_service[i] = re.sub("23","C",train_length_of_service[i])
    train_length_of_service[i] = re.sub("22","D",train_length_of_service[i])
    train_length_of_service[i] = re.sub("21","I",train_length_of_service[i])
    train_length_of_service[i] = re.sub("20","F",train_length_of_service[i])
    train_length_of_service[i] = re.sub("19","D",train_length_of_service[i])
    train_length_of_service[i] = re.sub("18","H",train_length_of_service[i])
    train_length_of_service[i] = re.sub("17","H",train_length_of_service[i])
    train_length_of_service[i] = re.sub("16","G",train_length_of_service[i])
    train_length_of_service[i] = re.sub("15","G",train_length_of_service[i])
    train_length_of_service[i] = re.sub("14","I",train_length_of_service[i])
    train_length_of_service[i] = re.sub("13","F",train_length_of_service[i])
    train_length_of_service[i] = re.sub("12","F",train_length_of_service[i])
    train_length_of_service[i] = re.sub("11","D",train_length_of_service[i])
    train_length_of_service[i] = re.sub("10","E",train_length_of_service[i])
    train_length_of_service[i] = re.sub("9","E",train_length_of_service[i])
    train_length_of_service[i] = re.sub("8","E",train_length_of_service[i])
    train_length_of_service[i] = re.sub("7","F",train_length_of_service[i])
    train_length_of_service[i] = re.sub("6","F",train_length_of_service[i])
    train_length_of_service[i] = re.sub("5","F",train_length_of_service[i])
    train_length_of_service[i] = re.sub("4","E",train_length_of_service[i])
    train_length_of_service[i] = re.sub("3","E",train_length_of_service[i])
    train_length_of_service[i] = re.sub("2","E",train_length_of_service[i])
    train_length_of_service[i] = re.sub("1","F",train_length_of_service[i])
    
    
train.length_of_service = train_length_of_service
train.length_of_service.unique()
########################################################################

train.dtypes
training_data = train.drop(["employee_id","is_promoted"], axis = 1)
training_data = pd.get_dummies(training_data)

training_label = train[["is_promoted"]]


test.dtypes
#no profiling for department variable
###########################################################################
#region variable profiling

test.region =test.region.astype(str)
test_region = test.region.tolist()
import re
for i in range(len(test_region)):
    test_region[i] =re.sub("region_34","B",test_region[i])
    test_region[i] =re.sub("region_33","C",test_region[i])
    test_region[i] =re.sub("region_32","C",test_region[i])
    test_region[i] =re.sub("region_31","E",test_region[i])
    test_region[i] =re.sub("region_30","H",test_region[i])
    test_region[i] =re.sub("region_29","C",test_region[i])
    test_region[i] =re.sub("region_28","K",test_region[i])
    test_region[i] =re.sub("region_27","G",test_region[i])
    test_region[i] =re.sub("region_26","E",test_region[i])
    test_region[i] =re.sub("region_25","L",test_region[i])
    test_region[i] =re.sub("region_24","C",test_region[i])
    test_region[i] =re.sub("region_23","K",test_region[i])
    test_region[i] =re.sub("region_22","J",test_region[i])
    test_region[i] =re.sub("region_21","C",test_region[i])
    test_region[i] =re.sub("region_20","E",test_region[i])
    test_region[i] =re.sub("region_19","E",test_region[i])
    test_region[i] =re.sub("region_18","B",test_region[i])
    test_region[i] =re.sub("region_17","M",test_region[i])
    test_region[i] =re.sub("region_16","F",test_region[i])
    test_region[i] =re.sub("region_15","G",test_region[i])
    test_region[i] =re.sub("region_14","F",test_region[i])
    test_region[i] =re.sub("region_13","H",test_region[i])
    test_region[i] =re.sub("region_12","F",test_region[i])
    test_region[i] =re.sub("region_11","E",test_region[i])
    test_region[i] =re.sub("region_10","G",test_region[i])
    test_region[i] = re.sub("region_9","A",test_region[i])
    test_region[i] =re.sub("region_8","G",test_region[i])
    test_region[i] =re.sub("region_7","J",test_region[i])
    test_region[i] =re.sub("region_6","D",test_region[i])
    test_region[i] =re.sub("region_5","D",test_region[i])
    test_region[i] =re.sub("region_4","M",test_region[i])
    test_region[i] =re.sub("region_3","J",test_region[i])
    test_region[i] =re.sub("region_2","G",test_region[i])
    test_region[i] =re.sub("region_1","I",test_region[i])

test.region = test_region
test.region.unique()
########################################################################
#missing values education in test and test
test.education = test.education.fillna("Unknown")
test.education.value_counts()

test.education =test.education.astype(str)
test_education = test.education.tolist()
import re
for i in range(len(test_education)):
    test_education[i] = re.sub("Unknown", "Others", test_education[i])
    test_education[i] = re.sub("Below Secondary", "Others", test_education[i])
    test_education[i] = re.sub("Bachelor's", "Others", test_education[i])

test.education = test_education
test.education.unique()
########################################################################
#no profiling for recruitment_channel variable
#no profiling for no of testings variable
test.no_of_trainings = test.no_of_trainings.astype('category')

#age variable profiling
test.age =test.age.astype(str)
test_age = test.age.tolist()
for i in range(len(test_age)):
    test_age[i] = re.sub("60","D",test_age[i])
    test_age[i] = re.sub("59","F",test_age[i])
    test_age[i] = re.sub("58","F",test_age[i])
    test_age[i] = re.sub("57","A",test_age[i])
    test_age[i] = re.sub("56","F",test_age[i])
    test_age[i] = re.sub("55","D",test_age[i])
    test_age[i] = re.sub("54","F",test_age[i])
    test_age[i] = re.sub("53","B",test_age[i])
    test_age[i] = re.sub("52","F",test_age[i])
    test_age[i] = re.sub("51","G",test_age[i])
    test_age[i] = re.sub("50","D",test_age[i])
    test_age[i] = re.sub("49","E",test_age[i])
    test_age[i] = re.sub("48","F",test_age[i])
    test_age[i] = re.sub("47","C",test_age[i])
    test_age[i] = re.sub("46","D",test_age[i])
    test_age[i] = re.sub("45","D",test_age[i])
    test_age[i] = re.sub("44","F",test_age[i])
    test_age[i] = re.sub("43","F",test_age[i])
    test_age[i] = re.sub("42","F",test_age[i])
    test_age[i] = re.sub("41","F",test_age[i])
    test_age[i] = re.sub("40","F",test_age[i])
    test_age[i] = re.sub("39","G",test_age[i])
    test_age[i] = re.sub("38","H",test_age[i])
    test_age[i] = re.sub("37","F",test_age[i])
    test_age[i] = re.sub("36","F",test_age[i])
    test_age[i] = re.sub("35","H",test_age[i])
    test_age[i] = re.sub("34","G",test_age[i])
    test_age[i] = re.sub("33","H",test_age[i])
    test_age[i] = re.sub("32","F",test_age[i])
    test_age[i] = re.sub("31","G",test_age[i])
    test_age[i] = re.sub("30","G",test_age[i])
    test_age[i] = re.sub("29","G",test_age[i])
    test_age[i] = re.sub("28","H",test_age[i])
    test_age[i] = re.sub("27","G",test_age[i])
    test_age[i] = re.sub("26","F",test_age[i])
    test_age[i] = re.sub("25","C",test_age[i])
    test_age[i] = re.sub("24","F",test_age[i])
    test_age[i] = re.sub("23","F",test_age[i])
    test_age[i] = re.sub("22","F",test_age[i])
    test_age[i] = re.sub("21","C",test_age[i])
    test_age[i] = re.sub("20","B",test_age[i])


test.age = test_age
test.age.unique()
########################################################################
#previous year rating variable profiling
#missing values previous year rating in test and test

test.previous_year_rating = test.previous_year_rating.fillna(4)
test.previous_year_rating = test.previous_year_rating.astype('category')

########################################################################

#LENGTH OF SERVICE variable profiling
test.length_of_service = test.length_of_service.astype(str)
test.length_of_service.value_counts()
test_length_of_service = test.length_of_service.tolist()
test_length_of_service1 = test.length_of_service.tolist()
for i in range(len(test_length_of_service)):
    test_length_of_service[i] = re.sub("37","L",test_length_of_service[i])
    test_length_of_service[i] = re.sub("34","A",test_length_of_service[i])
    test_length_of_service[i] = re.sub("33","L",test_length_of_service[i])
    test_length_of_service[i] = re.sub("32","B",test_length_of_service[i])
    test_length_of_service[i] = re.sub("31","L",test_length_of_service[i])
    test_length_of_service[i] = re.sub("30","L",test_length_of_service[i])
    test_length_of_service[i] = re.sub("29","D",test_length_of_service[i])
    test_length_of_service[i] = re.sub("28","G",test_length_of_service[i])
    test_length_of_service[i] = re.sub("27","K",test_length_of_service[i])
    test_length_of_service[i] = re.sub("26","L",test_length_of_service[i])
    test_length_of_service[i] = re.sub("25","J",test_length_of_service[i])
    test_length_of_service[i] = re.sub("24","L",test_length_of_service[i])
    test_length_of_service[i] = re.sub("23","C",test_length_of_service[i])
    test_length_of_service[i] = re.sub("22","D",test_length_of_service[i])
    test_length_of_service[i] = re.sub("21","I",test_length_of_service[i])
    test_length_of_service[i] = re.sub("20","F",test_length_of_service[i])
    test_length_of_service[i] = re.sub("19","D",test_length_of_service[i])
    test_length_of_service[i] = re.sub("18","H",test_length_of_service[i])
    test_length_of_service[i] = re.sub("17","H",test_length_of_service[i])
    test_length_of_service[i] = re.sub("16","G",test_length_of_service[i])
    test_length_of_service[i] = re.sub("15","G",test_length_of_service[i])
    test_length_of_service[i] = re.sub("14","I",test_length_of_service[i])
    test_length_of_service[i] = re.sub("13","F",test_length_of_service[i])
    test_length_of_service[i] = re.sub("12","F",test_length_of_service[i])
    test_length_of_service[i] = re.sub("11","D",test_length_of_service[i])
    test_length_of_service[i] = re.sub("10","E",test_length_of_service[i])
    test_length_of_service[i] = re.sub("9","E",test_length_of_service[i])
    test_length_of_service[i] = re.sub("8","E",test_length_of_service[i])
    test_length_of_service[i] = re.sub("7","F",test_length_of_service[i])
    test_length_of_service[i] = re.sub("6","F",test_length_of_service[i])
    test_length_of_service[i] = re.sub("5","F",test_length_of_service[i])
    test_length_of_service[i] = re.sub("4","E",test_length_of_service[i])
    test_length_of_service[i] = re.sub("3","E",test_length_of_service[i])
    test_length_of_service[i] = re.sub("2","E",test_length_of_service[i])
    test_length_of_service[i] = re.sub("1","F",test_length_of_service[i])
    
    
test.length_of_service = test_length_of_service
test.length_of_service.unique()
########################################################################



prediction_data = pd.get_dummies(test.drop("employee_id",axis = 1))
prediction_data['no_of_trainings_10'] = 0

import random
random.seed(400)

import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

neural_net=Sequential()
neural_net.add(Dense(output_dim=5000,init='uniform',activation='relu',input_dim=67))
neural_net.add(Dense(output_dim=1,init='uniform',activation='sigmoid'))
neural_net.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
neural_net.fit(training_data,training_label,batch_size=132,epochs=20)

prediction = neural_net.predict(prediction_data)
prediction1 = (prediction>0.5)
sample["is_promoted"] = prediction1
sample["is_promoted"] = sample["is_promoted"].astype("int")
sample["is_promoted"].value_counts()

sample.to_csv('prediction_file_18.csv',index=False)