def count_negative_numbers(numbers):
    return sum(1 for num in numbers if num < 0)

numbers = [16, -18, 27, -16, 23, -21, 19]
negative_count = count_negative_numbers(numbers)
print("Number of negative numbers in List of elements =", negative_count)
