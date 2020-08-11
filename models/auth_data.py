import os 


def get_user_pass():
    user_name = os.environ["POSTGRES_USER"]
    password = os.environ["POSTGRES_PASSWORD"]
    return user_name, password
