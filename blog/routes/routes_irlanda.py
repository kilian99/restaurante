from flask import Flask, Blueprint, render_template, request, redirect, url_for



rutas_irlanda = Blueprint("ruta_irlanda", __name__)

@rutas_irlanda.route('/')
def index():
    return render_template('index.html')

@rutas_irlanda.route('/verirlanda')
def verirlanda():
    return render_template('irlanda/irlanda.html')

@rutas_irlanda.route('/dublin')
def verdublin():
    return render_template('irlanda/dublin.html')

@rutas_irlanda.route('/galway')
def vergalway():
    return render_template('irlanda/galway.html')

@rutas_irlanda.route('/cork')
def vercork():
    return render_template('irlanda/cork.html')