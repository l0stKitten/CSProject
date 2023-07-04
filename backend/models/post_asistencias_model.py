from backend.models.post_connection_pool import PostgreSQLPool
from backend.models.post_personas_model import PersonaModel
import cv2
import numpy as np
import requests

class AsistenciaModel:
    def __init__(self):        
        self.post_pool = PostgreSQLPool()

    def get_asistencia(self, codigo_asistencia):    
        params = {'codigo' : codigo_asistencia}      
        rv = self.post_pool.execute("""SELECT a.codigo, a.estado, a.fecha_asistencia, CONCAT(p.nombres, ' ', p.apellido_paterno, ' ', p.apellido_materno) as full_name, a3.nombre from asistencias a 
                                        inner join  matriculas m on a.matricula = m.codigo
                                        inner join alumnos a2 on a2.dni = m.alumno
                                        inner join personas p on p.dni = a2.dni
                                        inner join cursos c on c.codigo = m.curso
                                        inner join asignaturas a3 on a3.codigo = c.asignatura
                                        where a.codigo=%(codigo)s""", params)                
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
                                        inner join alumnos a2 on a2.dni = m.alumno
                                        inner join personas p on p.dni = a2.dni
                                        inner join cursos c on c.codigo = m.curso
                                        inner join asignaturas a3 on a3.codigo = c.asignatura""")              
        data = []
        content = {}
        for result in rv:
            content = {'codigo': result[0], 'estado': result[1], 'fecha_asistencia': result[2], 'full_name': result[3], 
                         'nombre': result[4]}
            data.append(content)
            content = {}
        return data

    def create_asistencia(self, path, fecha_asistencia, matricula, dni):    
        #tomar una imagen
        #endpoint_url = "http://127.0.0.1:81/openfaceAPI"
        #f = {"file": open(path, "rb")}
        #vec = requests.post(endpoint_url, files=f) 
        #res = vec.json()
        res = path
        vector1 = res["result"].replace('[', '').replace(']', '').split()
        vector11 = [float(numeric_string) for numeric_string in vector1]
        #print("vector 11 ", vector11)

        #llamamos para obtener el vector del alumno ya guardado
        persona = PersonaModel()
        info = persona.get_persona(dni)
        vec2 = info[0]["vector"]
        vector2 = vec2.replace('[', '').replace(']', '').split()
        vector22 = [float(numeric_string) for numeric_string in vector2]
        #print("vector 22 ",vector22)
        #comparar la imagen con la del guardado
        distancia = np.linalg.norm(np.array(vector11) - np.array(vector22))

        #cambiar el estado
        estado = False
        if distancia < 0.64 :
            estado = True

        data = {
            'estado' : estado,
            'fecha_asistencia' : fecha_asistencia,
            'matricula' : matricula
        }  

        if estado == True:
            query = """insert into asistencias (estado, fecha_asistencia, matricula) values (%(estado)s, %(fecha_asistencia)s, %(matricula)s)"""    
            cursor = self.post_pool.execute(query, data, commit=True)  
            print(data)
        return data

    def update_asistencia(self, codigo_asistencia, estado, fecha_asistencia, matricula):    
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

