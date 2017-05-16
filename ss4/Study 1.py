letter_counts = {}
users_text = input("Please enter a string:").lower()

for letter in users_text:
    letter_counts[letter] = letter_counts.get(letter, 0) +1

letter_items = list (letter_counts.items())
letter_items.sort()

print(*letter_items, sep='\n')
