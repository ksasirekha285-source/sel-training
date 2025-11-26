@pytest.fixture(scope='module')
def setup()
    print("good morning")
    yield
    print("good evening")

def test_signup(setup):
    print("signup executing")
def test_logout():
    print("logout executing")

class TestSample:
    def test_login(selfself,setup):
        print("logout execution")

