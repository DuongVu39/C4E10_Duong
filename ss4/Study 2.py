<<<<<<< HEAD
def add_fruit(inventory, fruit, quantity=0):  
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return (inventory)
    
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)

print(new_inventory["strawberries"])

add_fruit(new_inventory, "strawberries", 25)

print(new_inventory["strawberries"])
=======
def add_fruit(inventory, fruit, quantity=0):  
    inventory[fruit] = inventory.get(fruit, 0) + quantity
    return (inventory)
    
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)

print(new_inventory["strawberries"])

add_fruit(new_inventory, "strawberries", 25)

print(new_inventory["strawberries"])
>>>>>>> 687005e51286e9522a42a2d33dcef452fb0a05b2
