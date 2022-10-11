FROM python:3.8.5-alpine3.12
WORKDIR /myWorkDir
COPY requirements.txt /src
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ./app.py