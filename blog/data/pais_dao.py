from app.data.modelo.paises import Pais

class Pais_dao:

    def select_all(self,db) -> list[Pais]:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM paises')
        paises_en_db = cursor.fetchall()
        pais : list[Pais]= list()
        for pais_en_db in paises_en_db:
            pais.append(Pais(pais_en_db[0], pais_en_db[1]))

        cursor.close()
        return pais
        
    def insert(self,db,paises):
        cursor = db.cursor()
        sql = ("INSERT INTO paises (paises) values (%s) ") 
        data = (paises,)
        cursor.execute(sql,data)
        db.commit()

    def delete(self,db,id):
        cursor = db.cursor()
        sql = ("DELETE FROM paises WHERE id = %s")
        data = (id,)
        cursor.execute(sql, data)
        db.commit()
        
    def update(self,db,id,paises):
        cursor = db.cursor()
        sql = ("UPDATE paises set paises = %s WHERE id = %s ")
        data = (id,paises)
        cursor.execute(sql, data)
        db.commit()    