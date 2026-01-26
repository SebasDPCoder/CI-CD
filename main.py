from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient
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
    

client = TestClient(app)

# Test cases
def test_login_success():
    URL = "http://127.0.0.1:8000/login"
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = client.post(URL, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Login successful"}