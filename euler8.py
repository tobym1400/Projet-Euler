import time

def adjacentProduct():
    fo = open("euler8.txt", "r")
    
    posStrs = []
    for i in range(0,1000-13):
        fo.seek(i,0)
        posStr = fo.read(13)
        posStrs.append(posStr)

    #print(len(posStrs)) #987

    strSums = []
    maxSum = 1

    for strs in posStrs:
        sum = 1
        for i in range(13):
            sum *= int(strs[i])
        strSums.append(sum)
        if sum > maxSum:
            maxSum = sum

    #print(len(strSums))
    print(maxSum)

    fo.close()

tic = time.perf_counter()
adjacentProduct()
toc = time.perf_counter()
print(f"Time taken: {toc-tic:0.4f} seconds")