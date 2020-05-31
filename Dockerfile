FROM python:3

RUN git clone https://github.com/JessePonkman/tp5_docker.git

WORKDIR /tp5_docker

CMD ["python3", "main.py"] && ["python3", "testPersonService.py"]
