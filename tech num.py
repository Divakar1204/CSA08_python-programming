def is_tech_number(n):
    num_str = str(n)
    even_count = 0
    odd_count = 0

    for digit in num_str:
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count == odd_count


num = int(input("Enter a number: "))
if is_tech_number(num):
    print(num, "is a Tech number")
else:
    print(num, "is not a Tech number")
