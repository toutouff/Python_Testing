def test_valid_email(client):
    response = client.post('showSummary', data={'email': 'john@simplylift.co'})
    print(response.data)
    assert response.status_code == 200


def test_not_valid_email(client):
    response = client.post('showSummary', data={'email': "false'email@not_true.test"})
    print(response.data)
    #assert b'sorry, mail not found' in response.data
    assert response.status_code == 200


def test_should_status_ok(client):
    response = client.get("/")
    print(response)
    assert response.status_code == 200
