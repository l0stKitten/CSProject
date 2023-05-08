from backend.models.post_connection_pool import PostgreSQLPool

class ParticipacionModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_participacion(self, asistencia_codigo):    
        params = {'codigo' : asistencia_codigo}      
        rv = self.post_pool.execute("""SELECT 
                                        par.asistencia AS asistencia,
                                        al.dni,
                                        CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as fullname,
                                        asig.nombre as asignatura,
                                        par.cantidad,
                                        ast.fecha_asistencia AS dia
                                                FROM personas p
                                                INNER JOIN alumnos al ON p.dni = al.dni
                                                INNER JOIN matriculas m ON al.dni = m.alumno
                                                INNER JOIN cursos c ON m.curso = c.codigo
                                                INNER JOIN asignaturas asig ON asig.codigo = c.asignatura
                                                INNER JOIN asistencias ast ON m.codigo = ast.matricula
                                                INNER JOIN participaciones par ON ast.codigo = par.asistencia where par.asistencia=%(codigo)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'asistencia': result[0],'dni': result[1], 'fullname': result[2], 'asignatura': result[3], 'cantidad': result[4], 'fecha_asistencia': result[5]}
            data.append(content)
            content = {}
        return data

    def get_participaciones(self):  
        rv = self.post_pool.execute("""SELECT 
                                        par.asistencia AS asistencia,
                                        al.dni,
                                        CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as fullname,
                                        asig.nombre as asignatura,
                                        par.cantidad,
                                        ast.fecha_asistencia AS dia
                                                FROM personas p
                                                INNER JOIN alumnos al ON p.dni = al.dni
                                                INNER JOIN matriculas m ON al.dni = m.alumno
                                                INNER JOIN cursos c ON m.curso = c.codigo
                                                INNER JOIN asignaturas asig ON asig.codigo = c.asignatura
                                                INNER JOIN asistencias ast ON m.codigo = ast.matricula
                                                INNER JOIN participaciones par ON ast.codigo = par.asistencia""")  
        data = []
        content = {}
        for result in rv:
            content = {'asistencia': result[0],'dni': result[1], 'fullname': result[2], 'asignatura': result[3], 'cantidad': result[4], 'fecha_asistencia': result[5]}
            data.append(content)
            content = {}
        return data

    def create_participacion(self, asistencia, cantidad):    
        data = {
            'asistencia' : asistencia,
            'cantidad': cantidad
        }  
        query = """insert into participaciones (asistencia, cantidad) 
            values ( %(asistencia)s, %(cantidad)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)   
        return data

    def update_participacion(self, asistencia, cantidad):    
        data = {
            'asistencia' : asistencia,
            'cantidad': cantidad
        }  
        query = """update participaciones set cantidad = %(cantidad)s where asistencia = %(asistencia)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_participacion(self, asistencia):    
        params = {'asistencia' : asistencia}      
        query = """delete from participaciones where asistencia = %(asistencia)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result