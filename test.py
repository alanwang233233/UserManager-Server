class Test2:
    @staticmethod
    def list():
        return {'userid': {'username': 'test1', 'password': '<PASSWORD>'}}


from UserManagerServer import UserManager, User

usermanager = UserManager(Test2)
