
#double degree derrangements where bottom deck is ordered

import itertools

def derrangements(numbs):
    leList = []
    for i in range(1, numbs + 1):
        leList.append(i)
    perms = list(itertools.permutations(leList))
    c = 0
    for orderedPair in range(len(perms)):
        t = 1
        for i in range(len(leList)):
            if perms[orderedPair][i] == leList[i]: 
                t = 0
                break
        c += t              
    return  c 


def main():
    for x in range(1, 10):
        print(derrangements(x))
    
main()
