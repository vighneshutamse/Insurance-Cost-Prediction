from flask import Flask, render_template, request
#import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_forest_regressor_model.pkl', 'rb'))
@app.route('/',methods=['GET'])

def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])

def predict():
    # Fuel_Type_Diesel=0
    if request.method == 'POST':
        age = int(request.form['age'])
        sex = int(request.form['gender'])
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker'])
        region = int(request.form['region'])
        
        prediction=model.predict([[age,sex,bmi,children,smoker,region]])
        output=round(prediction[0],2)
        if output<0:
            return render_template('result.html',prediction="Sorry, you cannot get the insurance")
        else:
            return render_template('result.html',prediction="Your insurance cost is: {}$".format(output))


if __name__=="__main__":
    app.run(debug=True)