from backend.models.post_connection_pool import PostgreSQLPool

class JustificacionModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_justificacion(self, codigo_justificacion):    
        params = {'codigo' : codigo_justificacion}      
        rv = self.post_pool.execute("""SELECT j.codigo, a.codigo as asis_code, a.fecha_asistencia, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as full_name, j.titulo, j.descripcion from justificaciones j 
                                        inner join asistencias a on j.asistencia = a.codigo 
                                        inner join matriculas m on a.matricula = m.codigo 
                                        inner join alumnos a2 on a2.dni = m.alumno 
                                        inner join personas p on p.dni = a2.dni where j.codigo=%(codigo)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'asis_code': result[1], 'fecha_asistencia': result[2], 'full_name': result[3], 
                         'titulo': result[4],  'descripcion': result[5]}
            data.append(content)
            content = {}
        return data

    def get_justificaciones(self):  
        rv = self.post_pool.execute("""SELECT j.codigo, a.codigo as asis_code, a.fecha_asistencia, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as full_name, j.titulo, j.descripcion from justificaciones j 
                                        inner join asistencias a on j.asistencia = a.codigo 
                                        inner join matriculas m on a.matricula = m.codigo 
                                        inner join alumnos a2 on a2.dni = m.alumno 
                                        inner join personas p on p.dni = a2.dni""")                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'asis_code': result[1], 'fecha_asistencia': result[2], 'full_name': result[3], 
                         'titulo': result[4],  'descripcion': result[5]}
            data.append(content)
            content = {}
        return data

    def create_justificacion(self, asistencia, titulo, descripcion):    
        data = {
            'asistencia' : asistencia,
            'titulo' : titulo,
            'descripcion' : descripcion
        }  
        query = """insert into justificaciones (asistencia, titulo, descripcion) values (%(asistencia)s, %(titulo)s, %(descripcion)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)  
        return data

    def update_justificacion(self, codigo_justificacion, asistencia, titulo, descripcion):    
        data = {
            'codigo' : codigo_justificacion,
            'asistencia' : asistencia,
            'titulo' : titulo,
            'descripcion' : descripcion
        }

        query = """update justificaciones set asistencia = %(asistencia)s, titulo = %(titulo)s,
                    descripcion = %(descripcion)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_justificacion(self, codigo_justificacion):    
        params = {'codigo' : codigo_justificacion}      

        query = """delete from justificaciones where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True) 

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = PersonaModel()     
    print(pm.create_persona('71218699', 'Rebeca', 'del Río', 'Santos', '12/14/1982', 'rdelrios@universidad.edu.pe', '12345')) """

