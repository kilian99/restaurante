from flask import Flask, Blueprint, render_template, request, redirect, url_for

rutas_espana = Blueprint("ruta_espana", __name__)

@rutas_espana.route('/')
def index():
    return render_template('index.html')

@rutas_espana.route('/verespana')
def verespana():
    return render_template('españa/espana.html')

@rutas_espana.route('/madrid')
def vermadrid():
    return render_template('españa/madrid.html')

@rutas_espana.route('/barcelona')
def verbarcelona():
    return render_template('españa/barcelona.html')

@rutas_espana.route('/sevilla')
def versevilla():
    return render_template('españa/sevilla.html')