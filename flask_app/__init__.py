from flask import Flask

app = Flask(__name__)
app.secret_key = "clave_secreta_super_segura"


from flask_app.controllers import usuarios