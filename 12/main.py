import string

def main(input_file):
    grid = open(input_file).read().strip().split('\n')
    #print(grid)

    def possible_movement(A,B,going_down=False): # origin, destination, (i,j) coords

        # check if destination is inside grid
        if B[0]<0 or B[0]>=len(grid[0]):
            return False
        if B[1]<0 or B[1]>=len(grid):
            return False

        # check if elevation increase is not too high
        lA,lB = grid[A[1]][A[0]],grid[B[1]][B[0]]

        lA=lA.replace('S','a').replace('E','z')
        lB=lB.replace('S','a').replace('E','z')

        if not going_down:
            return string.ascii_lowercase.index(lA)+1 >= string.ascii_lowercase.index(lB)
        else: # part 2
            return string.ascii_lowercase.index(lB)+1 >= string.ascii_lowercase.index(lA)


    # find starting position
    for j,line in enumerate(grid):
        if 'S' in line:
            i = line.index('S')
            break

    visited = [(i,j)]
    queue = [(i,j)]
    paths = ['S']
    while True:

        i,j = queue.pop(0) # takes first element in the queue
        path = paths.pop(0)
        if path[-1] == 'E':
            break

        for mv in ([(0,1),(0,-1),(1,0),(-1,0)]):
            ib,jb = i+mv[0],j+mv[1]
            if (ib,jb) not in visited:
                if possible_movement((i,j),(ib,jb)):
                    visited.append((ib,jb))
                    queue.append([ib,jb])
                    paths.append(path + grid[jb][ib])

    print(path)
    print("Part 1: ", len(path)-1)


    # For part 2, start at "E" and find quickest to any "a"

    # find starting position
    for j,line in enumerate(grid):
        if 'E' in line:
            i = line.index('E')
            break
    visited = [(i,j)]
    queue = [(i,j)]
    paths = ['E']
    while True:

        i,j = queue.pop(0) # takes first element in the queue
        path = paths.pop(0)
        if path[-1] == 'a':
            break

        for mv in ([(0,1),(0,-1),(1,0),(-1,0)]):
            ib,jb = i+mv[0],j+mv[1]
            if (ib,jb) not in visited:
                if possible_movement((i,j),(ib,jb),going_down=True):
                    visited.append((ib,jb))
                    queue.append([ib,jb])
                    paths.append(path + grid[jb][ib])

    print(path)
    print("Part 2: ", len(path)-1)


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
