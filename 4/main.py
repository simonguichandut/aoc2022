import numpy as np

def fully_contains(range1,range2):
    if range1[0]<=range2[0] and range1[1]>=range2[1]:
        return True
    elif range1[0]>=range2[0] and range1[1]<=range2[1]:
        return True
    else:
        return False

def any_overlap(range1,range2):
    for n in range(range1[0],range1[1]+1):
        if n in range(range2[0],range2[1]+1):
            return True
    return False


def main(input_file):
    data = open(input_file).read().strip().split('\n')

    s1,s2 = 0,0
    for pair in data:
        r1,r2 = pair.split(',')
        range1 = [eval(x) for x in r1.split('-')]
        range2 = [eval(x) for x in r2.split('-')]
        if fully_contains(range1,range2):
            s1+=1
        if any_overlap(range1,range2):
            s2+=1

    print("Part 1: ", s1)
    print("Part 2: ", s2)


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
