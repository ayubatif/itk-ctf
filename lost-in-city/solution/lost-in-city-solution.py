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
        if char == "s":
            start = (x, y)
            maze[x][y] = True
        elif char == "e":
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


def walk():
    global path,maze
    pos = path[-1]
    if pos == end:
        return
    if not maze[pos[0] - 1][pos[1]]: # If not been left
        maze[pos[0] - 1][pos[1]] = True
        path.append((pos[0] - 1, pos[1]))

    elif not maze[pos[0] + 1][pos[1]]: # If not been right
        maze[pos[0] + 1][pos[1]] = True
        path.append((pos[0] + 1, pos[1]))

    elif not maze[pos[0]][pos[1] - 1]: # If not been up
        maze[pos[0]][pos[1] - 1] = True
        path.append((pos[0], pos[1] - 1))

    elif not maze[pos[0]][pos[1] + 1]: # If not been down
        maze[pos[0]][pos[1] + 1] = True
        path.append((pos[0], pos[1] + 1))

    else: # Dead end
        path.pop()

    if len(path) == 0:
        return
    elif not pos == end:
        walk()

def toText(dir):
    text = ""
    for i in range(0, len(dir)-1):
        step = (dir[i][0] - dir[i + 1][0], dir[i][1] - dir[i + 1][1])
        if step[0] == -1:
            text += "R "
        elif step[0] == 1:
            text += "L "
        elif step[1] == 1:
            text += "U "
        elif step[1] == -1:
            text += "D "
    return text

walk()
print(toText(path))