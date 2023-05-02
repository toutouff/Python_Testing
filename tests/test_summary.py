import sys

def test_point_are_showed(client):
    response = client.post('showSummary',data={'email':'john@simplylift.co'})
    print(response.data,file=sys.stderr)
    assert 200 == response.status_code
    assert b'Name: Iron Temple'
    assert b'Number of points:' in response.data
    assert b'Name: She Lifts'
