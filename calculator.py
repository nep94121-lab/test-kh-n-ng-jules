"""
Calculator Module - Ứng dụng máy tính đơn giản
Dự án test cho Jules Google AI Agent
"""


def add(a, b):
    """Cộng hai số"""
    return a + b


def subtract(a, b):
    """Trừ hai số"""
    return a - b


def multiply(a, b):
    """Nhân hai số - BUG: sai công thức!"""
    return a * b  # 🐛 BUG #1: Đáng lẽ phải là a * b


def divide(a, b):
    """Chia hai số - BUG: không xử lý chia cho 0!"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b  # 🐛 BUG #2: Thiếu kiểm tra b == 0


def power(a, b):
    """Lũy thừa a^b"""
    return a ** b


def average(numbers):
    """Tính trung bình cộng - BUG: sai logic khi list rỗng!"""
    if not numbers:
        raise ValueError("Cannot compute average of empty list")
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)  # 🐛 BUG #3: Crash khi list rỗng (ZeroDivisionError)


def find_max(numbers):
    """Tìm số lớn nhất - BUG: trả về sai khi có số âm!"""
    if not numbers:
        raise ValueError("Cannot find maximum of empty list")
    max_val = float('-inf')  # 🐛 BUG #4: Nên dùng numbers[0] hoặc float('-inf')
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def is_even(n):
    """Kiểm tra số chẵn"""
    return n % 2 == 0


def factorial(n):
    """Tính giai thừa - BUG: không xử lý số âm!"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):  # 🐛 BUG #5: Nếu n < 0 thì range rỗng, trả về 1 (sai)
        result *= i
    return result


def celsius_to_fahrenheit(celsius):
    """Chuyển độ C sang độ F - BUG: sai công thức!"""
    return celsius * 9 / 5 + 32  # 🐛 BUG #6: Phải là + 32, không phải + 30


def fibonacci(n):
    """Tính số Fibonacci thứ n"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def is_palindrome(text):
    """Kiểm tra chuỗi đối xứng - BUG: phân biệt hoa/thường!"""
    return text.lower() == text[::-1].lower()  # 🐛 BUG #7: "Racecar" sẽ trả False (nên lower() trước)


def count_vowels(text):
    """Đếm nguyên âm trong chuỗi"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
