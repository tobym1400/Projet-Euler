import time

def readNums():
    fo = open("euler13.txt", "r")

    #Read
    nums = []
    for i in range(100):
        nums.append(int(fo.readline()))
    return nums

def sum(nums):
    sum = 0
    for x in nums:
        sum += x
    return sum

tic = time.perf_counter()
print("Number = ",sum(readNums()))
toc = time.perf_counter()
print(f"Total time taken = {toc-tic:0.4f} seconds")