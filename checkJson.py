import json


# Sample Json

userJSON = '{"firstname":"John","lastname":"Doe"}'


user = json.loads(userJSON)

print(len(user))


car = {
    "make": "Ford",
    "name": "test"
}

carJSON = json.dumps(car)

print(carJSON)
