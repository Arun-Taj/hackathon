import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import os
#creating tthe TF+IDFvectorizer 
def predict_disease(symptoms):
    df =pd.read_csv('medicine.csv')
    #displaying the dataframe
    #print(df)
    x= df['symptoms'].values
    y_disease=df['disease']
    y_medicine=df['medicine']

    vectorizer =TfidfVectorizer()
    #transforming symptoms array into TF_IDF vectorizer
    x_tfidf=vectorizer.fit_transform(x)
    #splitting the data into training and testing sets
    x_train, x_test,y_disease_train,y_disease_test,y_medicine_train,y_medicine_test=train_test_split(
        x_tfidf,y_disease,y_medicine,test_size=0.2,random_state=70)
    #creating and training a logistic regression model
    disease_classifier = LogisticRegression()
    disease_classifier.fit(x_train,y_disease_train)
    #training the classifier for predicting medicine
    medicine_classifier=LogisticRegression()
    medicine_classifier.fit(x_train,y_medicine_train)
    #checking the accuracy of the model
    disease_accuracy=disease_classifier.score(x_test,y_disease_test)
    medicine_accuracy=medicine_classifier.score(x_test,y_medicine_test)
    symptoms_tfidf=vectorizer.transform(symptoms)

    response={
        "predicted_disease":disease_classifier.predict(symptoms_tfidf),
        "predicted_medicine":medicine_classifier.predict(symptoms_tfidf),
    }

    return response
