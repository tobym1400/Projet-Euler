import time

def adjacentProduct():
    fo = open("euler11.txt", "r")

    #Read
    nums = [ [0]*20 for i in range(20)]
    for i in range(20):
        numbers = fo.readline()
        numbersSplit = numbers.split()
        for j in range(20):
            nums[i][j] = int(numbersSplit[j])

    maxProduct = 1
    #H Options
    for i in range(20):
        for j in range(17):
            product = nums[i][j] * nums[i][j+1] * nums[i][j+2] * nums[i][j+3]
            if product > maxProduct:
                maxProduct = product
    #V Options
    for i in range(17):
        for j in range(20):
            product = nums[i][j] * nums[i+1][j] * nums[i+2][j] * nums[i+3][j]
            if product > maxProduct:
                maxProduct = product
    #D Options
    for i in range(0,17):
        for j in range(0,17):
            product = nums[i][j] * nums[i+1][j+1] * nums[i+2][j+2] * nums[i+3][j+3]
            if product > maxProduct:
                maxProduct = product
    for i in range(0,17):
        for j in range(3,20):
            product = nums[i][j] * nums[i+1][j-1] * nums[i+2][j-2] * nums[i+3][j-3]
            if product > maxProduct:
                maxProduct = product
    
    return maxProduct

tic = time.perf_counter()
print("Max Product =",adjacentProduct())
toc = time.perf_counter()
print(f"Total time taken = {toc-tic:0.4f} seconds")