from app.data.modelo.ciudades import Ciudad

class Ciudades_dao:

    def select_all(self,db,id_paises) -> list[Ciudad]:
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT j.*,e.paises FROM 
            ciudades j inner join paises e on j.id_paises = e.id
            where j.id_paises = %s
            """,[id_paises])
        ciudades_en_db = cursor.fetchall()
        ciudades : list[Ciudad]= list()
        for ciudad_en_db in ciudades_en_db:
            ciudades.append(Ciudad(ciudad_en_db[0], ciudad_en_db[1], ciudad_en_db[2], ciudad_en_db[3]))

        cursor.close()
        return ciudades

    def insert(self,db,ciudades,contenido,id_paises):
        cursor = db.cursor()
        sql = ("INSERT INTO ciudades (ciudades,contenido,id_paises) values (%s,%s,%s) ")
        data = (ciudades,contenido,id_paises)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("DELETE from ciudades where id = %s ")
        data = [id]
        cursor.execute(sql, data)
        db.commit()
        
    def update(self,db,id,ciudades,contenido):
        cursor = db.cursor()
        sql = ("UPDATE ciudades set ciudades = %s, contenido = %s where id = %s ")
        data = (ciudades,contenido,id)
        cursor.execute(sql, data)
        db.commit()