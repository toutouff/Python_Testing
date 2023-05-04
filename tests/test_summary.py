import sys

def test_point_are_showed(client):
    response = client.post('showSummary',data={'email':'john@simplylift.co'})
    print(response.data,file=sys.stderr)
    assert 200 == response.status_code
    assert 'Name: Iron Temple' in response.data.decode()
    assert 'Number of points:' in response.data.decode()
    assert 'Name: She Lifts' in response.data.decode()


def test_past_competion_unbookable(client):
    response = client.post('showSummary',data={'email':'john@simplylift.co'})
    print(response.data.decode())

