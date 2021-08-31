# Docker_Env

study about docker for setting up dev environment

## python_env

ubuntu 18.04 이미지를 기반으로 python3 개발 환경을 설치한 이미지를 Dockerfile을 사용하여 빌드

### 1. Dockerfile

새로운 image 생성을 위한 명령어들을 작성해놓은 파일.

#### Dockerfile 예시

```python
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
