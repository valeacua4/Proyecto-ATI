FROM python:3.11.0rc2-alpine3.16
WORKDIR /myWorkDir
COPY ./requirements.txt .
COPY ./requirements.txt ./src
RUN pip install -r requirements.txt
CMD ./app.py