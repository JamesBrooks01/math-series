def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n -1) + fibonacci(n - 2)

def lucas(n):
        if n == 0:
            return 2
        if n == 1:
            return 1
        return lucas(n -1) + lucas(n - 2)

def sum_series(n, num1 = 0, num2 = 1):
    if num1 == 0 and num2 == 1:
        return fibonacci(n)
    elif num1 == 2 and num2 == 1:
        return lucas(n)
    else:
        return "Please input valid parameters: Only (n) for Fibonacci, (n, 2, 1) for Lucas"
        