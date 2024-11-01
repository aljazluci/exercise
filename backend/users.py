_users = [
        {
            "id": 1,
            "firstName": "John Doe",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "john@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 2,
            "firstName": "Jane Doe",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "jan@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 3,
            "firstName": "Alice",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "alice@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 4,
            "firstName": "Bob",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "bob@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 5,
            "firstName": "Charlie",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "charlie@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 6,
            "firstName": "Lex",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "lex@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 7,
            "firstName": "Eve",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "eve@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 8,
            "firstName": "Andrew",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "andrew@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 9,
            "firstName": "Robert",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "robert@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 10,
            "firstName": "Anniston",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "anniston@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 11,
            "firstName": "Maria",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "maria@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 12,
            "firstName": "Bob",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "bob@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 13,
            "firstName": "Steve",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "steve@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 14,
            "firstName": "Nandor",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "nandor@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 15,
            "firstName": "Jack",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "jack@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 16,
            "firstName": "Jason",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "jason@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 17,
            "firstName": "Bruce",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "bruce@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 18,
            "firstName": "Lana",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "lana@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 19,
            "firstName": "Wednesday",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "wednesday@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 20,
            "firstName": "Boris",
            "lastName": "Doe",
            "age": 30,
            "gender": "male",
            "email": "boris@doe.com",
            "phone": "123-456-7890",
        },
        {
            "id": 21,
            "firstName": "Molly",
            "lastName": "Doe",
            "age": 30,
            "gender": "female",
            "email": "molly@doe.com",
            "phone": "123-456-7890",
        }
    ]

from models import User

def get_user_by_id(id):
    for user in _users:
        if id == user["id"]:
            return user
    return None


def get_users(limit=30):
    if not limit:
        limit = 30
    return _users[:limit]
    
    
def update_user(id, user_data: User):
    user = get_user_by_id(id)
    if not user:
        return None
    
    fields = {
        "firstName": user_data.firstName,
        "lastName": user_data.lastName,
        "age": user_data.age,
        "gender": user_data.gender,
        "email": user_data.email,
        "phone": user_data.phone
    }
    
    for fname, fval in fields.items():
        if fval:
            user[fname] = fval
    
    return user


if __name__ == "__main__":
    print(len(_users))
    print("Running users.py")