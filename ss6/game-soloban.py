<<<<<<< HEAD

#pusher
#map
#box
#destination
import time
#set pusher coordinate
#rep: P
pusher ={
    "x":1,
    "y":0
    }

#set box coordinate
#rep: B
boxes = [
        {
            "x": 3,
            "y": 2
        },
        {
            "x": 1,
            "y": 3
        }]
#set destination coordinate
#rep: D
gates = [
        {
            "x": 5,
            "y": 5
        },
        {
            "x": 0,
            "y": 0
        },
        ]


#set map size
size = {
    "x": 6,
    "y": 7
    }

def in_map(x, y, size):
    return 0 <= x < size["x"] and 0<= y < size["y"]


def check_overlap (x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True
    return False

            
def map(pusher, boxes, gates):
    for i in range (size["y"]):
        for j in range (size["x"]):
            if i == pusher["y"] and j == pusher["x"]:
                print (" P ", end = '')
            elif check_overlap(j, i, boxes):
                print (" B ", end = '')
            elif check_overlap(j, i, gates):
                print (" D ", end = '')
            else:
                print (" - ", end = '')
        print()
        
def check_box(pusher,dx,dy,items):
    for item in items:
        if item["x"] == pusher["x"] + dx and item["y"] == pusher["y"] + dy:
            return item
    return None

def move(item, dx, dy):
    item["x"] += dx
    item["y"] += dy
    return item

def check_win(boxes, gates):
    count = 0
    for box in boxes:
        for gate in gates:
            if box == gate:
                count += 1
    return count
        
map(pusher, boxes, gates)

def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":
        dy -=1
        
    elif direction == "A":
        dx -=1
        
    elif direction == "S":
        dy +=1
        
    elif direction == "D":
        dx +=1
    else:
        print("Wrong button, pls enter again:")
        time.sleep(.5
                   )
    return dx, dy

# main GAME_LOOP

while True:  
    direction = input("What's your next move? W/A/S/D").upper()
    # xu ly dau vao
    dx, dy = input_process(direction)
    box_ = check_box(pusher,dx,dy,boxes)
    if box_ is not None:
        if check_overlap (box_["x"]+dx, box_["y"]+dy, boxes):
                print("You can't go there, bro!")
        else:
            if in_map(box_["x"]+dx,box_["y"]+dy,size):
                    box_ = move(box_, dx, dy)
                    pusher = move(pusher, dx, dy)
            else:
                print ("Box will fall out bro")
                time.sleep(0.5)
    elif in_map(pusher["x"] + dx, pusher["y"] + dy, size):
            pusher = move(pusher, dx, dy)

    else:
        print ("You can't go there, bro")
        time.sleep(.5)
    map(pusher, boxes, gates)
    if check_win(boxes, gates) == len(boxes):
        break

print ("You won!")
=======
#pusher
#map
#box
#destination
import time
#set pusher coordinate
#rep: P
pusher_x = 1
pusher_y = 0

#set box coordinate
#rep: B
boxes = [
        {
            "x": 3,
            "y": 2
        },
        {
            "x": 1,
            "y": 3
        }]
#set destination coordinate
#rep: D
gates = [
        {
            "x": 5,
            "y": 5
        },
        {
            "x": 0,
            "y": 0
        },
        ]


#set map size
size_x = 6
size_y = 7

def in_map(x, y, size_x, size_y):
    return 0 <= x < size_x and 0<= y < size_y

def box_in_map(dx, dy, size_x, size_y, items):
    for item in items:
        if not in_map(item["x"]+dx,item["y"]+dy,size_x, size_y):
            return False
    return True


def check_overlap (x, y, items):
    for item in items:
        if x == item["x"] and y == item["y"]:
            return True
    return False

            
def map(pusher_x, pusher_y, boxes, gates):
    for i in range (size_y):
        for j in range (size_x):
            if i == pusher_y and j == pusher_x:
                print (" P ", end = '')
            elif check_overlap(j, i, boxes):
                print (" B ", end = '')
            elif check_overlap(j, i, gates):
                print (" D ", end = '')
            else:
                print (" - ", end = '')
        print()
        
def check_box(pusher_x,pusher_y,dx,dy,items):
    for item in items:
        if item["x"] == pusher_x + dx and item["y"] == pusher_y + dy:
            return True
    return False

##def check_win(boxes, gates):
##    for box, gate in boxes, gates:
##        if box["x"]==gate["x"] and box["y"]==gate["y"]
##            continue
##        else:
##            break
##    return False
        
        
map(pusher_x, pusher_y, boxes, gates)

def input_process(direction):
    dx = 0
    dy = 0
    if direction == "W":
        dy -=1
        
    elif direction == "A":
        dx -=1
        
    elif direction == "S":
        dy +=1
        
    elif direction == "D":
        dx +=1
    else:
        print("Wrong button, pls enter again:")
        time.sleep(.5
                   )
    return dx, dy

# main GAME_LOOP

while True:  
    direction = input("What's your next move? W/A/S/D").upper()
    # xu ly dau vao
    dx, dy = input_process(direction)
    if check_box(pusher_x,pusher_y,dx,dy,boxes):
        if box_in_map(dx,dy,size_x, size_y,boxes):
            for box in boxes:
                if box["x"] - dx == pusher_x and box["y"] - dy == pusher_y:
                    box["x"] += dx
                    box["y"] += dy
                    pusher_x += dx
                    pusher_y += dy
        else:
            print ("Box will fall out bro")
            time.sleep(0.5)
    else:
        if in_map(pusher_x + dx, pusher_y + dy, size_x, size_y):
            pusher_x += dx
            pusher_y += dy

        else:
            print ("You can't go there, bro")
            time.sleep(.5)
    map(pusher_x, pusher_y, boxes, gates)

    if boxes == gates:
        break

print ("You won!")
>>>>>>> 687005e51286e9522a42a2d33dcef452fb0a05b2
