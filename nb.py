import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score,classification_report
from sklearn.preprocessing import LabelEncoder,StandardScaler

data=pd.read_csv('diabetes.csv')
target='Outcome'
data=data.dropna()

x=data.drop(columns=[target])
y=data[target]

x=pd.get_dummies(x)
if y.dtype == 'object':
    le = LabelEncoder()
    y= le.fit_transform(y)

x=StandardScaler().fit_transform(x)
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=42)

gnb=GaussianNB()

cv_score=cross_val_score(gnb,x,y,cv=5)
print(f'Cross validated scorre:{cv_score.mean()*100}')

gnb.fit(xtrain,ytrain)
y_pred=gnb.predict(xtest)

print("\nAccuacy score:",accuracy_score(ytest,y_pred))
print("\nclassification_report:\n",classification_report(ytest,y_pred))
