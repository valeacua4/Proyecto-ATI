FROM python:3.11.0rc2-alpine3.16
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development 
COPY requirements.txt .
COPY /src /workdir
RUN pip install -r requirements.txt
WORKDIR /workdir/src
CMD ["flask","run"]