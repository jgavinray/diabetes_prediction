import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
# Read data into pandas dataframe
df=pd.read_csv(r'data/diabetes.csv')
#Define Feature Matrix (X) and Label Array (y)
X=df.drop(['Outcome'],axis=1)
y=df['Outcome']
lr=RandomForestClassifier(n_estimators=53, n_jobs=1,random_state=8)
lr.fit(X,y)

#Serialize the model and save
import joblib
joblib.dump(lr, 'models/randomfs.pkl')
print("Random Forest Model Saved")
#Load the model
lr = joblib.load('models/randomfs.pkl')
# Save features from training
rnd_columns = list(X.columns)
joblib.dump(rnd_columns, 'models/rnd_columns.pkl')
print("Random Forest Model Colums Saved")
