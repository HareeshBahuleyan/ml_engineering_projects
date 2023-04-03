# Exposing ML Model as a Microservice with Docker + Kubernetes

[https://www.youtube.com/watch?v=fDsJO7jKOO8](https://www.youtube.com/watch?v=fDsJO7jKOO8)

### **+ Adding adding Kubernetes to the stack**

[Deploy Machine Learning Model using Flask , Docker and Minikube Kubernetes Cluster](https://www.youtube.com/watch?v=A3y5UHKoMPs)

One issue that I faced was directly accessing the docker IP address (without port forwarding) as shown in the video (which seems to be done on a Linux system). Apparently on Mac and Windows, it is not possible without changing some system settings:

- Same issue as this user: [https://stackoverflow.com/questions/69644254/flask-api-hosted-as-a-docker-container-works-with-localhost5000-but-not-with-17](https://stackoverflow.com/questions/69644254/flask-api-hosted-as-a-docker-container-works-with-localhost5000-but-not-with-17)
- Solution: [https://github.com/docker/for-mac/issues/2670](https://github.com/docker/for-mac/issues/2670)

Follow the `minikube` instructions as per the video, but to get the URL of your app to test locally, run the command:

```python
minikube service --url salarypredapp
```

[https://www.techbeatly.com/how-to-access-applications-deployed-in-minikube-kubernetes-cluster/](https://www.techbeatly.com/how-to-access-applications-deployed-in-minikube-kubernetes-cluster/)

Alternate video (more recent and more explanation):

[https://www.youtube.com/watch?v=DQRNt8Diyw4](https://www.youtube.com/watch?v=DQRNt8Diyw4)

### **+ Using Poetry for Dependency Management**

[https://www.youtube.com/watch?v=0f3moPe_bhk](https://www.youtube.com/watch?v=0f3moPe_bhk)

### **+ Using a HTML form to submit your features to the Flask APP**

[How To Use Forms In Python Flask](https://vegibit.com/how-to-use-forms-in-python-flask/)