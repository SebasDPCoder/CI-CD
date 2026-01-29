from urllib import response
from fastapi.testclient import TestClient
from mdurl import URL
from main import app

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
    
def test_login_failure():
    URL = "http://127.0.0.1:8000/login"
    payload = {
        "username": "admin",
        "password": "password"
    }
    response = client.post(URL, json=payload)
    assert response.status_code == 200
    assert response.json() == {"message": "Invalid credentials", "status": 401}
    
def test_login_empty_username():     
    URL = "http://127.0.0.1:8000/login"     
    
    payload = {
        "username": "",
        "password": "password123"
        }     
    
    response = client.post(URL, json=payload)     
    assert response.status_code == 422  # Unprocessable Entity due to validation error     
    assert response.json() == {"message": "Invalid credentials", "status": 401}