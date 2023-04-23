from backend.models.post_connection_pool import PostgreSQLPool

class ProfesorModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_profesor(self, persona_dni):    
        params = {'dni' : persona_dni}      
        rv = self.post_pool.execute("SELECT p.dni, p.nombres, p.apellido_paterno, p.apellido_materno, p.fecha_nacimiento, p.correo_institucional, p2.especialidad from personas p inner join profesores p2 on p2.dni = p.dni where dni=%(dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'especialidad': result[6]}
            data.append(content)
            content = {}
        return data

    def get_profesores(self):  
        rv = self.post_pool.execute("SELECT p.dni, p.nombres, p.apellido_paterno, p.apellido_materno, p.fecha_nacimiento, p.correo_institucional, p2.especialidad from personas p inner join profesores p2 on p2.dni = p.dni")  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'especialidad': especialidad[6]}
            data.append(content)
            content = {}
        return data

    def create_profesor(self, dni, especialidad):    
        data = {
            'dni' : dni,
            'especialidad': especialidad
        }  
        query = """insert into profesores (dni, especialidad) values (%(dni)s, %(especialidad)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)  
        return data

    def update_profesor(self, dni, especialidad):    
        data = {
            'dni' : dni,
            'especialidad': especialidad
        }  
         
        query = """update profesores set nombrespecialidades = %(especialidad)s where dni = %(dni)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)

        result = {'result':1} 
        return result

    def delete_alumno(self, dni):    
        params = {'dni' : dni}      

        query = """delete from alumnos where dni = %(dni)s"""    
        self.post_pool.execute(query, params, commit=True) 

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = PersonaModel()     
    print(pm.create_persona('71218699', 'Rebeca', 'del Río', 'Santos', '12/14/1982', 'rdelrios@universidad.edu.pe', '12345')) """

