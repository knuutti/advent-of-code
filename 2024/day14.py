import numpy as np
import re
from math import prod


def create_christmas_kernel(layers=16):
    width, height = (layers*2)-1, layers+1
    M = np.zeros([height, width])
    M[height-1,(width-1)//2] = 1
    for i in range(height-1):
        M[i,(width-1)//2 - i:(width-1)//2 + i + 1] = 1
    return M

data = open("input_day14.txt").read().splitlines()
N = len(data)
print(len(data))
R = 103
C = 101

robot_info = []
for robot in data:
    stuff = [int(x) for x in re.findall("-?\\d+", robot)]
    robot_info.append(stuff)
#print(robot_info)
tree = create_christmas_kernel(15)
for t in range(2):
    M = np.zeros([R,C])
    for robot in robot_info:
        robot[0] += robot[2]
        robot[1] += robot[3]
        if robot[0] < 0: robot[0] += C
        elif robot[0] > C-1: robot[0] -= C
        if robot[1] < 0: robot[1] += R
        elif robot[1] > R-1: robot[1] -= R
        M[robot[1],robot[0]] = 1
    np.convolve(M,tree)

quadrants = [0,0,0,0]
for robot in robot_info:
    #print(robot[1],robot[0])
    if robot[1] < (R-1)/2 and robot[0] < (C-1)/2:
        quadrants[0] += 1
    elif robot[1] < (R-1)/2 and robot[0] > (C-1)/2:
        quadrants[1] += 1
    elif robot[0] < (C-1)/2 and robot[1] > (R-1)/2:
        quadrants[2] += 1
    elif robot[0] > (C-1)/2 and robot[1] > (R-1)/2:
        quadrants[3] += 1
print(prod(quadrants))