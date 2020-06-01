# ELK-flask toy project

[flask logging with ELK](#flask logging with elk)
   - [Download Git](#download git)
   - [Set And Run ELK with Docker](#set and run elk with docker)
   - [Activate Virtual Env and Install flask and requirement packages](#activate virtual env and install flask and requirement packages)
   - [Run Flask server](#run flask server)
   
# flask logging with elk

**Requirements ELK with Docker**
**flask**

## download git

[paullee714/ELK-docker-python](https://github.com/paullee714/ELK-docker-python/tree/54d5bdb24aceef6023eee2c80b0ffe3e866f4edf)

```bash
tree -L 2
ELK-docker-python
├── README.md
├── docker-elk
│   ├── LICENSE
│   ├── README.md
│   ├── docker-compose.yml
│   ├── docker-stack.yml
│   ├── elasticsearch
│   ├── extensions
│   ├── kibana
│   └── logstash
├── elk-flask
│   ├── __pycache__
│   ├── app.py
│   ├── elk_lib
│   └── route
├── requirements.txt
└── venv
    ├── bin
    ├── lib
    └── pyvenv.cfg
```

## set and run elk with docker

Docker로 ELK를 세팅

```bash
#Project Root Dir (ELK-docker-python) 기준
$ cd docker-elk
$ docker-compose up -d # ELK의 모든 로그를 보고싶다면, -d를 없애준다
```

## activate virtual env and install flask and requirement packages

### activate virtual env

```bash
$ virtualenv venv && source venv/bin/activate
```

### install requirements

```bash
$ install -r requirements.txt
```

## run flask server

```bash
#Project Root Dir (ELK-docker-python) 기준
$ flask run
```