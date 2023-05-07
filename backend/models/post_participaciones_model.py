from backend.models.post_connection_pool import PostgreSQLPool

class ParticipacionModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_participacion(self, asistencia_codigo):    
        params = {'codigo' : asistencia_codigo}      
        rv = self.post_pool.execute("""SELECT 
       ast.codigo AS codigo,
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
INNER JOIN participaciones par ON ast.codigo = par.asistencia where par.codigo=%(codigo)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = content = {'codigo': result[0],'dni': result[1], 'nombres': result[2], 'apellido_paterno': result[3], 'apellido_materno': result[4], 'cantidad': result[5], 'curso': result[6], 'dia': result[7]}
            data.append(content)
            content = {}
        return data

    def get_participaciones(self):  
        rv = self.post_pool.execute("""SELECT 
       ast.codigo AS codigo,
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
            content = {'codigo': result[0],'dni': result[1], 'nombres': result[2], 'apellido_paterno': result[3], 'apellido_materno': result[4], 'cantidad': result[5], 'curso': result[6], 'dia': result[7]}
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

    def update_participacion(self, codigo, asistencia, cantidad):    
        data = {
            'codigo' : codigo,
            'asistencia' : asistencia,
            'cantidad': cantidad
        }  
        query = """update participaciones set asistencia = %(asistencia)s, cantidad = %(cantidad)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_participacion(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from participaciones where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result