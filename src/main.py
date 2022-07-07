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
    id= int(id)
    var_id=id
    # Max combinations in the first char.
    max=17576000
    patent=''
    #region CHARS
    for i in range(0,4):
        temp = int(var_id/max)
        if (var_id % max) == 0:
            temp-=1
        var_id = var_id - max * temp
        max/=26
        patent+=(string.ascii_uppercase[temp])
    #endregion

    #region NUMS
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
    patent += nums
    #endregion
    return {id: patent}
