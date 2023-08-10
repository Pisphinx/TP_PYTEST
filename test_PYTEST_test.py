import pytest

def calculate_discount(price, discount_percentage):
    if price <= 0 or discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Invalid input values")
    discount_amount = (discount_percentage / 100) * price
    discounted_price = price - discount_amount
    return discounted_price


def test_dsicount_0():
    assert calculate_discount(20,50) == 10
    assert calculate_discount(200,50) == 100
    assert calculate_discount(100,76) == 24

def test_discount_1():
    assert calculate_discount(20,0) == 20
    assert calculate_discount(200,0) == 200

def test_discount_2():
    assert calculate_discount(20,100) == 0
    assert calculate_discount(200000,100) == 0

def test_discount_error():
    with pytest.raises(ValueError,match="Invalid input values"):
        calculate_discount(-10,1)
    with pytest.raises(ValueError,match="Invalid input value"):
        calculate_discount(-20,1)
    with pytest.raises(ValueError,match="Invalid input values"):
        calculate_discount(10,-1)

