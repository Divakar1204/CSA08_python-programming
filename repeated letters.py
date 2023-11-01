word = input("Enter the word: ")
letter_count = {}
repeated_letters = []

for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

for letter, count in letter_count.items():
    if count > 1:
        repeated_letters.append(letter)

print("Number of repeated letters =", len(repeated_letters))
print("Repeated letter =", ' '.join(repeated_letters))
