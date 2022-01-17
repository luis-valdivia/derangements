
#degree 2 and 3 derangements with bottom ordered

import itertools


def derrangements(numbs):
    leList = []
    for i in range(1, numbs + 1):
        leList.append(i)
    perms = list(itertools.permutations(leList))
    p2 = perms
    c = 0
    for op in range(len(p2)):
        for orderedPair in range(len(perms)):
            t = 1
            for i in range(len(leList)):
                if perms[orderedPair][i] == leList[i]:
                    t = 0
                    break
                elif perms[orderedPair][i] == p2[op][i]:
                    t = 0
                    break
                elif p2[op][i] == leList[i]:
                    t = 0
                    break
            c += t              
    return  c 


def main():
    for x in range(1, 8):
        print(derrangements(x))
    
main()
