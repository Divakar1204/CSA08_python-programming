def is_happy_number(n):
    def get_next_number(number):
        result = 0
        while number > 0:
            digit = number % 10
            result += digit ** 2
            number //= 10
        return result

    seen_numbers = set()
    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = get_next_number(n)

    return n == 1

num = int(input("Enter a number: "))
if is_happy_number(num):
    print(num, "is a Happy number")
else:
    print(num, "is not a Happy number")
