FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install python-pip python-dev build-essential
COPY . /main
CMD ["main.py"]
