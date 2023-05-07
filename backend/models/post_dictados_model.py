from backend.models.post_connection_pool import PostgreSQLPool

class DictadoModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_dictado(self, dictado_codigo):    
        params = {'codigo' : dictado_codigo}      
        rv = self.post_pool.execute("select d.codigo, c.codigo as curso, s.codigo as salon, d.tema from dictados d inner join cursos c ON d.curso = c.codigo inner join salones s ON d.salon = s.codigo; where codigo=%(codigo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'curso': result[1], 'salon': result[2], 'tema': result[3]}
            data.append(content)
            content = {}
        return data

    def get_dictados(self):  
        rv = self.post_pool.execute("select d.codigo, c.codigo as curso, s.codigo as salon, d.tema from dictados d inner join cursos c ON d.curso = c.codigo inner join salones s ON d.salon = s.codigo;")  
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'curso': result[1], 'salon': result[2], 'tema': result[3]}
            data.append(content)
            content = {}
        return data

    def create_dictado(self, codigo, curso, salon, tema):  
        data = {
            'curso': curso,
            'salon': salon,
            'tema': tema
        }  
        query = """insert into dictados (dictado, salon, tema) 
            values ( %(dictado)s, %(salon)s, %(tema)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)   
        return data

    def update_dictado(self, codigo, curso, salon, tema):    
        data = {
            'codigo' : codigo,
            'curso': curso,
            'salon': salon,
            'tema': tema
        }  
        query = """update dictados set curso = %(curso)s, salon = %(salon)s, tema = %(tema)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_dictado(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from dictados where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 