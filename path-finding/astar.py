# Visualization https://qiao.github.io/PathFinding.js/visual/
# Explanation https://www.geeksforgeeks.org/a-search-algorithm/
import sys
from random import randint

def getMazes():
    emptyMaze = [
        [' ', ' ', 'x', ' ', ' ', 'x'],
        ['x', ' ', ' ', 'x', ' ', ' '],
        ['x', ' ', 'x', ' ', ' ', 'x'],
        [' ', ' ', 'x', 'x', 'x', ' '],
        [' ', 'x', ' ', 'x', ' ', ' '],
        ['R', ' ', ' ', ' ', ' ', ' ']]

    mazesList = []

    for _ in range(20):
        randomPos = (5,0)
        while emptyMaze[randomPos[0]][randomPos[1]] != ' ':
            randomPos = (randint(0, 5),randint(0, 5))
        
        auxMaze = emptyMaze
        auxMaze[randomPos[0]][randomPos[1]] = 'o'
        mazesList.append(auxMaze)
        break

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

def astar(maze, init, target, distance, actual):
    # Set parameters to check overflow
    height = len(maze)
    width = len(maze[0])
    # Register of the next move (always the best)
    bestDist = sys.maxsize
    bestMove = (0,0)
    print(actual)
    if actual == target:
        return True

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

    astar(maze, init, target, distance, bestMove)

if __name__ == "__main__":
    mazesList = getMazes()
    maze = mazesList[0]
    init, target = findMarks(maze)
    print('Init:', init, 'Target:', target)
    #astar(maze, init, target, manhattanDist, init)
