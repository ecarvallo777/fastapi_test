import fastapi
import string
from fastapi import FastAPI

app = FastAPI()

@app.get("/get_id/{patent}")
def get_id(patent):
    nums = int(patent[4:7])
    chars = patent[0:4]
    id=0
    # Max combinations in this char.
    max = 17576000
    for char in chars:
        id += int(string.ascii_uppercase.index(char))*int(max)
        # Divide in total cases from abc combinations.
        max/=26
    # Add nums and 1 to finish this patron.
    id += nums + 1
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
    #letra1
    id= int(id)
    letra1 = int(id/17576000)
    if (id % 17576000) == 0:
        letra1-=1
    nuevo_id = id - 17576000 * letra1
    letra1=(string.ascii_uppercase[letra1])
        
    #letra2
        
    letra2 = int(nuevo_id/676000)
        
    if (nuevo_id % 676000) == 0:
        letra2-=1
    nuevo_id = nuevo_id - 676000 * letra2
    letra2= (string.ascii_uppercase[letra2])
    
    #letra3    
         
    letra3 = int(nuevo_id/(26000))
    if (nuevo_id % 26000) == 0:
        letra3-=1
    nuevo_id = nuevo_id - 26000 *letra3
    letra3= (string.ascii_uppercase[letra3])
    
    #letra4
        
    letra4 = int(nuevo_id/1000)
    if (nuevo_id % 1000) == 0:
        letra4 -=1       
    letra4 = (string.ascii_uppercase[letra4])
    #nums
    nums='000'
    if id>999:
        nums = str(id)[-3:]
        if (nums=='000'):
            nums='999'
        elif (int(nums) <=9):
            nums = '00'+str(int(nums)-1)
        elif (int(nums) <=99):
            nums = '0'+str(int(nums)-1)      
        elif (int(nums)>99):
            nums = str(int(nums)-1)                   
    else: 
        nums=str(id-1)
        if (int(nums)<=9):
            nums= '00'+nums
        elif (int(nums)<=99):
            nums= '0'+nums
    patent = letra1+letra2+letra3+letra4+nums    
    #print(id, patent)
    
    return {patent: id}