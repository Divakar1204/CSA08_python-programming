word = input("Enter the word: ")
normal_order = ''.join(sorted(word))
reverse_order = ''.join(sorted(word, reverse=True))
print("Alphabetical Order Normal:", normal_order)
print("Alphabetical Order Reverse:", reverse_order)


