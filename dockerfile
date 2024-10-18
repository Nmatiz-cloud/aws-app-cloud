FROM python:3.9.16

WORKDIR /project/flask

COPY . .

run pip install -r requirement.txt

CMD ["python", "./flask/server.py"]

