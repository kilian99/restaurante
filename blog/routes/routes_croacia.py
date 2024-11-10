from flask import Flask, Blueprint, render_template, request, redirect, url_for



rutas_croacia = Blueprint("ruta_croacia", __name__)

@rutas_croacia.route('/')
def index():
    return render_template('index.html')

@rutas_croacia.route('/vercroacia')
def vercroacia():
    return render_template('croacia/croacia.html')

@rutas_croacia.route('/zagreb')
def verzagreb():
    return render_template('croacia/zagreb.html')

@rutas_croacia.route('/zadar')
def verzadar():
    return render_template('croacia/zadar.html')

@rutas_croacia.route('/split')
def versplit():
    return render_template('croacia/split.html')