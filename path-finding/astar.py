# Visualization https://qiao.github.io/PathFinding.js/visual/
# Explanation https://www.geeksforgeeks.org/a-search-algorithm/
import sys
from random import randint
import math

def getTargetMaze(randomPos):
    maze = [
        ['.', '.', 'x', '.', '.', 'x'],
        ['x', '.', '.', 'x', '.', '.'],
        ['x', '.', 'x', '.', '.', 'x'],
        ['.', '.', 'x', 'x', 'x', '.'],
        ['.', 'x', '.', 'x', '.', '.'],
        ['R', '.', '.', '.', '.', '.']]

    maze[randomPos[0]][randomPos[1]] = 'o'

    return maze

def getMazes():
    emptyMaze = [
        ['.', '.', 'x', '.', '.', 'x'],
        ['x', '.', '.', 'x', '.', '.'],
        ['x', '.', 'x', '.', '.', 'x'],
        ['.', '.', 'x', 'x', 'x', '.'],
        ['.', 'x', '.', 'x', '.', '.'],
        ['R', '.', '.', '.', '.', '.']]

    mazesList = []

    for _ in range(20):
        randomPos = (5,0)
        while emptyMaze[randomPos[0]][randomPos[1]] != '.':
            randomPos = (randint(0, 5),randint(0, 5))

        mazesList.append(getTargetMaze(randomPos))

    return mazesList

def findMarks(maze):
    for i,line in enumerate(maze):
        for j,element in enumerate(line):
            if element == 'R':
                init = (i,j)
            elif element == 'o':
                target = (i,j)
    
    return init, target

def manhattanDist(actual, target):
    return  abs(actual[0] - target[0]) + abs(actual[1] - target[1])

def euclideanDist(actual, target):
    return  math.sqrt((actual[0] - target[0]) ** 2 + (actual[1] - target[1]) ** 2)

def printPath(maze, steps):
    count = 0
    aux = []
    for line in maze:
        aux += [''.join(line)]

    for i, j in steps:
        count += 1
        aux[i] = list(aux[i])
        aux[i][j] = str(count)
        aux[i] = ''.join(aux[i])

    print()
    for line in aux:
        print('\t\t\t' + line)
    print()

def astar(maze, init, target, distance, steps,  actual):
    # Set parameters to check overflow
    height = len(maze)
    width = len(maze[0])
    # Register of the next move (always the best)
    bestDist = sys.maxsize
    bestMove = (0,0)
    # Adding the steps
    steps.append(actual)

    if actual == target:
        print('\t\t\t' + str(steps))
        printPath(maze, steps)
        return steps

    # Check right
    if actual[1]+1 < width:
        moveRight = (actual[0],actual[1]+1)
        distRight = distance(moveRight,target)

        if distRight < bestDist:
            bestDist = distRight
            bestMove = moveRight

    # Check left
    if actual[1]-1 >= 0:
        moveLeft = (actual[0],actual[1]-1)
        distLeft = distance(moveLeft,target)

        if distLeft < bestDist:
            bestDist = distLeft
            bestMove = moveLeft

    # Check top
    if actual[0]-1 >= 0:
        moveTop = (actual[0]-1,actual[1])
        distTop = distance(moveTop,target)

        if distTop < bestDist:
            bestDist = distTop
            bestMove = moveTop

    # Check bottom
    if actual[0]+1< height:
        moveTop = (actual[0]+1,actual[1])
        distTop = distance(moveTop,target)

        if distTop < bestDist:
            bestDist = distTop
            bestMove = moveTop

    astar(maze, init, target, distance, steps, bestMove)

if __name__ == "__main__":
    mazesList = getMazes()
    print('- Algorithm A* search')

    for maze in mazesList:
        init, target = findMarks(maze)

        print('\n\t+ Init:', init, 'Target:', target)
        
        print('\t\tManhattan distance:')
        astar(maze[:], init, target, manhattanDist, [], init)

        print('\t\tEuclidean distance:')
        astar(maze[:], init, target, euclideanDist, [], init)
        