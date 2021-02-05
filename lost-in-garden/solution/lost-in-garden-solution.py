import fileinput

start = (-1,-1)
end = (-1, -1)
width = 0
height = 0
maze = [[]]

def addRow(y, row):
    global maze,start,end
    x = 0
    for char in row.strip():
        if char == "#":
            maze[x][y] = True
            print("#", end="")
        else:
            maze[x][y] = False
            print(" ", end="")
        if char == "S":
            start = (x, y)
            maze[x][y] = True
        elif char == "E":
            end = (x, y)
        x += 1
    print()

index = 0
for line in fileinput.input():
    if index == 0:
        width = int(line)
    elif index == 1:
        height = int(line)
        maze = [[False for i in range(height)] for j in range(width)]
    else:
        addRow(index-2, line)
    index += 1

### Maze is built and we have start and end position
path = [start]

debug = False

def walk():
    global path,maze
    pos = path[-1]
    if pos == end:
        return False
    if not (pos[0] == 0 or maze[pos[0] - 1][pos[1]]): # If not been left
        maze[pos[0] - 1][pos[1]] = True
        path.append((pos[0] - 1, pos[1]))
        if debug: print("left")

    elif not (pos[0] == width-1 or maze[pos[0] + 1][pos[1]]): # If not been right
        maze[pos[0] + 1][pos[1]] = True
        path.append((pos[0] + 1, pos[1]))
        if debug: print("right")

    elif not (pos[1] == 0 or maze[pos[0]][pos[1] - 1]): # If not been up
        maze[pos[0]][pos[1] - 1] = True
        path.append((pos[0], pos[1] - 1))
        if debug: print("up")

    elif not (pos[1] == height-1 or maze[pos[0]][pos[1] + 1]): # If not been down
        maze[pos[0]][pos[1] + 1] = True
        path.append((pos[0], pos[1] + 1))
        if debug: print("down")

    else: # Dead end
        path.pop()
        if debug: print("pop")

    if len(path) == 0:
        return False
    return True

def toText(dir):
    text = ""
    last = (0,1)
    for i in range(0, len(dir)-1):
        step = (dir[i][0] - dir[i + 1][0], dir[i][1] - dir[i + 1][1])
        turn = step[0]*last[1] - step[1]*last[0]
        if turn == 0:
            text += "F "
        elif turn == 1:
            text += "L "
        elif turn == -1:
            text += "R "
        last = step
    return text

while walk(): pass

print(toText(path))