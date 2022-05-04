from faker import Faker
from pprint import pprint

fake = Faker()

def getUser():
    return f"{fake.first_name()} {fake.last_name()}"

def getUsers(n):
    return [getUser() for _ in range(n)]

if __name__ == "__main__":
    # user = getUser()
    # pprint(user)
    users = getUsers(5)
    pprint(users)
