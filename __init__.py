

import mysql.connector

# Conectarse con la base de datos
db = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='informatica.iesquevedo.es',
    port = 3333,
    user ='root', #USUARIO QUE USAMOS NOSOTROS
    password ='1asir', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='kilian'
)


# Importar las rutas
def create_app():
    app = Flask(__name__)
    app.debug = True
    

    

    from .blog.routes import routes_croacia
    from .blog.routes import routes_espana
    from .blog.routes import routes_irlanda
    from .blog.routes import routes_ciudades
    from .blog.routes import routes_paises
    from .blog.routes import routes_personajes
    app.register_blueprint(routes_croacia.rutas_croacia)
    app.register_blueprint(routes_espana.rutas_espana)
    app.register_blueprint(routes_irlanda.rutas_irlanda)
    app.register_blueprint(routes_ciudades.rutas_ciudades)
    app.register_blueprint(routes_paises.rutas_paises)
    app.register_blueprint(routes_personajes.rutas_personajes)
    

    return app