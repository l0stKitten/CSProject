from backend.models.post_connection_pool import PostgreSQLPool
from flask import jsonify
import requests

class PersonaModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_persona(self, persona_dni):    
        params = {'dni' : persona_dni}      
        rv = self.post_pool.execute("SELECT * from personas where dni=%(dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'password': result[6],  'path': result[7],  'vector': result[8]}
            data.append(content)
            content = {}
        return data

    def get_personas(self):  
        rv = self.post_pool.execute("SELECT * from personas")  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'password': result[6]}
            data.append(content)
            content = {}
        return data
    
    def crear_p(self, dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password, path):
        if path is not '':
            dir = "C:/Users/ASUS/Pictures/Personas/{}".format(path)
            print(dir)
            endpoint_url = "http://127.0.0.1:81/openfaceAPI"
            f = {"file": open(r"{}".format(dir), "rb")}
            vec = requests.post(endpoint_url, files=f) 
            res = vec.json()
            data = {
                'dni' : dni,
                'nombres' : nombres,
                'apellido_paterno': apellido_paterno,
                'apellido_materno': apellido_materno,
                'fecha_nacimiento': fecha_nacimiento,
                'correo_institucional': correo_institucional,
                'password': password,
                'path': path,
                'vector': res["result"]
                
            }
            query = """insert into personas (dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password, path, vector) 
            values (%(dni)s, %(nombres)s, %(apellido_paterno)s, %(apellido_materno)s, %(fecha_nacimiento)s, %(correo_institucional)s, %(password)s, %(path)s, %(vector)s)""" 
            cursor = self.post_pool.execute(query, data, commit=True)   
        else:
            data = {
                'dni' : dni,
                'nombres' : nombres,
                'apellido_paterno': apellido_paterno,
                'apellido_materno': apellido_materno,
                'fecha_nacimiento': fecha_nacimiento,
                'correo_institucional': correo_institucional,
                'password': password
                
            }
            query = """insert into personas (dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password) 
                values (%(dni)s, %(nombres)s, %(apellido_paterno)s, %(apellido_materno)s, %(fecha_nacimiento)s, %(correo_institucional)s, %(password)s)""" 
            cursor = self.post_pool.execute(query, data, commit=True)   
 
        return data
    
    def create_persona(self, dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password, path, tipo, cargo, especialidad): 
        data = self.crear_p(dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password, path)

        if tipo == "Alumno":
            endpoint_url = "http://127.0.0.1:5000/alumno"
            r = requests.put(endpoint_url, json={"dni": dni})
            print(r)
        elif tipo == "Administrador":
            endpoint_url = "http://127.0.0.1:5000/administrador"
            r = requests.put(endpoint_url, json={"dni": dni, "cargo": cargo})
            print(r)
        elif tipo == "Profesor":
            endpoint_url = "http://127.0.0.1:5000/profesor"
            r = requests.put(endpoint_url, json={"dni": dni, "especialidad": especialidad})
            print(r)
        return data

    def update_persona(self, dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password, path):    
        endpoint_url = "http://127.0.0.1:81/openfaceAPI"
        f = {"file": open("{}".format(path), "rb")}
        vec = requests.post(endpoint_url, files=f) 
        res = vec.json()
        
        data = {
            'dni' : dni,
            'nombres' : nombres,
            'apellido_paterno': apellido_paterno,
            'apellido_materno': apellido_materno,
            'fecha_nacimiento': fecha_nacimiento,
            'correo_institucional': correo_institucional,
            'password': password,
            'path': path,
            'vector': res["result"]
        }  
        query = """update personas set nombres = %(nombres)s, apellido_paterno = %(apellido_paterno)s,
                    apellido_materno = %(apellido_materno)s, fecha_nacimiento = %(fecha_nacimiento)s,
                    correo_institucional = %(correo_institucional)s, password = %(password)s, path = %(path)s, vector = %(vector)s where dni = %(dni)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_persona(self, dni):    
        params = {'dni' : dni}      
        query = """delete from personas where dni = %(dni)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = PersonaModel()     
    print(pm.create_persona('71218699', 'Rebeca', 'del Río', 'Santos', '12/14/1982', 'rdelrios@universidad.edu.pe', '12345')) """

