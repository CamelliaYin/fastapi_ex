# base image
FROM python:3.8.10-slim

# cd to:
WORKDIR /app

# copy everything from the current dir to the work dir
COPY . /app

# get ready by install the dependencies in the docker image
RUN pip install -r requirements.txt
