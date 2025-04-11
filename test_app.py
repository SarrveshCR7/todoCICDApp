import pytest
from app import app

def test_addition():
    assert app.calculate("2+2") == "4"

def test_subtraction():
    assert app.calculate("5-3") == "2"
