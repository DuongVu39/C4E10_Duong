import time
clothes = ["T-Shirt", "Sweater", "Jeans"]
print ("|==============================================|")
print ("|Copy: 'C' |Read: 'R' |Update: 'U' |Delete: 'D'|")
print ("|==============================================|")

while True:

    action = input ( "Welcome to our shop, what do you want (C, R, U, D)?")
    action = action.upper()
    if action == "C":
        item = (input("Enter new item:")).title()
        clothes.append(item)
        print ("Our items:",clothes)
    elif action == "R":
        print ("Our items:",clothes)
    elif action == "U":
        position = int(input("Update position:"))
        if position > (len (clothes)-1):
            print ("There's no item number", position)
            print()
            continue
        item = (input("New item:")).title()
        clothes[position-1] = item
        print ("Our items:",clothes)
    else:
        position = int(input("Delete position:"))
        if position > (len (clothes) -1):
            print ("There's no item number", position)
            print()
            continue
        del clothes[position-1]
        print ("Our items:",clothes)
        
    print ()
    time.sleep(3)

