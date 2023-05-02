import sys

def test_point_are_showed(client):
    response = client.post('showSummary',data={'email':'john@simplylift.co'})
    print(response.data,file=sys.stderr)
    assert 200 == response.status_code
    assert b'<li>\n            Name: Iron Temple</br>\n            Number of points: 4\n        </li>' in response.data
    assert b'<li>\n            Name: She Lifts</br>\n            Number of points: 12\n        </li>' in response.data
