def get_users():
    return [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@doe.com"
        },
        {
            "id": 2,
            "name": "Jane Doe",
            "email": "jan@doe.com"
        },
        {
            "id": 3,
            "name": "Alice",
            "email": "alice@doe.com"
        },
        {
            "id": 4,
            "name": "Bob",
            "email": "bob@doe.com"
        },
        {
            "id": 5,
            "name": "Charlie",
            "email": "charlie@doe.com"
        }
    ]
    
    
def update_user(id, name=None, email=None):
    for user in get_users():
        if id == str(user["id"]):
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return user
    return None

if __name__ == "__main__":
    print("Running users.py")