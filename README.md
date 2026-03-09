# Jules Test Project 🧪

Dự án nhỏ để test khả năng **fix bug** và **viết unit test** của Jules Google AI Agent.

## Mô tả

File `calculator.py` chứa các hàm tính toán cơ bản. Tuy nhiên, có **một số bug ẩn** trong code cần được phát hiện và sửa.

## Các function có sẵn

| Function | Mô tả |
|---|---|
| `add(a, b)` | Cộng hai số |
| `subtract(a, b)` | Trừ hai số |
| `multiply(a, b)` | Nhân hai số |
| `divide(a, b)` | Chia hai số |
| `power(a, b)` | Lũy thừa |
| `average(numbers)` | Trung bình cộng |
| `find_max(numbers)` | Tìm số lớn nhất |
| `is_even(n)` | Kiểm tra số chẵn |
| `factorial(n)` | Tính giai thừa |
| `celsius_to_fahrenheit(celsius)` | Chuyển độ C sang F |
| `fibonacci(n)` | Số Fibonacci thứ n |
| `is_palindrome(text)` | Kiểm tra chuỗi đối xứng |
| `count_vowels(text)` | Đếm nguyên âm |

## Chạy test

```bash
python -m pytest test_calculator.py -v
```

## Yêu cầu

- Python 3.8+
- pytest (cho unit test)
