import numpy as np

def main(input_file):
    data = open(input_file).read().strip().split('\n')
    elves_calories = [[]]
    count = 0
    for line in data:
        if line=='':
            count+=1
            elves_calories.append([])
        else:
            elves_calories[count].append(eval(line))

    totals = [sum(ec) for ec in elves_calories]

    print('Part 1: ',max(totals))

    sum3 = 0
    for i in range(3):
        sum3+=max(totals)
        totals.remove(max(totals))

    print('Part 2: ',sum3)



# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
