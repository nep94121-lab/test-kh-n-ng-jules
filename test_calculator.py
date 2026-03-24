import pytest
from calculator import (
    add, subtract, multiply, divide, power, average, find_max,
    is_even, factorial, celsius_to_fahrenheit, fibonacci,
    is_palindrome, count_vowels
)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(0, 5) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    assert divide(5, 2) == 2.5
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5
    assert power(-2, 3) == -8

def test_average():
    assert average([1, 2, 3, 4, 5]) == 3
    assert average([10, 20]) == 15
    assert average([-10, 10]) == 0
    with pytest.raises(ValueError, match="Cannot compute average of empty list"):
        average([])

def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-10, -5, -20]) == -5
    assert find_max([0, 0, 0]) == 0
    with pytest.raises(ValueError, match="Cannot find maximum of empty list"):
        find_max([])

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-4) == True

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        factorial(-1)

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert celsius_to_fahrenheit(37) == 98.6

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(-5) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(10) == 55

def test_is_palindrome():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == False # Spaces are not removed
    assert is_palindrome("madam") == True

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("HELLO") == 2
    assert count_vowels("rhythm") == 0
    assert count_vowels("aeiou") == 5
    assert count_vowels("") == 0
