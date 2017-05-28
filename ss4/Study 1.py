<<<<<<< HEAD
letter_counts = {}
users_text = input("Please enter a string:").lower()

for letter in users_text:
    letter_counts[letter] = letter_counts.get(letter, 0) +1

letter_items = list (letter_counts.items())
letter_items.sort()

print(*letter_items, sep='\n')
=======
letter_counts = {}
users_text = input("Please enter a string:").lower()

for letter in users_text:
    letter_counts[letter] = letter_counts.get(letter, 0) +1

letter_items = list (letter_counts.items())
letter_items.sort()

print(*letter_items, sep='\n')
>>>>>>> 687005e51286e9522a42a2d33dcef452fb0a05b2
