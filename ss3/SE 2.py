
sizes = [5, 7, 300, 90, 24, 50, 75]
print ( "Hello, my name is Duong and these are my sheep sizes:")
print (sizes)
print()
p = sizes.index(max(sizes))
print("Now my biggest sheep has size",max(sizes),". Let's shear it!")
print ()
sizes[p] = 8
print ("After shearing, here is my flock:", sizes)
print ()
    
def increase_size (sizes):
    """ Increase each sheep's size by 50"""
    for (idx, val) in enumerate (sizes):
        sizes[idx] = val + 50
for i in range (3):
    print ("Month", i+1, ":")
    print ("One month has passed, now here is my flock:")
    increase_size (sizes)
    print (sizes)
    if i +1 == 3:
        break
    p = sizes.index(max(sizes))
    print("Now my biggest sheep has size",max(sizes),". Let's shear it!")
    print ()
    sizes[p] = 8
    print ("After shearing, here is my flock:", sizes)
    print ()

s = sum (sizes)
print ("My flock has size in total:", s)
print ("I would get", s, " * $2 = $", s * 2)



