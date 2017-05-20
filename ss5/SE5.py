def remove_dollar_sign():
    s = input("Please enter a string:")
    for word in s:
        if word == "$":
            s=s.replace(word,'')
            
    print (s)
remove_dollar_sign()
