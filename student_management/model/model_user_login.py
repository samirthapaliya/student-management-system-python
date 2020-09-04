class login:
    def __init__(self, user, password):
        self.__user = user
        self.__password = password

    def set_user(self, user):
        self.__user = user

    def get_user(self):
        return self.__user

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

