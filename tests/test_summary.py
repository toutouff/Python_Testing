import sys
from tests.conftest import client_getter


def test_point_are_showed():
    client = client_getter()
    response = client.post('showSummary',data={'email':'john@simplylift.co'})
    print(response.data,file=sys.stderr)
    assert 200 == response.status_code
    assert 'Name: Iron Temple' in response.data.decode()
    assert 'Number of points:' in response.data.decode()
    assert 'Name: She Lifts' in response.data.decode()
