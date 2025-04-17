from app import app

def test_addition():
    with app.test_client() as client:
        response = client.get('/calculate?expression=2%2B2&answer=4')
        assert response.data.decode() == 'Correct'

def test_subtraction():
    with app.test_client() as client:
        response = client.get('/calculate?expression=5-3&answer=2')
        assert response.data.decode() == 'Correct'

def test_multiplication():
    with app.test_client() as client:
        response = client.get('/calculate?expression=3*3&answer=9')
        assert response.data.decode() == 'Correct'

def test_division():
    with app.test_client() as client:
        response = client.get('/calculate?expression=10/2&answer=5.0')
        assert response.data.decode() == 'Correct'

