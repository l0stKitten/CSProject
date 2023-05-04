from backend.models.post_connection_pool import PostgreSQLPool

class AdminModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_administrador(self, admin_dni):    
        params = {'dni' : admin_dni}      
        rv = self.post_pool.execute("SELECT p.dni, p.nombres, p.apellido_paterno, p.apellido_materno, p.fecha_nacimiento, p.correo_institucional, a.cargo from personas p inner join administradores a on a.dni = p.dni where a.dni=%(dni)s", params)                
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'cargo': result[6]}
            data.append(content)
            content = {}
        return data

    def get_administradores(self):  
        rv = self.post_pool.execute("SELECT p.dni, p.nombres, p.apellido_paterno, p.apellido_materno, p.fecha_nacimiento, p.correo_institucional, a.cargo from personas p inner join administradores a on a.dni = p.dni")  
        data = []
        content = {}
        for result in rv:
            content = {'dni': result[0], 'nombres': result[1], 'apellido_paterno': result[2], 'apellido_materno': result[3], 
                         'fecha_nacimiento': result[4],  'correo_institucional': result[5],  'cargo': result[6]}
            data.append(content)
            content = {}
        return data

    def create_administrador(self, dni, cargo):    
        data = {
            'dni' : dni,
            'cargo': cargo
        }  
        query = """insert into administradores (dni, cargo) values (%(dni)s, %(cargo)s)"""    
        cursor = self.post_pool.execute(query, data, commit=True)  
        return data

    def update_administrador(self, dni, cargo):    
        data = {
            'dni' : dni,
            'cargo': cargo
        }  
         
        query = """update administradores set cargo = %(cargo)s where dni = %(dni)s"""    
        cursor = self.post_pool.execute(query, data, commit=True)

        result = {'result':1} 
        return result

    def delete_administrador(self, dni):    
        params = {'dni' : dni}      

        query = """delete from administradores where dni = %(dni)s"""    
        self.post_pool.execute(query, params, commit=True) 

        result = {'result': 1}
        return result 

