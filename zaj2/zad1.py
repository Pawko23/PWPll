class UserNotFoundError(Exception):
    pass

class WrongPasswordError(Exception):
    pass

class UserAuth:
    def __init__(self, users):
        self.users = users

    def login(self, username, password):
        if username not in self.users:
            raise UserNotFoundError("User does not exist.")
        elif self.users[username] != password:
            raise WrongPasswordError("Password incorrect.")
        else:
            print("Login succesfull!")

auth = UserAuth({"admin": "1234", "user": "abcd"})

try:
    auth.login("admin", "1234") # Sukces
    auth.login("unknown", "pass") # Powinien rzucić UserNotFoundError
    auth.login("user", "wrongpass") # Powinien rzucić WrongPasswordError
except Exception as e:
    print(f"Error: {e}")