"""
Adapted from https://github.com/CarlosML27/salary-ml
"""
import pickle
import json
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn import tree

TRAIN_RATIO = 0.9
DATA_FILEPATH = "data/salary.csv"
MODEL_SAVEPATH = "model.pkl"
LABEL_MAPPINGS_SAVEPATH = "label_mappings.json"

def replace_missing_data(data):
	data.replace(["NaN"], np.nan, inplace = True)
	data = data.apply(lambda x:x.fillna(x.value_counts().index[0]))
	return data

def parse_integer_values(data):
	numericlabels = ['age', 'capital_gain', 'capital_loss', 'hours_per_week']
	for label in numericlabels:
		data[label] = data[label].astype('int32')
	return data

def encode_string_values(data):
	labelencoder = LabelEncoder()
	stringlabels = ['workclass', 'education', 'marital_status', 'occupation', 'sex', 'native_country', 'salary']
	label_mappings_dict = {}
	for label in stringlabels:
		data[label] = labelencoder.fit_transform(data[label])
		label_mappings_dict[label] = dict(zip(labelencoder.classes_, labelencoder.transform(labelencoder.classes_).tolist()))
	
	with open(LABEL_MAPPINGS_SAVEPATH, 'w') as fio:
		json.dump(label_mappings_dict, fio)
    
	return data

def get_data(filename):
	data = pd.read_csv(filename, sep=",", header=0, na_values=["?"])
	data = replace_missing_data(data)
	data = parse_integer_values(data)
	data = encode_string_values(data)
	return data

def split_train_test_data(data, training_ratio):
	X = data.drop(columns=['salary'])
	print(X.columns)
	Y = data['salary'].values.tolist()
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1-training_ratio)
	return X_train, X_test, Y_train, Y_test

def create_dtc(X, Y):
	decision_tree_classifier = tree.DecisionTreeClassifier()
	decision_tree_classifier = decision_tree_classifier.fit(X, Y)
	return decision_tree_classifier

def get_accuracy(classifier, X, Y):
	accuracy = classifier.score(X, Y)
	return accuracy

def get_prediction(classifier, X):
	prediction = classifier.predict(X)
	return prediction

def get_confusion_matrix(prediction, Y):
	confusion_matrix = confusion_matrix(prediction, Y)
	return confusion_matrix

def main():
	print("Prepare dataset and train model...")
	data = get_data(DATA_FILEPATH)
	X_train, X_test, Y_train, Y_test = split_train_test_data(data, TRAIN_RATIO)
	decision_tree_classifier = create_dtc(X_train, Y_train)
	dtc_accuracy = get_accuracy(decision_tree_classifier, X_test, Y_test) 
	
	print(f"Accuracy: {round(dtc_accuracy*100, 4)}")
	dtc_prediction = get_prediction(decision_tree_classifier, X_test)
	dtc_confusion_matrix = confusion_matrix(dtc_prediction, Y_test)
	print(dtc_confusion_matrix)
	
	print("Save model as pickle object...")
	pickle.dump(decision_tree_classifier, open(MODEL_SAVEPATH, 'wb'))
	print(f'Saved model successfully at {MODEL_SAVEPATH}')
	

if __name__ == '__main__':
	main()