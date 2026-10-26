from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.usuarios import Usuario

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/registro', methods=['POST'])
def registro():
    # Guardamos el nombre ingresado en el registro
    session['nombre'] = request.form['nombre']
    return redirect('/bienvenido')

@app.route('/login', methods=['POST'])
def login():
    session['nombre'] = request.form['email']
    return redirect('/bienvenido')

@app.route('/bienvenido')
def bienvenido():
    if 'nombre' not in session:
        return redirect('/')
    return render_template('bienvenido.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')