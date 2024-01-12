import time

def sumSquareDiff():
    sumSquares = 0
    for i in range(1,101):
        sumSquares = sumSquares + i**2
    print(sumSquares)
    sum = 0
    for j in range(1,101):
        sum = sum + j
    print(sum)
    squareSum = sum**2
    print(squareSum)
    print(squareSum - sumSquares)

tic = time.perf_counter()
sumSquareDiff()
toc = time.perf_counter()
print(f"Time taken: {toc-tic:0.4f} seconds")