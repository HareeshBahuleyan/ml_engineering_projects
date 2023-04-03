FROM python:3.9

RUN mkdir /mlapp_microservice_on_kubernetes

COPY . /mlapp_microservice_on_kubernetes

WORKDIR /mlapp_microservice_on_kubernetes

EXPOSE 5000

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install --only=main --no-root
CMD poetry run flask run --host=0.0.0.0 --port=5000

# RUN poetry export -f requirements.txt --output requirements.txt
# RUN pip install -r requirements.txt
# CMD python app.py
