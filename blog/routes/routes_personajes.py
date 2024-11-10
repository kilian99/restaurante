from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.personajes_dao import Personajes_dao
from app.data.pais_dao import Pais_dao

rutas_personajes = Blueprint("ruta_personaje", __name__)

@rutas_personajes.route('/')
def index():
    return render_template('adminpersonajes.html')

@rutas_personajes.route('/verpersonaje', methods=['POST','GET'])
def verpersonaje():
    Personajes = list()
    nombrePais = ""
    pais_dao = Pais_dao()
    paises = pais_dao.select_all(db)

    if (request.method == 'POST'):
        id_pais = request.form['id_pais']
        personaje_dao = Personajes_dao()
        Personajes = personaje_dao.select_all(db,id_pais)
        for pais in paises:
            
            if (id_pais == int(pais.id)):
               
                nombrePais = pais.nombre



    return render_template('adminpersonajes.html',personajes=Personajes,
                           paises=paises,
                           nombrePais=nombrePais)

@rutas_personajes.route('/addpersonaje', methods=['POST'])   
def addpersonaje():
    personaje_dao = Personajes_dao()
    
    nombre = request.form['nombre']
    profesion = request.form['profesion']
    id_pais = request.form['id_pais']

    if (nombre == "" or profesion == "" or id_pais == ""):
        return redirect(url_for('ruta_personaje.verpersonaje'))

    personaje_dao.insert(db,nombre,profesion,id_pais)
  
    return redirect(url_for('ruta_personaje.verpersonaje')) 

@rutas_personajes.route('/delpersonaje', methods=['POST'])   
def delpersonaje():
    id = request.form['id']
    personaje_dao = Personajes_dao()
    personaje_dao.delete(db,id)
    
   
    return redirect(url_for('ruta_personaje.verpersonaje'))  

@rutas_personajes.route('/updatepersonaje', methods=['POST'])   
def updatepersonaje():
    personaje_dao = Personajes_dao()

    id = request.form['id']
    nombre = request.form['nombre']
    profesion = request.form['profesion']

    if (nombre == ""):
        return redirect(url_for('ruta_personaje.verpersonaje'))

    
    personaje_dao.update(db,id,nombre,profesion)
   
    return redirect(url_for('ruta_personaje.verpersonaje'))