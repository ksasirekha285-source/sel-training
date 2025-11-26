import pyreference

@pyreference.fixture()
def greet():
    print("good morning")
    yield
    print("good evening")

def test_login(greet):
     print ("login executing")
def test_signup(greet):
    print("signup execution")
def test_logout(greet):
    print("logout executing")