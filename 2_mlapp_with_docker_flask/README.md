# Machine Learning App with Flask & Docker

**Part 1: Developing the application**

- Interesting part was to build a scikit-learn pipeline
- And create your own TextPreprocessor class which was part of the pipeline (the main idea is to inherit sklearn classes `BaseEstimator`, `TransformerMixin` - and to have a `fit` and `transform` functions defined)
    
    [https://www.youtube.com/watch?v=S--SD4QbGps](https://www.youtube.com/watch?v=S--SD4QbGps)
    

**Part 2: Dockerizing the Flask application**

- Learnings - using docker compose (generally used when you have multiple services)
- [Major Learning] When pickling (during ML dev in Jupyter notebook) and unpickling (in the flask app) the sklearn pipeline which contained the custom `TextPreprocessor`, I ran into multiple issues around Flask not able to understand the `TextPreprocessor` namespace and where to load it from when unpickling. Eventually understood that the way to resolve it is having the `TextPreprocessor` class in a separate python file - which is imported similarly when pickling (during ML dev in Jupyter notebook) and unpickling (in the flask app).
    
    [Module Main has No Attribute... (on Pipelines and Pickles)](https://rebeccabilbro.github.io/module-main-has-no-attribute/)
    
    [Why does my Flask app work when executing using `python app.py` but not when using `heroku local web` or `flask run`?](https://stackoverflow.com/questions/49483732/why-does-my-flask-app-work-when-executing-using-python-app-py-but-not-when-usi)
    
- How to use Postman - an application for testing REST APIs with requests
- How to publish your docker image to docker hub and run docker compose in future that directly pull the image from docker hub
    
    [https://www.youtube.com/watch?v=zGP_nYmZd9c&t=0s](https://www.youtube.com/watch?v=zGP_nYmZd9c&t=0s)