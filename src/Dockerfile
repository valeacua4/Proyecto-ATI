FROM python:3.11.0rc2-alpine3.16
WORKDIR /myWorkDir
COPY requirements.txt /src
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ./app.py