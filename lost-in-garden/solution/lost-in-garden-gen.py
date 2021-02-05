import random

class Cell:
    up = False
    left = False
    visited = False

width = int(input("(output = width*2+1) width: "))
height = int(input("(output = height*2+1) height: "))

maze = [[Cell() for y in range(height)] for x in range(width)]
start = (width//2, height-1)
path = [start]
maze[start[0]][start[1]].visited = True

debug = False

def walk(dir):
    global maze, path
    pos = path[-1]
    
    if dir == "up" and not (pos[1] == 0 or maze[pos[0]][pos[1]-1].visited):
        maze[pos[0]][pos[1]].up = True # open path up
        pos = (pos[0], pos[1]-1)
        maze[pos[0]][pos[1]].visited = True
        path.append(pos)
        if debug: print("up")
        return True
    if dir == "down" and not (pos[1] == height-1 or maze[pos[0]][pos[1]+1].visited):
        pos = (pos[0], pos[1]+1)
        maze[pos[0]][pos[1]].up = True # open path up
        maze[pos[0]][pos[1]].visited = True
        path.append(pos)
        if debug: print("down")
        return True
    if dir == "left" and not (pos[0] == 0 or maze[pos[0]-1][pos[1]].visited):
        maze[pos[0]][pos[1]].left = True # open path left
        pos = (pos[0]-1, pos[1])
        maze[pos[0]][pos[1]].visited = True
        path.append(pos)
        if debug: print("left")
        return True
    if dir == "right" and not (pos[0] == width-1 or maze[pos[0]+1][pos[1]].visited):
        pos = (pos[0]+1, pos[1])
        maze[pos[0]][pos[1]].left = True # open path left
        maze[pos[0]][pos[1]].visited = True
        path.append(pos)
        if debug: print("right")
        return True

    return False

def decide():
    directions = ["up", "down", "left", "right"]
    random.shuffle(directions)

    atStart = path[-1] == start

    walked = False
    while directions and not walked:
        walked = walk(directions.pop())

    if not walked:
        if atStart and path[-1] == start:
            return False
        else:
            path.pop()
            if debug: print("pop")

    return True

while decide(): pass

print(width*2 + 1)
print(height*2 + 1)
for y in range(height):
    for x in range(width):
        if not maze[x][y].up:
            if x == start[0] and y == 0: print("#E", end="") # closed
            else: print("##", end="")
        else: print("# ", end="")                 # open
    print("#")
    for x in range(width):
        if not maze[x][y].left: print("# ", end="")
        else: print("  ", end="")
    print("#")
for x in range(width):
    if x == start[0]: print("#S", end="")
    else: print("##", end="")
print("#")