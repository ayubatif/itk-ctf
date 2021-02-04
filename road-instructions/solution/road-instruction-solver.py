import fileinput
import math


def move(pos, theta, dist):
    return (int(round(pos[0] + dist * math.cos(math.radians(theta)))), int(round(pos[1] + dist * math.sin(math.radians(theta)))))


def solve(str):
    instructions = str.split()
    theta = 90
    
    pos = (0,0)

    for instr in instructions:
        if instr[0] == "R":
            theta -= 90
        else:
            theta += 90
        pos = move(pos, theta, int(instr[1:]))
        
    return (pos[0], pos[1])

for line in fileinput.input():
    print(solve(line))