class User:
    def __init__(self, name, fullname, email) -> None:
        self.name = name
        self.fullname = fullname
        self.email = email
    
    def intro(self, guest):
        return 'Hello {}, I am {}. You can contact me at {}'.format(guest, self.fullname, self.email)
    
user = User('sb', 'Some Body', 'sb@gmail.com')
print(user.intro('Guest'))

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].name < user.name:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, name):
        for user in self.users:
            if name == user.name:
                return user
    
    def update(self, user):
        target = self.find(user.name)
        target.fullname = user.fullname
    
    def list_all(self):
        return self.users

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

user_db = UserDatabase()
user_db.insert(biraj)
user_db.insert(jadhesh)
user_db.insert(aakash)


for user in user_db.list_all():
    print(user.fullname)

jadhesh = User('jadhesh', 'Jadhesh Verman', 'jadhesh@example.com')
user_db.update(jadhesh)

for user in user_db.list_all():
    print(user.fullname)

print(user_db.find('jadhesh').email)


