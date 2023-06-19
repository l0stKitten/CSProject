from backend.models.post_connection_pool import PostgreSQLPool

class CursoModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_curso(self, curso_codigo):    
        params = {'codigo' : curso_codigo}      
        rv = self.post_pool.execute("""SELECT c.codigo, c.asignatura, a.nombre as asig_nombre, c.profesor, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as fullname, 
                                            h.hora_inicio, h.hora_fin, h.dia from cursos c 
                                            inner join profesores pr ON c.profesor = pr.dni 
                                            inner join personas p on pr.dni = p.dni 
                                            inner join asignaturas a on a.codigo = c.asignatura 
                                            inner join horarios h on h.codigo = c.horario 
                                            where c.codigo=%(codigo)s""", params)               
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'asignatura': result[1], 'asig_nombre': result[2], 'profesor': result[3], 'fullname': result[4], 'hora_inicio': result[5], 'hora_fin': result[6], 'dia': result[7] }
            data.append(content)
            content = {}
        return data

    def get_cursos(self):  
        rv = self.post_pool.execute("SELECT c.codigo, c.asignatura, a.nombre as asig_nombre, c.profesor, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as fullname,  c.horario from cursos c inner join profesores pr ON c.profesor = pr.dni inner join personas p on pr.dni = p.dni inner join asignaturas a on a.codigo = c.asignatura inner join horarios h on h.codigo = c.horario")  
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'asignatura': result[1], 'asig_nombre': result[2], 'profesor': result[3], 'fullname': result[4], 'horario': result[5]}
            data.append(content)
            content = {}
        return data

    def get_cursos_usuario(self, dni):  
        params = {'dni' : dni}    
        rv = self.post_pool.execute("""SELECT c.codigo, c.asignatura, a.nombre as asig_nombre, c.profesor, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as fullname,  
                                            h.hora_inicio, h.hora_fin, h.dia, m.codigo from cursos c 
                                            inner join profesores pr ON c.profesor = pr.dni 
                                            inner join personas p on pr.dni = p.dni inner join asignaturas a on a.codigo = c.asignatura 
                                            inner join horarios h on h.codigo = c.horario
                                            inner join matriculas m on m.curso = c.codigo
                                            inner join alumnos al on al.dni = m.alumno
                                            where al.dni=%(dni)s""", params)  
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'asignatura': result[1], 'asig_nombre': result[2], 'profesor': result[3], 'fullname': result[4], 'hora_inicio': result[5], 'hora_fin': result[6], 'dia': result[7], 'codigom': result[8] }
            data.append(content)
            content = {}
        return data

    def create_curso(self, asignatura, profesor, horario):  
        data = {
            'asignatura': asignatura,
            'profesor': profesor,
            'horario': horario
        }  
        query = """insert into cursos (asignatura, profesor, horario) 
            values ( %(asignatura)s, %(profesor)s, %(horario)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)   
        return data

    def update_curso(self, codigo, asignatura, profesor, horario):    
        data = {
            'codigo' : codigo,
            'asignatura': asignatura,
            'profesor': profesor,
            'horario': horario
        }  
        query = """update cursos set asignatura = %(asignatura)s, profesor = %(profesor)s, horario = %(horario)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_curso(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from cursos where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 