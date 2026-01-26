from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

valid_user = {
    "username": "admin",
    "password": "password123"
}

@app.post("/login")
async def login(user: User):
    if user.username == valid_user["username"] and user.password == valid_user["password"]:
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials", "status": 401}