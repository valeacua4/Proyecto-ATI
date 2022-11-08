#!/usr/bin/env python
from flask import Flask, render_template
import flask

app = flask.Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/comentarios')
def comentarios():
    return render_template("comentarios.html")

@app.route('/publicacion')
def publicacion():
    return render_template("publicacion.html")

@app.route('/notificaciones')
def notificaciones():
    return render_template("notificaciones.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@app.route('/perfil')
def perfil():
    return render_template("ver-perfil.html")

@app.route('/perfil2')
def perfil2():
    return render_template("ver-perfil2.html")

@app.route('/perfil3')
def perfil3():
    return render_template("ver-perfil3.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyone