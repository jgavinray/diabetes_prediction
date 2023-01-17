# Diabetes Prediction
![](images/diabetus.jpeg)

### Requirements
Python 3.10  
`pip install -r requirements`

### Build the model
`python create_model.py`

### Serve Model
`python webserver.py`

Once the server is running you can get a prediction:  
`curl localhost:12345/prediction -d '[{"Pregnancies":7,"Glucose":120,"BloodPressure":90,"SkinThickness":23,"Insulin":135,"BMI":25,"DiabetesPedigreeFunction":0.5,"Age":45}]' -X POST -H 'content-type: application/json'`

### Dataset
[Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) is in data/diabetes.csv