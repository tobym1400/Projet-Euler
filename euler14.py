import time

def collatz():
    maxNumsInChain = 0
    maxChainNum = 0
    for i in range(1,1000000):
        numsInChain = 1
        nextNum = i
        while nextNum != 1:
            nextNum = nextNumInChain(nextNum)
            numsInChain += 1
        if numsInChain > maxNumsInChain:
            maxNumsInChain = numsInChain
            maxChainNum = i
            
    return maxChainNum

def nextNumInChain(i):
    if i%2 == 0:
        return i/2
    else:
        return 3*i + 1

tic = time.perf_counter()
print("Number = ",collatz())
toc = time.perf_counter()
print(f"Total time taken = {toc-tic:0.4f} seconds")