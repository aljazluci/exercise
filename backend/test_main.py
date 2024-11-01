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
    id =16
    
    new_user = {
            "id": id,
            "firstName": "Jacky",
            "lastName": "Dines",
            "age": 30,
            "gender": "other",
            "email": "jason@dooooe.com",
            "phone": "123-7890",
        }
    
    response = client.put(
        "/users/" + str(id),
        json=new_user
        )
    assert response.status_code == 200
    assert response.json() == new_user