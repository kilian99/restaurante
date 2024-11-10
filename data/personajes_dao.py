from app.data.modelo.personajes import Personajes

class Personajes_dao:

    def select_all(self,db,id_pais) -> list[Personajes]:
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT j.*,e.paises FROM 
            personajes j inner join paises e on j.id_pais = e.id
            where j.id_pais = %s
            """,[id_pais])
        personajes_en_db = cursor.fetchall()
        personajes : list[Personajes]= list()
        for personaje_en_db in personajes_en_db:
            personajes.append(Personajes(personaje_en_db[0], personaje_en_db[1], personaje_en_db[2], personaje_en_db[3]))

        cursor.close()
        return personajes

    def insert(self,db,nombre,profesion,id_pais):
        cursor = db.cursor()
        sql = ("INSERT INTO personajes (nombre,profesion,id_pais) values (%s,%s,%s) ")
        data = (nombre,profesion,id_pais)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("DELETE from personajes where id = %s ")
        data = [id]
        cursor.execute(sql, data)
        db.commit()
        
    def update(self,db,id,nombre,profesion):
        cursor = db.cursor()
        sql = ("UPDATE ciudades set nombre = %s, profesion = %s where id = %s ")
        data = (nombre,profesion,id)
        cursor.execute(sql, data)
        db.commit()