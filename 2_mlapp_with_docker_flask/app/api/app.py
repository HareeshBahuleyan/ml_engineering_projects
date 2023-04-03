from flask import Flask, jsonify, request
from text_preprocessing import TextPreprocessor
from utilities import load_model_pipeline, predict_labels

app = Flask(__name__)

@app.before_first_request
def load_models():
    # this step means we load the model only once
    # also helps in pickling and unpickling
    # as per https://rebeccabilbro.github.io/module-main-has-no-attribute/
    # and https://stackoverflow.com/questions/49483732/why-does-my-flask-app-work-when-executing-using-python-app-py-but-not-when-usi
    global model_pipeline
    model_pipeline = load_model_pipeline()

@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text was passed'})

    sample = [sample]
    predictions = predict_labels(model_pipeline, sample)
    print(predictions)

    try:
        result = jsonify(predictions[0])
    except TypeError as e:
        return jsonify({'error': str(e)})

    return result

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)