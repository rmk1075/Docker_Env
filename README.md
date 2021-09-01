# Docker_Env

study about docker for setting up dev environment

## python_env

ubuntu 18.04 이미지를 기반으로 python3 개발 환경을 설치한 이미지를 Dockerfile을 사용하여 빌드

### 1. Dockerfile

새로운 image 생성을 위한 명령어들을 작성해놓은 파일.

#### Dockerfile 예시

```dockerfile
# FROM: build 하는 image의 기반이 되는 parent image
FROM ubuntu:18.04

# LABEL: image의 meta data로 key-value pair로 구성된다.
# 해당 예제에서는 author를 설정
LABEL author="jamie <rmk1075@gmail.com>"

# RUN: 스크립트나 명령을 실행한다.
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-dev build-essential

# WORKDIR: RUN, CMD, ENTRYPOINT, COPY, ADD 등의 명령어가 실행되는 디렉토리 위치.
WORKDIR /home/app/

# COPY <src> <dest>: 로컬의 <src>의 파일들을 도커 컨테이너의 <dest>로 복사한다.
COPY test_v01/ .
RUN pip3 install --no-cache-dir -r requirements.txt
```

### 2. Docker build

Dockerfile을 빌드하여 새로운 docker image를 생성한다.

```sh
$ docker build .

# -f option으로 해당 경로에 있는 dockerfile로 빌드한다.
$ docker build -f /path/to/a/Dockerfile .

# -t option으로 image에 tag를 준다.
$ docker build -t test/myapp .
```

## composetest

docker-compose를 이용하여 dockerfile의 이미지 빌드 및 서비스 설정, 실행

### 1. docker-compose.yml

```yaml
version: "3.9"
services:
  # web과 redis 두가지 service 정의
  # service - web
  web:
    # build from the Dockerfile in current directory
    build: .
    # binds the containser and the host machine to the exposed port, 5000
    ports:
      - "5000:5000"
    # mount the project directory (./) on the host to /code inside the container
    volumes:
      - .:/code
    # set the FLASK_ENV environment variable to development
    environment:
      FLASK_ENV: development
  # service - redis 
  redis:
    # use a public Redis image pulled from the Docker Hub registry
    image: "redis:alpine"
```

### 2. run docker-compose

```sh
$ docker-compose up

# -d : detach 옵션 사용하여 background 실행
$ docker-compose up -d

# 현재 실행 중인 프로세스 확인
$ docker-compose ps
```

- reference: <https://docs.docker.com/compose/gettingstarted/>
