import fastapi
import string
from fastapi import FastAPI

app = FastAPI()


@app.get("/get_id/{patent}")
def get_id(patent):
    # Verificar que: 
    
    # Largo de la cadena sea 7.
    # un str de 4 primeros caracteres (A-Z) y luego 3 digitos.
    # chars en mayús.
    
    #Luego de verificar la patente:
    #['A','A','A','A','0','0','0']
    # convert_asciiPosition(list[0]) * 10 ** 6 + list[1] * 10 ** 5 + list[2] * 10 ** 4 + list[3] * 10 ** 3 + list[4] 
    
    exp_count = 6
    id=1
    for value in patent:
        if (exp_count > 2 ):
            id = id + string.ascii_uppercase.index(value) * 10 ** exp_count
        else:
            id = id + int(value) * 10 ** exp_count
        exp_count = exp_count -1
    
    return {patent: id}


@app.get("/get_patent/{id}")
def get_patent(id):
    # if not isinstance(id, (int, str)):
    #     raise ValueError('El identificador debe ser un número entero y no una palabra.')
    # if not isinstance(id, (int, float)):
    #     raise ValueError('El identificador debe ser un número enterosk.')
    # if id < 0:
    #     raise ValueError('El identificador debe ser mayor o igual a cero.')
    # if id > 28886999:
    #     raise ValueError('El identificador debe ser menor o igual a 28.886.999')
    
    
    return id