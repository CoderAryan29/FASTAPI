from fastapi import FastAPI

app = FastAPI()
#home route
@app.get("/")
def home():
    return{"message":"welcome to fastapi man"}

#about route
@app.get("/about")
def about():
    return{"message":"welcome to fastapi about route man"}

#users route
"""@app.get("/users")
def users():
    return{
        "users":["mohit","rohit","sup"]
    }"""

@app.get("/users/{user_id}")
def users(user_id:int):
    return{
        "user_id":user_id
    }