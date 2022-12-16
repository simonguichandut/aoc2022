import numpy as np

#p1 = {'A':'rock', 'B':'paper', 'C':'scissors'}
#p2 = {'X':('rock',1), 'B':('paper',2), 'C':('scissors',3)}
p1 = ['A','B','C'] # representing rock,paper,scissors
p2 = ['X','Y','Z']

def main(input_file):
    data = open(input_file).read().strip().split('\n')

    score1,score2 = 0,0
    for hand in data:
        i1,i2 = p1.index(hand[0]), p2.index(hand[-1])

        # part 1
        score1 += i2+1 # 1pt for rock, 2 paper, 3 scissors
        if i1==i2: # draw
            score1 += 3
        elif i2-i1==1 or i2-i1==-2: # win
            score1 += 6

        # part 2
        if i2==0: #lose
            score2 += 0
            score2 += (i1-1)+1 if i1!=0 else 3
        elif i2==1: #draw
            score2 += 3
            score2 += i1+1
        else: # win
            score2 += 6
            score2 += (i1+1)+1 if i1!=2 else 1

    print("Part 1: ", score1)
    print("Part 2: ", score2)


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
