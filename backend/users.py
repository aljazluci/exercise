_users = [
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
        },
        {
            "id": 6,
            "name": "Christopher Doe",
            "email": "christopher@doe.com"
        },
        {
            "id": 7,
            "name": "Dennis Doe",
            "email": "dennis@doe.com"
        },
        {
            "id": 8,
            "name": "Frank",
            "email": "frank@doe.com"
        },
        {
            "id": 9,
            "name": "Guillermo Doe",
            "email": "guillermo@doe.com"
        },
        {
            "id": 10,
            "name": "Kenny Doe",
            "email": "kenny@doe.com"
        },
        {
            "id": 11,
            "name": "Lis",
            "email": "lis@doe.com"
        },
        {
            "id": 12,
            "name": "Madeline",
            "email": "madeline@doe.com"
        },
        {
            "id": 13,
            "name": "Noah Doe",
            "email": "noah@doe.com"
        },
        {
            "id": 14,
            "name": "Paula Doe",
            "email": "paula@doe.com"
        },
        {
            "id": 15,
            "name": "Patrick Doe",
            "email": "patrick@doe.com"
        },
        {
            "id": 16,
            "name": "Rick",
            "email": "rick@doe.com"
        },
        {
            "id": 17,
            "name": "Samuel",
            "email": "samuel@doe.com"
        },
        {
            "id": 18,
            "name": "Tina Doe",
            "email": "tina@doe.com"
        },
        {
            "id": 19,
            "name": "Tilda Doe",
            "email": "tilda@doe.com"
        },
        {
            "id": 20,
            "name": "Uriela",
            "email": "uriela@doe.com"
        },
        {
            "id": 21,
            "name": "V",
            "email": "charlie@doe.com"
        }
    ]


def get_users():
    return _users
    
    
def update_user(id, name=None, email=None):
    for user in get_users():
        if id == user["id"]:
            if name:
                user["name"] = name
            if email:
                user["email"] = email
            return user
    return None

if __name__ == "__main__":
    print(len(_users))
    print("Running users.py")