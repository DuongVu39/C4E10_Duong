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
