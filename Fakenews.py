import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import re
import string

df_fake=pd.read_csv("Fake.csv")
df_true=pd.read_csv("True.csv")
df_fake["class"]=0
df_true["class"]=1
df_merge=pd.concat([df_fake,df_true],axis=0)
df=df_merge.drop(["title","subject","date"],axis=1)
df=df.sample(frac=1)


def word_drop(text):

    text=text.lower()
    pattern = r'[' + string.punctuation + ']'
    text = re.sub(pattern, '', text)
    return text

df["text"]=df["text"].apply(word_drop)
x=df["text"]
y=df["class"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

vectorization = TfidfVectorizer()
xv_train = vectorization.fit_transform(x_train)
xv_test = vectorization.transform(x_test)

#logistic regression
LR = LogisticRegression()
LR.fit(xv_train,y_train)
pred_lr=LR.predict(xv_test)
#Decision Tree Classification
DT = DecisionTreeClassifier()
DT.fit(xv_train, y_train)
pred_dt = DT.predict(xv_test)
#Gradient Boosting Classifier
GBC = GradientBoostingClassifier(random_state=0)
GBC.fit(xv_train, y_train)
pred_gbc = GBC.predict(xv_test)
#Random Forest Classifier
RFC = RandomForestClassifier(random_state=0)
RFC.fit(xv_train, y_train)
pred_rfc = RFC.predict(xv_test)


def output_lable(n):
    if n == 0:
        return "Fake News"
    elif n == 1:
        return "Not A Fake News"


def manual_testing(news):
    testing_news = {"text": [news]}
    new_def_test = pd.DataFrame(testing_news)
    new_def_test["text"] = new_def_test["text"].apply(word_drop)
    new_x_test = new_def_test["text"]
    new_xv_test = vectorization.transform(new_x_test)
    pred_LR = LR.predict(new_xv_test)
    pred_DT = DT.predict(new_xv_test)
    pred_GBC = GBC.predict(new_xv_test)
    pred_RFC = RFC.predict(new_xv_test)

    return print("\n\nLR Prediction: {} \nDT Prediction: {} \nGBC Prediction: {} \nRFC Prediction: {}".format(
        output_lable(pred_LR[0]),
        output_lable(pred_DT[0]),
        output_lable(pred_GBC[0]),
        output_lable(pred_RFC[0])))

news = str(input("Enter news : "))
manual_testing(news)


