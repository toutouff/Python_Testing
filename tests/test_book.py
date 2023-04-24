import sys
# possible TODO : add encoder so test don't depend on predone mathematics

# TODO : test if point are deduced from club's total
# DONE
def test_point_are_deduced_from_club(client):

    data={
        'club':'Simply Lift',
        'competition':'Spring Festival',
        'places':5
        }
    response = client.post('purchasePlaces',data=data)
    print(response.data)
    assert b'Points available: 8' in response.data
    # expect error more point than club have
    assert 200 == response.status_code



# TODO : test if place are deduced from competition's total# DONE 
def test_places_are_deduced_from_event(client):
    data={
            'club':'Simply Lift',
            'competition':'Spring Festival',
            'places':4
        }
    
    response = client.post('purchasePlaces',data=data)
    print(response.data,file=sys.stderr)
    assert b'Number of Places: 16' in response.data
    assert 200 == response.status_code
