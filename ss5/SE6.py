##s = input("Please enter a string:")

def remove_dollar_sign(s):
    for letter in s:
        if letter == "$":
            s=s.replace(letter,'')
    print(s)
    

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

