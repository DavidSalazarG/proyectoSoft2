from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello_world():
    return {"message":"Servidor ejecutandose"}

usuarios = [
    {
        'id':1,
        'username':'reinel',
        'password':'quiz'
    },
    {
        'id':2,
        'username':'juan',
        'password':'jose'
    },
    {
        'id':3,
        'username':'chatgpt',
        'password':'version4'
    }
]

@app.get("/user/all/")
def listar_all_users():
    return usuarios

@app.get("/user/unique/{id_usuario}")
def listar_just_one(id_usuario: int):
    #Buscar el usurio en la lista
    for i in usuarios:
        if(i['id'] == id_usuario):
            return i
    return "paila ñero, no está"