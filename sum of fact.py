def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
N = 5
sum_factorial_divided = sum(factorial(i) / i for i in range(1, N+1))
print(f"The sum of factorials divided by their respective numbers from 1 to {N} is: {int(sum_factorial_divided)}")
