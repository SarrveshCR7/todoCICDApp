from app import app

def test_addition():
    with app.test_client() as client:
        response = client.get('/calculate?expression=2%2B2') 
        assert float(response.data.decode()) == 4.0

def test_subtraction():
    with app.test_client() as client:
        response = client.get('/calculate?expression=5-3')
        assert float(response.data.decode()) == 2.0

def test_multiplication():
    with app.test_client() as client:
        response = client.get('/calculate?expression=3*3')
        assert float(response.data.decode()) == 9.0

def test_division():
    with app.test_client() as client:
        response = client.get('/calculate?expression=10/2')
        assert float(response.data.decode()) == 5.0
