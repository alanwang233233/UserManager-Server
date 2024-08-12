class UserManager:
    def __init__(self, user_db_controller: type):
        userdb1 = user_db_controller()
        self.user_list = userdb1.list()


class User:
    def __init__(self, *var_args_tuple, **var_args_dict):
        self.data = var_args_tuple
        for key, value in var_args_dict.items():
            if key in dir(self):
                setattr(self, key, value)
