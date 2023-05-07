from backend.models.post_connection_pool import PostgreSQLPool

class AsistenciaModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_asistencia(self, codigo_asistencia):    
        params = {'codigo' : codigo_asistencia}      
        rv = self.post_pool.execute("""SELECT a.codigo, a.estado, a.fecha_asistencia, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as full_name, a3.nombre from asistencias a 
                                        inner join  matriculas m on a.matricula = m.codigo
                                        inner join alumno a2 on a2.dni = m.alumno
                                        inner join personas p on p.dni = a2.dni
                                        inner join cursos c on c.codigo = m.curso
                                        inner join asignaturas a3 on a3.codigo = c.asignatura
                                        where j.codigo=%(codigo)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'estado': result[1], 'fecha_asistencia': result[2], 'full_name': result[3], 
                         'nombre': result[4]}
            data.append(content)
            content = {}
        return data

    def get_asistencias(self):  
        rv = self.post_pool.execute("""SELECT a.codigo, a.estado, a.fecha_asistencia, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as full_name, a3.nombre from asistencias a 
                                        inner join  matriculas m on a.matricula = m.codigo
                                        inner join alumno a2 on a2.dni = m.alumno
                                        inner join personas p on p.dni = a2.dni
                                        inner join cursos c on c.codigo = m.curso
                                        inner join asignaturas a3 on a3.codigo = c.asignatura""", params)              
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'estado': result[1], 'fecha_asistencia': result[2], 'full_name': result[3], 
                         'nombre': result[4]}
            data.append(content)
            content = {}
        return data

    def create_asistencia(self, estado, fecha_asistencia, matricula):    
        data = {
            'estado' : estado,
            'fecha_asistencia' : fecha_asistencia,
            'matricula' : matricula
        }  
        query = """insert into asistencias (estado, fecha_asistencia, matricula) values (%(estado)s, %(fecha_asistencia)s, %(matricula)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)  
        return data

    def update_asistencia(self, codigo_asistencia, asistencia, titulo, descripcion, archivo):    
        data = {
            'codigo' : codigo_asistencia,
            'estado' : estado,
            'fecha_asistencia' : fecha_asistencia,
            'matricula' : matricula
        }

        query = """update asistencias set estado = %(estado)s, fecha_asistencia = %(fecha_asistencia)s,
                    matricula = %(matricula)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_asistencia(self, codigo_asistencia):    
        params = {'codigo' : codigo_asistencia}      

        query = """delete from asistencias where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True) 

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = PersonaModel()     
    print(pm.create_persona('71218699', 'Rebeca', 'del Río', 'Santos', '12/14/1982', 'rdelrios@universidad.edu.pe', '12345')) """

