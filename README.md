# ELK-flask toy project

[flask logging with ELK](#flask logging with ELK)
   - [Download Git](#Download Git)
   - [Set And Run ELK with Docker](#Set And Run ELK with Docker)
   - [Activate Virtual Env and Install flask and requirement packages](#Activate Virtual Env and Install flask and requirement packages)
   - [Run Flask server](#Run Flask server)
# flask logging with ELK

**Requirements ELK with Docker**
**flask**

## Download Git

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

## Set And Run ELK with Docker

Docker로 ELK를 세팅

```bash
#Project Root Dir (ELK-docker-python) 기준
$ cd docker-elk
$ docker-compose up -d # ELK의 모든 로그를 보고싶다면, -d를 없애준다
```

## Activate Virtual Env and Install flask and requirement packages

### activate virtual env

```bash
$ virtualenv venv && source venv/bin/activate
```

### install requirements

```bash
$ install -r requirements.txt
```

## Run Flask server

```bash
#Project Root Dir (ELK-docker-python) 기준
$ flask run
```