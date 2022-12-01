from flask import Flask, render_template, request, redirect, url_for
from forms import SignupForm, PostForm, LoginForm
from flask_login import LoginManager, login_required, login_user, current_user
from models import users
from werkzeug.urls import url_parse
from pymongo import MongoClient
from authlib.integrations.flask_client import OAuth
from flask_socketio import SocketIO, send
import os
import json

app = Flask(__name__)
app.config['TESTING'] = False
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['MONGO_DBNAME'] = 'prueba'
app.config["MONGO_URI"] = 'mongodb://bd:27017/'
login_manager = LoginManager(app)
login_manager.login_view = "user.login"
oauth = OAuth(app)
app.config['SECRET'] = "secret!123"
socketio = SocketIO(app, cors_allowed_origins="*")

# Establecemos conexión
<<<<<<< HEAD
mongodb_client = MongoClient('mongodb://bd:27017/')
# Seleccionamos nuestra base de datos
db = mongodb_client['miapp_ati']
my_coleccion= db["prueba"]
inserte = {"name": "Prueba", "sueldo": "100"}
result = my_coleccion.insert_one(inserte)
# Seleccionamos una colección
# print(db.list_database_names())

=======

# Seleccionamos nuestra base de datos
#db = mongodb_client.test_database
# Seleccionamos una colección
#my_coleccion= db.Nombre_Coleccion
>>>>>>> origin/cambiosVictor

mongodb_client = MongoClient('mongodb://bd:27017/')
db = mongodb_client["db_ati"]
co_usuarios = db["usuarios"]
co_amigo = db["amigo"]
co_publicacion = db["publicacion"]
co_media = db["media"]
co_comentario = db["comentario"]
co_chat = db["chat"]
co_mensaje = db["mensaje"]
co_configuracion = db["configuracion"]
co_lenguaje = db["lenguaje"]
co_perfil= db["perfil"]
co_notificacion = db["notificacion"]

with open('datos_BD.json') as j:
    mydata = json.load(j)
    print(mydata)

#inserte = {"name": "Prueba", "sueldo": "100"}
result = co_usuarios.insert_many(mydata)
print("result")

posts = []

@app.route("/")
def index():
    return render_template("home.html", posts=posts)

@app.route("/p/<string:slug>/")
def show_post(slug):
    return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/", methods=['GET', 'POST'], defaults={'post_id': None})
@app.route("/admin/post/<int:post_id>/", methods=['GET', 'POST'])
@login_required
def post_form(post_id):
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data

        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)

        return redirect(url_for('home'))
    return render_template("admin/post_form.html", form=form)

@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        lastname = form.lastname.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, lastname)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('iniciosesion1')
        return redirect(next_page)
    return render_template("signup_form.html", form=form)

@login_manager.user_loader
def load_user(user_id):
    for user in users:
        if user.id == int(user_id):
            return user
    return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home')
            return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/login1', methods=['GET', 'POST'])
def login1():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('home')
            return redirect(next_page)
    return render_template('iniciosesion1.html', form=form)

@app.route("/restartpassword/", methods=["GET", "POST"])
def restartpassword():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = get_user(form.email.data)
        password = form.password.data
        # Creamos el usuario y lo guardamos
        user = User(len(users) + 1, name, email, lastname)
        users.append(user)
        # Dejamos al usuario logueado
        login_user(user, remember=True)
        next_page = request.args.get('next', None)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('home')
        return redirect(next_page)
    return render_template("signup_form.html", form=form)

@socketio.on('message')
def handle_message(message):
    print("Mensaje Recibido: " + message)
    if message != "Conectado":
        send(message, broadcast=True)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/cambiarcontraseña')
def cambiarcontraseña():
    return render_template("cambiarcontraseña.html")

@app.route('/restablecer')
def restablecer():
    return render_template("restablecer.html")
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
    return render_template("Chat2.html")

@app.route('/perfil')
def perfil():
    return render_template("ver-perfil.html")

@app.route('/perfil2')
def perfil2():
    return render_template("ver-perfil2.html")

@app.route('/perfil3')
def perfil3():
    return render_template("ver-perfil3.html")


@app.route('/editarperfil')
def editarPerfil():
    return render_template("editar-perfil.html")

@app.route('/configuracion')
def configuracion():
    return render_template("configuracion.html")

@app.route('/facebook/')
def facebook():
   
    # Facebook Oauth Config
    FACEBOOK_CLIENT_ID = os.environ.get('870556254115719')
    FACEBOOK_CLIENT_SECRET = os.environ.get('be73f05f925a788270c33e5c52948575')
    oauth.register(
        name='facebook',
        client_id=FACEBOOK_CLIENT_ID,
        client_secret=FACEBOOK_CLIENT_SECRET,
        access_token_url='https://graph.facebook.com/oauth/access_token',
        access_token_params=None,
        authorize_url='https://www.facebook.com/dialog/oauth',
        authorize_params=None,
        api_base_url='https://graph.facebook.com/',
        client_kwargs={'scope': 'email'},
    )
    redirect_uri = url_for('facebook_auth', _external=True)
    return oauth.facebook.authorize_redirect(redirect_uri)
 
@app.route('/facebook/auth/')
def facebook_auth():
    token = oauth.facebook.authorize_access_token()
    resp = oauth.facebook.get(
        'https://graph.facebook.com/me?fields=id,name,email,picture{url}')
    profile = resp.json()
    print("Facebook User ", profile)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyone

    print("epaa")
    