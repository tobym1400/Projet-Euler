import time
from math import sqrt, floor

def TriNums():
    triNums=[0,1]
    triNumIndex = 1
    numDivisors = NumDivisors(triNums[triNumIndex])
    while numDivisors <= 500:
        triNumIndex += 1
        sum = triNums[triNumIndex-1] + triNumIndex
        triNums.append(sum)
        numDivisors = NumDivisors(sum)
    print(triNums)
    return triNums[triNumIndex]

def NumDivisors(triNum):
    numDivisors = 2
    for i in range(2,floor(sqrt(triNum))):
        if (triNum%i == 0):
            numDivisors += 2
    return numDivisors


tic = time.perf_counter()
print("Number = ",TriNums())
toc = time.perf_counter()
print(f"Total time taken = {toc-tic:0.4f} seconds")