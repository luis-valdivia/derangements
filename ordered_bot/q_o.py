
#4 degree derangements with bottom ordered

import itertools


def derrangements(numbs):
    leList = []
    for i in range(1, numbs + 1):
        leList.append(i)
    perms = list(itertools.permutations(leList))
    p2 = perms
    p3 = perms
    c = 0
    for tg in range(len(p3)):
        for op in range(len(p2)):
            for orderedPair in range(len(perms)):
                t = 1
                for i in range(len(leList)):
                    if perms[orderedPair][i] == leList[i] == p2[op][i] == p3[tg][i]:
                        t = 0
                        break
                c += t              
    return  c 


def main():
    for x in range(1, 7):
        print(derrangements(x))
    
main()
