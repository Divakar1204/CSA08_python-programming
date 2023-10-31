def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_non_prime_numbers(a, b):
    for num in range(a, b+1):
        if not is_prime(num):
            print(num)

a = int(input("enter the number:"))
b =  int(input("enter the number:"))
print("Non-prime numbers between", a, "and", b, ":")
print_non_prime_numbers(a, b)
