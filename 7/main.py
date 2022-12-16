import numpy as np

class file:
    def __init__(self, name, size, parent_directory):
        self.name = name
        self.size = size
        self.parent_directory = parent_directory

class directory:
    def __init__(self, name, parent_directory=None, children=[]):
        self.name = name
        self.parent_directory = parent_directory
        self.children = children

    def add_something(self, something):
        self.children.append(something)

    def ls(self,indent_level=0):
        for child in self.children:
            print('-'*indent_level+' ', child.name)
            if type(child) is directory:
                child.ls(indent_level=indent_level+4)

    def evaluate_size(self):
        size = 0
        for child in self.children:
            if type(child) is file:
                size += child.size
            elif type(child) is directory:
                size += child.evaluate_size() # recursive here
        return size

    # parse the tree and yield size of dir everytime one is encountered 
    def parse_directories(self):
        #print(self.name)
        yield self.evaluate_size()
        for child in self.children:
            if type(child) is directory:
                yield from child.parse_directories()


def main(input_file):
    data = open(input_file).read().strip().split('\n')

    # parse the commands to build the tree
    # the only command that requires doing something is cd
    Home = directory('/')
    current_dir = Home

    for line in data[1:]: # can skip the first line "cd /"
        #print(line)

        if "$ ls" in line:
            pass # nothing to do

        elif "$ cd" in line:
            cd_name = line.split()[-1]

            if cd_name == '..':
                new_current_dir = current_dir.parent_directory

            else:
                for child in current_dir.children:
                    if child.name == cd_name:
                        if type(child) is not directory:
                            print('problem..')
                        new_current_dir = child
                        break

            del current_dir
            current_dir = new_current_dir

        else: # we are in an "ls" output
            if line.split()[0] == 'dir':
                current_dir.add_something(directory(name=line.split()[1], parent_directory=current_dir, children=[]))
            else:
                current_dir.add_something(file(name=line.split()[1], size=eval(line.split()[0]), parent_directory=current_dir))


    Home.ls()
    print('\n')
    Home.parse_directories()

    all_sizes = [size for size in Home.parse_directories()]
    print("Part 1: ", sum(size for size in all_sizes if size<100000))
    print("Part 2: ", min(size for size in all_sizes if size+70000000-max(all_sizes)>=30000000))


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
