from python:stretch

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY . /opt/app

CMD ["python", "kreationen.py", "speisen2.txt"]
