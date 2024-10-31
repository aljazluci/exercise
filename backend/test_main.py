from fastapi.testclient import TestClient

from main import app
import users

client = TestClient(app)


def test_get_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == users.get_users()
    
def test_get_users_limit():
    limit = 20
    response = client.get(
        "/users",
        params={"limit":limit}
    )
    assert response.status_code == 200
    assert len(response.json()) == limit
    
def test_update_user_wrong_id():
    response = client.put(
        "/users/123",
        json={}
        )
    assert response.status_code == 404
    
def test_update_user_empty_body():
    id = 2
    response = client.put(
        "/users/" + str(id),
        json={}
        )
    assert response.status_code == 200
    assert response.json() == users.get_user_by_id(id)
    
def test_update_user_with_body():
    name = "Laszlo Cravensworth"
    email = "laszlo@cravensworth.com"
    id =2
    
    new_user = users.get_user_by_id(id)
    new_user["name"] = name
    new_user["email"] = email
    
    response = client.put(
        "/users/" + str(id),
        json={
            "name": name,
            "email": email
        }
        )
    assert response.status_code == 200
    assert response.json() == new_user