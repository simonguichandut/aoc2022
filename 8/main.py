import numpy as np

def is_visible(treemap,i,j):
    if not False in list(treemap[i,j] > treemap[i,:j]): # left
        return True
    if not False in list(treemap[i,j] > treemap[i,j+1:]): # right
        return True
    if not False in list(treemap[i,j] > treemap[:i,j]): # top
        return True
    if not False in list(treemap[i,j] > treemap[i+1:,j]): # bottom
        return True
    return False

def scenic_score(treemap,i,j):
    score = 1
    height = treemap[i,j]

    for k,h in enumerate(treemap[i,:j][::-1]): # left
        if h>=height:
            break
    score *= k+1

    for k,h in enumerate(treemap[i,j+1:]): # right
        if h>=height:
            break
    score *= k+1

    for k,h in enumerate(treemap[:i,j][::-1]): # top
        if h>=height:
            break
    score *= k+1

    for k,h in enumerate(treemap[i+1:,j]): # bottom
        if h>=height:
            break
    score *= k+1

    #print(i,j,score)
    return score

def main(input_file):
    data = open(input_file).read().strip().split('\n')
    treemap = []
    for row in data:
        treemap.append([eval(x) for x in row])
    treemap = np.array(treemap)

    size = len(treemap[0])
    n_visible = 4*size - 4
    scores = []
    for i in range(1,size-1):
        for j in range(1,size-1):

            if is_visible(treemap,i,j):
                n_visible+=1

            scores.append(scenic_score(treemap,i,j))

    print("Part 1: ", n_visible)
    print("Part 2: ", max(scores))


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
