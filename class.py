class User:
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def getUser(self):
        return f'My name is {self.name} and email is {self.email} i am {self.age} '

    def setAge(self):
        self.age += 1


newUser = User("thancee", "Than@gmail.com", 22)

newUser.setAge()
print(newUser.getUser())
