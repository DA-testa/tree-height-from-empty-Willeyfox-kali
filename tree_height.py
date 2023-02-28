# python3

import sys
import threading
import numpy

def compute_height(n, parents):
    koks = [[] for i in range(n)]
    sakne = -1
    for i in range (n): 
        parent = parents[i]
        if parent == -1:
            sakne = i
        else:
            koks[parent].append(i)
    # Write this function
    max_height = 0
    lvl = [sakne]
    while lvl:
        max_height = max_height + 1
        lvlup = []
        for nodes in lvl:
            for child in koks[nodes]:
                lvlup.append(child)
        lvl = lvlup
    # Your code here
    return max_height


def main():
    n = input().strip()
    if n == 'I':
        n = int(input())
        parents = list(map(int, input().split()))
        rezult = compute_height(n, parents)
        print(rezult)
    elif n == 'F':
        file = input()
        with open (file, 'r') as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
            rezult = compute_height(n, parents)
            print(rezult)
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
