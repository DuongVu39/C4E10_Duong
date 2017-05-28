inventory = {
    'gold'      : 500,
    'pouch'     : ['flint', 'twine', 'gemstone'],
    'backpack'  : ['xylophone', 'dagger', 'bedroll', 'bread loaf'],
    'pocket'    : ['seashell', 'strangeberry', 'lint']
}

inventory['backpack'].sort()
print (inventory['backpack'])
print()
inventory['backpack'].remove('dagger')
print (inventory['backpack'])
print()

inventory['gold'] +=50
print (inventory['gold'])
