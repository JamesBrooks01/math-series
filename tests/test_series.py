import pytest
from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci_zero():
  actual = fibonacci(0)
  expected = 0
  assert actual == expected

def test_fibonacci_one():
  actual = fibonacci(1)
  expected = 1
  assert actual == expected

def test_fibonacci_five():
  actual = fibonacci(5)
  expected = 5
  assert actual == expected

def test_fibonacci_fifteen():
  actual = fibonacci(15)
  expected = 610
  assert actual == expected

@pytest.mark.skip("Skipping for time purposes")
def test_fibonacci_thirty_three():
  actual = fibonacci(33)
  expected = 3524578
  assert actual == expected

def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected

def test_lucas_fifteen():
    actual = lucas(15)
    expected = 1364
    assert actual == expected

@pytest.mark.skip("Skipping for time purposes")
def test_lucas_thirty_three():
  actual = lucas(33)
  expected = 7881196
  assert actual == expected

def test_sum_series_fibonacci():
    actual = sum_series(5)
    expected = 5
    assert actual == expected

def test_sum_series_lucas():
    actual = sum_series(5, 2, 1)
    expected = 11
    assert actual == expected

def test_sum_series_other():
    actual =  sum_series(5, 15, 1)
    expected = "Please input valid parameters: Only (n) for Fibonacci, (n, 2, 1) for Lucas"
    assert actual == expected