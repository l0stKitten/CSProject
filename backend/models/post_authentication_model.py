from backend.models.post_connection_pool import PostgreSQLPool
from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token
from flask import jsonify
import requests

class AuthModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()
        token = ""

    def login_get_persona(self, persona_dni, persona_pass):    
        params = {'dni' : persona_dni}      
        rv = self.post_pool.execute("SELECT * from personas where dni=%(dni)s", params) 

        rol_al = self.post_pool.execute("SELECT * from alumnos where dni=%(dni)s", params) 
        rol_prof = self.post_pool.execute("SELECT * from profesores where dni=%(dni)s", params)
        rol_admin = self.post_pool.execute("SELECT * from administradores where dni=%(dni)s", params)

        if len(rol_al) != 0:
            rol = 'alumno'
        elif len(rol_prof) != 0:
            rol = 'profesor'
        elif len(rol_admin) != 0:
            rol = 'admin'

        data = []
        content = {}

        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'password': result[6],  'path': result[7],  
                         'vector': result[8], 'rol': rol}
            data.append(content)
            content = {}

        is_pass_correct = check_password_hash(generate_password_hash(data[0]["password"]), persona_pass)

        if is_pass_correct:
            #refresh = create_refresh_token(identity=data[0]["rol"])
            access = create_access_token(identity=data[0]["dni"])
            self.token = create_access_token(identity=data[0]["dni"])
            print(self.token)
            res = [{
                'access': access,
                'dni': data[0]["dni"],
                'rol': data[0]["rol"]
            }]

            return res
        
        return {'error': 'Wrong credentials'}
    
    def dec_token(token):
        decoded_token = decode_token(token)
        return decoded_token

"""if __name__ == "__main__":    
    pm = PersonaModel()     
    print(pm.create_persona('71218699', 'Rebeca', 'del Río', 'Santos', '12/14/1982', 'rdelrios@universidad.edu.pe', '12345')) """

