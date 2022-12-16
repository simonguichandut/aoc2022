import numpy as np

# debug
#dbg = True
dbg = False

def main(input_file):
    data = open(input_file).read().strip().split('\n')

    x = 1
    add = 0
    cycle = 1
    S = 0

    i = 0
    reading = True
    add_now = False

    #message = [['.' for _ in range(40)] for _ in range(6)]
    message = [[' ' for _ in range(40)] for _ in range(6)] # can see better on my terminal
    row = 0

    while True:
        if reading:
            if dbg: print(data[i])
            line = data[i].split()

            if line[0] != 'noop':
                reading = False
                add = int(line[1])

            i += 1
            add_now = False

        else:
            add_now = True # add at the end of this cycle
            reading = True

        # part 1
        if (cycle-20)%40 == 0:
            if dbg: print(cycle,x)
            S+=x*(cycle)

        # part 2
        row,col = (cycle-1)//40, (cycle-1)%40
        if col in (x-1,x,x+1):
            #message[row][col] = '#'
            message[row][col] = '.'

        if add_now:
            x+=add
        cycle += 1

        if reading and i == len(data): break


    print("Part 1: ", S)
    print("Part 2: ")
    for line in message:
        print(' '.join(line))


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
