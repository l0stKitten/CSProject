from backend.models.post_connection_pool import PostgreSQLPool

class HorarioModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_horario(self, horario_codigo):    
        params = {'codigo' : horario_codigo}      
        rv = self.post_pool.execute("SELECT * from horarios where codigo=%(codigo)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'hora_inicio': result[1], 'hora_fin': result[2], 'dia': result[3]}
            data.append(content)
            content = {}
        return data

    def get_horarios(self):  
        rv = self.post_pool.execute("SELECT * from horarios")  
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'hora_inicio': result[1], 'hora_fin': result[2], 'dia': result[3]}
            data.append(content)
            content = {}
        return data

    def create_horario(self, hora_inicio, hora_fin, dia):    
        data = {
            'hora_inicio' : hora_inicio,
            'hora_fin': hora_fin,
            'dia': dia
        }  
        query = """insert into horarios (hora_inicio, hora_fin, dia) 
            values (%(hora_inicio)s, %(hora_fin)s, %(dia)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)   
        return data

    def update_horario(self, codigo, hora_inicio, hora_fin, dia):    
        data = {
            'codigo' : codigo,
            'hora_inicio' : hora_inicio,
            'hora_fin': hora_fin,
            'dia': dia
        }  
        query = """update horarios set hora_inicio = %(hora_inicio)s, hora_fin = %(hora_fin)s,
                    dia = %(dia)s where codigo = %(codigo)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)   

        result = {'result':1} 
        return result

    def delete_horario(self, codigo):    
        params = {'codigo' : codigo}      
        query = """delete from horarios where codigo = %(codigo)s"""    
        self.post_pool.execute(query, params, commit=True)   

        result = {'result': 1}
        return result 

"""if __name__ == "__main__":    
    pm = AsignaturaModel()     
    print(pm.create_asignatura('Construccion de Software', '5', 'Ingenieria de Software')) """

