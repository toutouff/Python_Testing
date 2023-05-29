import sys
from tests.conftest import client_getter

def test_booking_13_places():
    client = client_getter()
    response = client.get('book/Spring%20Festival/Simply%20Lift')
    print(response.data.decode())
    assert 'max="12"' in response.data.decode()


def test_point_are_deduced_from_club():
    client = client_getter()
    data = {
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': 5
    }
    response = client.post('purchasePlaces', data=data)
    print(response.data.decode())
    assert b'Points available: 8' in response.data
    # expect error more point than club have
    assert 200 == response.status_code


def test_places_are_deduced_from_event():
    client = client_getter()
    data = {
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': 4
    }

    response = client.post('purchasePlaces', data=data)
    print(response.data.decode())
    assert b'Number of Places: 16' in response.data
    assert 200 == response.status_code

def test_max_has_changed():
    client = client_getter()
    response = client.get('book/Spring%20Festival/Simply%20Lift')
    print(response.data.decode())
    assert 'max="4"' in response.data.decode()



def test_booking_too_many_ticket():
    client = client_getter()
    data = {
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': 55
    }
    response = client.post('purchasePlaces',data=data)
    print(response.data.decode())
    assert 'error too many place booked' in response.data.decode()


def test_non_existent_comp_and_club():
    client = client_getter()
    response = client.get('book/falseCompetition/fakeClub')
    print(response.data.decode())
    assert 'Something went wrong please try again' in response.data.decode()


