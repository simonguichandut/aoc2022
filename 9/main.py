import numpy as np

# debug
#dbg = True
dbg = False

directions = {'R':(1,0),'L':(-1,0),'U':(0,1),'D':(0,-1)}

def distance(A,B): # Chebyshev distance (A,B are each (x,y) positions)
    return max((abs(A[0]-B[0]),abs(A[1]-B[1])))

def main(input_file):
    data = open(input_file).read().strip().split('\n')

    head,tail = [0,0],[0,0]
    tail_history = set()
    tail_history.add(tuple(tail))

    for line in data:
        d,n = line.split()
        dx,dy = directions[d]

        for _ in range(int(n)):
            head[0]+=dx
            head[1]+=dy

            if distance(head,tail) > 1:
                tail[0] += np.sign(head[0]-tail[0])
                tail[1] += np.sign(head[1]-tail[1])
                tail_history.add(tuple(tail))

    print("Part 1: ", len(tail_history))

    knots = [[0,0] for _ in range(10)] # head to tail
    tail_history = set()
    tail_history.add(tuple(knots[-1]))

    for line in data:
        print(line)
        d,n = line.split()
        dx,dy = directions[d]

        for _ in range(int(n)):
            knots[0][0]+=dx
            knots[0][1]+=dy

            for i in range(1,10):
                while distance(knots[i-1],knots[i]) > 1:
                    knots[i][0] += np.sign(knots[i-1][0]-knots[i][0])
                    knots[i][1] += np.sign(knots[i-1][1]-knots[i][1])
            tail_history.add(tuple(knots[-1]))

        if dbg:
            all_values = tail_history.copy()
            all_values.update([tuple(x) for x in knots])
            size = 2*max([abs(x) for x in np.array(list(all_values)).flatten()]) + 4
            grid_rep = [['.' for i in range(size)] for j in range(size)]
            for p in tail_history:
                grid_rep[int(size/2) - p[1]][int(size/2) + p[0]] = '#'
            for i,p in enumerate(knots):
                grid_rep[int(size/2) - p[1]][int(size/2) + p[0]] = str(i) if i!=0 else 'H'
            for line in grid_rep:
                print(' '.join(line))
    print("Part 2: ", len(tail_history))




# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
