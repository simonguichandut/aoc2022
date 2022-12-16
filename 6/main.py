import numpy as np

def all_unique_characters(string):
    return len(set(string)) == len(string)

def main(input_file):
    data = open(input_file).read().strip().split('\n')
    buffer = data[0]
    i1=i2=None
    for i in range(4,len(buffer)-1):
        if all_unique_characters(buffer[i-4:i]):
            #break
            if i1==None:
                i1=i

            # 14 unique characters can only happen if there are 4 to begin with
            if all_unique_characters(buffer[i-4:i+10]):
                i2=i+10
                break

    print("Part 1: ",i1)
    print("Part 2: ",i2)


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
