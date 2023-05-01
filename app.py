import pickle
from flask import Flask, request, jsonify, app, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

svmmodel = pickle.load(open('titanic_model0.1.0.pkl', 'rb'))
scaler = pickle.load(open('scaling.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.json('data')
    print(data)
    print(np.array(list(data.values())).reshape(-1,1))
    new_data = scaler.transforn(np.array(list(data.values)).reshape(-1,1))
    output = svmmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='8080', debug=True)
    