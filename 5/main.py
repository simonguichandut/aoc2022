import numpy as np
import copy

def main(input_file):
    #data = open(input_file).read().strip().split('\n')

    with open(input_file, 'r') as f:

        reading_stacks = True
        stacks_data = []
        Stacks = []

        for line in f:
            #print(line)

            if reading_stacks:
                if '[' in line: # still reading stacks
                    stacks_data.append(line[1::4])

                elif line[:3] == ' 1 ': # at the line numbering the stacks
                    Nstacks = eval(line.split()[-1])

                    # Create the stacks
                    Stacks = [[] for i in range(Nstacks)]
                    for layer in stacks_data[::-1]:
                        for k,character in enumerate(layer):
                            if character != ' ':
                                Stacks[k].append(character)

                    reading_stacks = False
                    next(f)

                    # for part 2
                    #Stacks2 = Stacks.copy()
                    #Stacks2 = list(Stacks)
                    Stacks2 = copy.deepcopy(Stacks) # required because nested lists

            else: # instructions
                digits = [eval(digit) for digit in line.replace('move','').replace('from','').replace('to','').split()]

                for i in range(digits[0]):
                    stack_from = Stacks[digits[1]-1]
                    stack_to = Stacks[digits[2]-1]
                    stack_to.append(stack_from[-1])
                    stack_from.pop()

                # part 2
                ncrates = digits[0]
                stack_from = Stacks2[digits[1]-1]
                stack_to = Stacks2[digits[2]-1]
                stack_to += stack_from[-ncrates:]
                for i in range(ncrates): stack_from.pop()

    print("Part 1: ", ''.join([stack[-1] for stack in Stacks]))
    print("Part 2: ", ''.join([stack[-1] for stack in Stacks2]))


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
