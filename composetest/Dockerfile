# syntax=docker/dockerfile:1

# Build an Image starting with the Python 3.7 image
FROM python:3.7-alpine

# set the working directory to /code
WORKDIR /code

# set environment varriables used by the flask command
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# install gcc and other dependencies
RUN apk add --no-cache gcc musl-dev linux-headers

# copy requirements.txt and install the python dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# add metadata to the image to describe that the container is listening on port 5000
EXPOSE 5000

# copy the current directory . in project to the workdir . in the image
COPY . .

# set the default command for the container to 'flask run'
CMD ["flask", "run"]