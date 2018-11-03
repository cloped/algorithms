# Visualization https://qiao.github.io/PathFinding.js/visual/
def getMaze():
    # Matrix with m lines and n columns
    coords = input()
    m = int(coords.split()[0])
    n = int(coords.split()[1])
    # Maze matrix 
    maze = []

    for index in range(m):
        line = input()
        aux = []
        for char in line:
            aux.append(char)
        maze.append(aux)

    return maze

def findMarks(maze):
    for i,line in enumerate(maze):
        for j,element in enumerate(line):
            if element == 'R':
                init = (i,j)
            elif element == 'o':
                target = (i,j)
    
    return init, target

if __name__ == "__main__":
    maze = getMaze()
    init, target = findMarks(maze)
    
