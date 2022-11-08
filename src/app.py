#!/usr/bin/env python
from flask import Flask, render_template
import flask

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("home.html")
@app.route('/perfil')
def perfil():
    return render_template("ver-perfil.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyone