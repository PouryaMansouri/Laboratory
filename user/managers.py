class UserManager():
    CURRENT_USER = None

    def register_user(self, user_type, *args, **kwargs):
        u = user_type(*args, **kwargs)
        return self.create(u)

    def login(self, username, password):
        for u in self.readall():
            if u.username == username and u.password == password:
                self.__class__.CURRENT_USER = u
                return u


