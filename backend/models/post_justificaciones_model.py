from backend.models.post_connection_pool import PostgreSQLPool

class JustificacionModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_justificacion(self, codigo_justificacion):    
        params = {'codigo' : codigo_justificacion}      
        rv = self.post_pool.execute("SELECT j.codigo, a.codigo, a.fecha_asistencia, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno), j.titulo, j.descripcion,  from justificaciones j inner join asistencias a on j.asistencia = a.codigo inner join matriculas m on a.matricula = m.codigo inner join alumno a2 on a2.dni = m.alumno inner join personas p on p.dni = a.dni where j.codigo=%(codigo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5]}
            data.append(content)
            content = {}
        return data

    def get_justificaciones(self):  
        rv = self.post_pool.execute("SELECT p.dni, p.nombres, p.apellido_paterno, p.apellido_materno, p.fecha_nacimiento, p.correo_institucional from personas p inner join alumnos a on a.dni = p.dni ;")  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5]}
            data.append(content)
            content = {}
        return data

    def create_justificacion(self, dni):    
        data = {
            'dni' : dni
        }  
        query = """insert into alumnos (dni) values (%(dni)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)  
        return data

    def update_justificacion(self, dni, nombres, apellido_paterno, apellido_materno, fecha_nacimiento, correo_institucional, password):    
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
        return result

    def delete_justificacion(self, dni):    
        params = {'dni' : dni}      

        query = """delete from alumnos where dni = %(dni)s"""    
        self.post_pool.execute(query, params, commit=True) 

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = PersonaModel()     
    print(pm.create_persona('71218699', 'Rebeca', 'del Río', 'Santos', '12/14/1982', 'rdelrios@universidad.edu.pe', '12345')) """

