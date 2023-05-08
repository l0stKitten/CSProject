from backend.models.post_connection_pool import PostgreSQLPool

class MatriculaModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_matricula(self, matricula_codigo):    
        params = {'codigo' : matricula_codigo}      
        rv = self.post_pool.execute("""SELECT m.codigo, m.alumno, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as fullname, c.asignatura, a.nombre as asig_nombre, m.estado from matriculas m 
                                        inner join personas p on m.alumno = p.dni 
                                        inner join cursos c on c.codigo = m.curso inner 
                                        join asignaturas a on a.codigo = c.asignatura where m.codigo=%(codigo)s""", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'alumno': result[1], 'fullname': result[2], 'asignatura': result[3], 'asig_nombre': result[4], 'estado': result[5]}
            data.append(content)
            content = {}
        return data

    def get_matriculas(self):  
        rv = self.post_pool.execute("""SELECT m.codigo, m.alumno, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as fullname, c.asignatura, a.nombre as asig_nombre, m.estado from matriculas m 
                                        inner join personas p on m.alumno = p.dni 
                                        inner join cursos c on c.codigo = m.curso inner 
                                        join asignaturas a on a.codigo = c.asignatura""")
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'alumno': result[1], 'fullname': result[2], 'asignatura': result[3], 'asig_nombre': result[4], 'estado': result[5]}
            data.append(content)
            content = {}
        return data

    def create_matricula(self, alumno, curso, estado):    
        data = {
            'alumno': alumno,
            'curso': curso,
            'estado': estado
        }  
        query = """insert into matriculas (alumno, curso, estado) 
            values ( %(alumno)s, %(curso)s, %(estado)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)   
        return data

    def update_matricula(self, codigo, alumno, curso, estado):    
        data = {
            'codigo' : codigo,
            'alumno': alumno,
            'curso': curso,
            'estado': estado
        }  
        query = """update matriculas set alumno = %(alumno)s, curso = %(curso)s, estado = %(estado)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_matricula(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from matriculas where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 
