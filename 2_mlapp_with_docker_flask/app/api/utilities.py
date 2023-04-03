import pickle
from text_preprocessing import TextPreprocessor


def load_model_pipeline(path='models/model.pkl'):
    with open(path, 'rb') as fio:
        model_pipeline = pickle.load(fio)
    print(f'Loaded model successfully from {path}')
    return model_pipeline


def predict_labels(model_pipeline, texts):
    predictions = model_pipeline.predict(texts)
    pred_to_label = {0: 'business', 1: 'tech', 2: 'politics', 3: 'sport', 4: 'entertainment'}
    
    # Make a list of texts with their respective predictions
    data = []
    for t, pred in zip(texts, predictions):
        data.append({'text': t, 'pred': int(pred), 'label': pred_to_label[pred]})
        
    return data
    

if __name__ =='__main__':
    # Random texts to be classified
    texts=['avatar in 3d set to be released at the cinemas mid december',
           'cryptocurrency crash and the bear market are consequences of the fed rate hike',
           'argentina defeat france to become world champions in one of the most exciting sporting events that the world has ever witnessed',
          ]
    model_pipeline = load_model_pipeline(path='models/model.pkl')
    predictions = predict_labels(model_pipeline, texts)
    print(predictions)