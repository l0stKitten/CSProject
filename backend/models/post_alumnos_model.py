from backend.models.post_connection_pool import PostgreSQLPool

class AlumnoModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_alumno(self, persona_dni):    
        params = {'dni' : persona_dni}      
        rv = self.post_pool.execute("SELECT p.dni, p.nombres, p.apellido_paterno, p.apellido_materno, p.fecha_nacimiento, p.correo_institucional from personas p inner join alumnos a on a.dni = p.dni where a.dni=%(dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5]}
            data.append(content)
            content = {}
        return data

    def get_alumnos(self):  
        rv = self.post_pool.execute("SELECT p.dni, p.nombres, p.apellido_paterno, p.apellido_materno, p.fecha_nacimiento, p.correo_institucional from personas p inner join alumnos a on a.dni = p.dni ;")  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5]}
            data.append(content)
            content = {}
        return data

    def get_alumnos_curso(self, codigo, fecha):  
        params = {'codig' : codigo, 'fecha': fecha}  
        rv = self.post_pool.execute('''SELECT p.dni, p.nombres, p.apellido_paterno, p.apellido_materno, p.fecha_nacimiento, p.correo_institucional, ass.codigo from personas p 
                                    inner join alumnos a on a.dni = p.dni 
                                    inner join matriculas m on m.alumno = a.dni
                                    inner join cursos cur on cur.codigo = m.curso
                                    inner join asistencias ass on ass.matricula = m.codigo
                                    where cur.codigo=%(codig)s and ass.estado=true and ass.fecha_asistencia=%(fecha)s''', params)  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'asistencia': result[6],  'number': 0}
            data.append(content)
            content = {}
        
        print(data)
        return data

    def create_alumno(self, dni):    
        data = {
            'dni' : dni
        }  
        query = """insert into alumnos (dni) values (%(dni)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)  
        return data

    """def update_alumno(self, dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password):    
        data = {
            'dni' : dni,
            'nombres' : nombres,
            'apellido_paterno': apellido_paterno,
            'apellido_materno': apellido_materno,
            'fecha_nacimiento': fecha_nacimiento,
            'correo_institucional': correo_institucional,
            'password': password
        }  
         
        pm = PersonaModel()
        pm.update_persona(dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password)

        result = {'result':1} 
        return result"""

    def delete_alumno(self, dni):    
        params = {'dni' : dni}      

        query = """delete from alumnos where dni = %(dni)s"""    
        self.post_pool.execute(query, params, commit=True) 

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = PersonaModel()     
    print(pm.create_persona('71218699', 'Rebeca', 'del Río', 'Santos', '12/14/1982', 'rdelrios@universidad.edu.pe', '12345')) """

