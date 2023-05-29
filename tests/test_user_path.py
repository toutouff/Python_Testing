import sys

from tests.conftest import client_getter


def test_path_login_to_booking():
    client = client_getter()
    summary_pre_book = client.get('/')
    #print(summary_pre_book.data.decode(),file=sys.stderr)
    point_display_asserter(summary_pre_book.data.decode())
    data = {'email': 'fake@fake.fake'}
    bad_login_response = client.post('showSummary', data=data)
    #print(bad_login_response.data.decode(),file=sys.stderr)
    bad_login_asserter(bad_login_response.data.decode())
    data = {'email': 'john@simplylift.co'}
    login_response = client.post('showSummary', data=data)
    #print(login_response.data.decode(),file=sys.stderr)
    login_asserter(login_response.data.decode())
    book = client.get('book/Spring%20Festival/Simply%20Lift')
    #print(book.data.decode(),file=sys.stderr)
    max_place_ui_asserter(book.data.decode())
    data = {'club': 'Simply Lift', 'competition': 'Spring Festival', 'places': '26'}
    summary_post_book = client.post('purchasePlaces', data=data)
    #print(summary_post_book.data.decode(),file=sys.stderr)
    assert_error_TMPB(summary_post_book.data.decode())
    data['places'] = '2'
    summary_post_book = client.post('purchasePlaces', data=data)
    print(summary_post_book.data.decode(),file=sys.stderr)
    assert_booking_and_deduction(summary_post_book.data.decode())
    data['competition']= 'Fall Classic'
    summary_post_book = client.post('purchasePlaces', data=data)
    #print(summary_post_book.data.decode(),file=sys.stderr)
    assert_error_pcb(summary_post_book.data.decode())


def assert_error_pcb(data):  # Past Competition Booking
    assert 'error past competition booking' in data
    assert 'Number of Places: 4'


def login_asserter(data):
    assert 'Welcome, john@simplylift.co' in data
    point_display_asserter(data)


def bad_login_asserter(data):
    assert 'sorry, mail not found' in data


def max_place_ui_asserter(data):
    assert 'max="4"' in data


def assert_error_TMPB(data):  # Too Many Place Booked
    assert 'error too many place booked' in data
    assert 'Points available: 4' in data
    assert 'Number of Places: 16' in data


def assert_booking_and_deduction(data):
    assert 'Great-booking complete!' in data
    assert 'Points available: 2' in data
    assert 'Number of Places: 14' in data


def point_display_asserter(data):
    assert 'Name: Simply Lift' in data
    assert 'Number of points:' in data
    assert 'Name: Iron Temple' in data
    assert 'Number of points:' in data
    assert 'Name: She Lifts' in data
    assert 'Number of points:' in data
