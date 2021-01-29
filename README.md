# django_microservices
This app is used to demonstrate a microservice architecture for a django based app. To install django use:
```
pip install django
pip install djangorestframework
```
The complete application also used [REACT FRAMEWORK](https://reactjs.org/) for its frontend which is in another repository. The main app is hosted using [**flask**](https://flask.palletsprojects.com/en/1.1.x/). The application communicates using [RABBITMQ](https://www.rabbitmq.com/download.html). We use docker container to deploy and ship the application. To learn more about docker and its usage, follow [Docker](https://www.docker.com/).

The repository for the main app is:
- [Main app](https://github.com/pratd/flask_app)
- [Frontend app](https://github.com/pratd/REACT_CRUD_frontend)

To run the app, run the docker-compose files as:
```
-  docker-compose --build
- docker-compose --up

```