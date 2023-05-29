from tests.conftest import client_getter


def test_valid_email():
    client = client_getter()
    response = client.post('showSummary', data={'email': 'john@simplylift.co'})
    print(response.data)
    assert response.status_code == 200


def test_not_valid_email():
    client = client_getter()
    response = client.post('showSummary', data={'email': "false'email@not_true.test"})
    print(response.data)
    #assert b'sorry, mail not found' in response.data
    assert response.status_code == 200


def test_should_status_ok():
    client = client_getter()
    response = client.get("/")
    print(response)
    assert response.status_code == 200



def test_logout():
    client = client_getter()
    response = client.get('logout')
    assert 'Redirecting' in response.data.decode()
    print(response.data.decode())
