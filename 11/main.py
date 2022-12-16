import numpy as np
import copy

# debug
#dbg = True
dbg = False

def main(input_file):
    data = open(input_file).read().strip().split('\n')

    # parse input
    Nmonk = len([line for line in data if "Monkey" in line])
    X = { m:[[],lambda x:0,0,0,0] for m in range(Nmonk)}
    N = [0 for _ in range(Nmonk)]

    i = 0 # line number
    m = 0 # monkey count
    while True:
        line = data[i]
        if "Monkey" in line:
            info_lines = data[i+1:i+6]

            # Items
            X[m][0] = [eval(n.replace(',','')) for n in info_lines[0].split()[2:]]

            # Operation
            if "old *" in info_lines[1]:
                if "old * old" in info_lines[1]:
                    X[m][1] = lambda x : x*x
                else:
                    num = int(eval(info_lines[1].split()[-1]))
                    X[m][1] = lambda x,num=num : x * num  # super important to set num=num otherwise the argument will be overwritten next evaluation

            else:
                num = int(eval(info_lines[1].split()[-1]))
                X[m][1] = lambda x,num=num : x + num

            #print("all previous lambdas evaluated on 4")
            #for j in range(m+1):
            #    print(X[j][1](4))
            #print("\n")

            # Divisibility test number
            X[m][2] = eval(info_lines[2].split()[-1])

            # Throw cases
            X[m][3] = eval(info_lines[3].split()[-1])
            X[m][4] = eval(info_lines[4].split()[-1])


            m+=1
        i+=1

        if m==Nmonk: break

    Xcopy = copy.deepcopy(X)

    for k in range(20):
        for m in range(Nmonk):
            items,func,d,ma,mb = X[m]
            N[m] += len(items)

            for item in items:
                val = int(func(item) / 3)
                if val % d == 0:
                    X[ma][0].append(val)
                else:
                    X[mb][0].append(val)
            X[m][0] = []

        if dbg:
            print("After Round ",k+1)
            for m in range(Nmonk):
                print("Monkey %d: "%m,", ".join(str(item) for item in X[m][0]),"\n")

    print("Part 1: ", np.prod(sorted(N)[-2:]))


    # For part 2, we reduce the numbers by keeping the modulo of the product of all factors
    # if mod(x,a1)=0, then mod(mod(x,a1*a2*a3*...), a1)=0 also!
    # e.g. 48 is divisible by 2,3, not 5
    # mod(48,2*3*5)=18 is still divisible by 2,3, not 5

    fac = np.prod([X[m][2] for m in range(Nmonk)])

    X = Xcopy
    N = [0 for _ in range(Nmonk)]
    for k in range(10_000):
        for m in range(Nmonk):
            items,func,d,ma,mb = X[m]
            N[m] += len(items)
            for item in items:
                val = func(item)
                val = val%fac
                if val % d == 0:
                    X[ma][0].append(val)
                else:
                    X[mb][0].append(val)
            X[m][0] = []

        if dbg:
            if (k+1)%100==0:
                print("After Round ",k+1)
                for m in range(Nmonk):
                    print("Monkey %d: "%m,", ".join(str(item) for item in X[m][0]),"\n")

    print("Part 2: ", np.prod(sorted(N)[-2:]))


# command line call : python main.py <input_file>
import sys
if __name__ == "__main__":
    if len(sys.argv)==2:
        input_file = sys.argv[1]
    else:
        input_file = "test_input.txt"
    main(input_file)
