from flask import Flask, Blueprint, render_template, request, redirect, url_for

from app import db
from app.data.ciudad_dao import Ciudades_dao
from app.data.pais_dao import Pais_dao

rutas_ciudades = Blueprint("ruta_ciudad", __name__)

@rutas_ciudades.route('/')
def index():
    return render_template('adminciudades.html')

@rutas_ciudades.route('/verciudad', methods=['POST','GET'])
def verciudad():
    Ciudades = list()
    nombrePais = ""
    pais_dao = Pais_dao()
    paises = pais_dao.select_all(db)

    if (request.method == 'POST'):
        id_paises = request.form['id_paises']
        ciudad_dao = Ciudades_dao()
        Ciudades = ciudad_dao.select_all(db,id_paises)
        for pais in paises:
            
            if (id_paises == int(pais.id)):
               
                nombrePais = pais.nombre



    return render_template('adminciudades.html',ciudades=Ciudades,
                           paises=paises,
                           nombrePais=nombrePais)

@rutas_ciudades.route('/addciudad', methods=['POST'])   
def addciudad():
    ciudad_dao = Ciudades_dao()
    ciudades = request.form['ciudades']
    contenido = request.form['contenido']
    id_paises = request.form['id_paises']

    if (ciudades == "" or contenido == "" or id_paises == ""):
        return redirect(url_for('ruta_ciudad.verciudad'))

    ciudad_dao.insert(db,ciudades,contenido,id_paises)
  
    return redirect(url_for('ruta_ciudad.verciudad')) 

@rutas_ciudades.route('/delciudad', methods=['POST'])   
def delciudad():
    id = request.form['id']
    ciudad_dao = Ciudades_dao()
    ciudad_dao.delete(db,id)
    
   
    return redirect(url_for('ruta_ciudad.verciudad'))  

@rutas_ciudades.route('/updateciudad', methods=['POST'])   
def updateciudad():
    ciudad_dao = Ciudades_dao()

    id = request.form['id']
    ciudades = request.form['ciudades']
    contenido = request.form['contenido']

    if (ciudades == ""):
        return redirect(url_for('ruta_ciudad.verciudad'))

    
    ciudad_dao.update(db,id,ciudades,contenido)
   
    return redirect(url_for('ruta_ciudad.verciudad'))