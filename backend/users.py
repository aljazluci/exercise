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

def get_user_by_id(id):
    for user in get_users(len(_users)):
        if id == user["id"]:
            return user
    return None


def get_users(limit=30):
    if not limit:
        limit = 30
    return _users[:limit]
    
    
def update_user(id, name=None, email=None):
    user = get_user_by_id(id)
    if not user:
        return None
    user["name"] = name
    user["email"] = email
    return user


if __name__ == "__main__":
    print(len(_users))
    print("Running users.py")