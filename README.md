## Goama Test Work

### How to run localy using runserver 

1. Clone the repository
```
$ git clone 
$ cd goama
```
2. Set .env file
```
ENV=local
DEBUG=True
```
3. Create virtual environment and Start run server
```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ python manage.py runserver
```

### How to run using Docker and redis as cache server

1. Clone the repository and following the commands bellow
```
$ git clone 
$ cd goama
```
2. Set .env file
```
ENV=dev
DEBUG=True
```
3. Run docker command
```
$ docker-compose up 
```

### Visit following url

1. http://127.0.0.1:8000/api/popular-queries/
2. http://127.0.0.1:8000/api/number-details/7/


