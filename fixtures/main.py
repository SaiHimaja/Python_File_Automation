class UserManager:
    def __init__(self):
        self.users={}
    def addUser(self,username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username]=email
        return True
    
    def getUser(self,username):
        return self.users.get(username)
    