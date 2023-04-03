import json
import pandas as pd
import pickle
from flask import Flask, render_template, request

# creating a Flask app instance
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# prediction function
def Predictor(to_predict_dict):
    # numericlabels = {'age', 'capital_gain', 'capital_loss', 'hours_per_week'}
    stringlabels = {'workclass', 'education', 'marital_status', 'occupation', 'sex', 'native_country', 'salary'}

    with open('label_mappings.json', 'r') as fio:
        label_mappings_dict = json.load(fio)

    for key, val in to_predict_dict.items():
        if key in stringlabels:
            val = label_mappings_dict[key][val]
        to_predict_dict[key] = [int(val)]
    
    to_predict = pd.DataFrame.from_dict(to_predict_dict, orient='columns')
    print(to_predict)
    
    loaded_model = pickle.load(open("model.pkl", "rb"))
    prediction = loaded_model.predict(to_predict)
    prediction = prediction.tolist()
    return prediction[0]


@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        to_predict_dict = request.form.to_dict()
        prediction = Predictor(to_predict_dict)
        
        if prediction == 1:
            response = "Income more than 50k"
        else:
            response = "Income less than 50k" 

        return render_template('result.html', prediction_response=response)
    else:
        return render_template('result.html', prediction_response="Error")
        
if __name__=='__main__':
    app.run('0.0.0.0', port=5000, debug=True)