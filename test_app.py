import pytest
from app import app

def test_addition():
    with app.test_client() as client:
        response = client.get('/calculate?expression=2+2')
        assert response.data.decode() == '4'

def test_subtraction():
    with app.test_client() as client:
        response = client.get('/calculate?expression=5-3')
        assert response.data.decode() == '2'
