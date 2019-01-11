FROM python:3.7-alpine

WORKDIR /opt/app
COPY . /opt/app
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "kreationen.py", "speisen2.txt"]
