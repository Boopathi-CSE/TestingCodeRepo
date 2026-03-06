class AuthService:

    def __init__(self):

        self.users = {
            "admin": "admin123",
            "user": "password"
        }

    def login(self, username, password):

        if username not in self.users:
            return False

        if self.users[username] != password:
            return False

        return True