import numpy as np

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def character_score(c):
    if c in alphabet: # lowercase
        return alphabet.index(c)+1
    else: # uppercase
        return alphabet.index(c.lower()) + 27

def str_intersect(s1,s2):
    # assuming there is 1 and only 1 common character
    for c in s1:
        if c in s2:
            return c

def str_intersect_3(s1,s2,s3):
    # assuming there is 1 and only 1 common character
    for c in s1:
        if c in s2 and c in s3:
            return c

def main(input_file):
    data = open(input_file).read().strip().split('\n')

    s = 0
    for line in data:
        middle = int(len(line)/2)
        pack1,pack2 = line[:middle],line[middle:]
        c = str_intersect(pack1,pack2)
        s += character_score(c)

    print("Part 1: ", s)

    s = 0
    for i in range(int(len(data)/3)):
        packs = data[3*i:3*i+3]
        c = str_intersect_3(*packs)
        s += character_score(c)

    print("Part 2: ", s)


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
