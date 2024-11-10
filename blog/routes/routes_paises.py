from flask import Flask, Blueprint, render_template, request, redirect, url_for
from app import db
from app.data.pais_dao import Pais_dao

rutas_paises = Blueprint("ruta_pais", __name__)

@rutas_paises.route('/')
def index():
    return render_template('index.html')

@rutas_paises.route('/verpaises')
def verpaises():
    pais_dao = Pais_dao()
    paises = pais_dao.select_all(db)

    return render_template('adminpaises.html', paises=paises)

@rutas_paises.route('/addpaises', methods=['POST'])   
def addpaises():
    pais_dao = Pais_dao()

    nombre = request.form['nombre']

    if (nombre == ""):
        return redirect(url_for('ruta_pais.verpaises'))

    pais_dao.insert(db,nombre)
    return redirect(url_for('ruta_pais.verpaises'))    

@rutas_paises.route('/delpaises', methods=['POST'])   
def delpaises():
    id = request.form['id']
    pais_dao = Pais_dao()
    pais_dao.delete(db,id)
   
    return redirect(url_for('ruta_pais.verpaises'))  

@rutas_paises.route('/updatepaises', methods=['POST'])   
def updatepaises():
    pais_dao = Pais_dao()

    nombre = request.form['nombre']

    if (nombre == ""):
        pais_dao.update(db,nombre)
        
    return redirect(url_for('ruta_pais.verpaises'))