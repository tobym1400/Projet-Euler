import time
from math import sqrt, floor

def pythagTrip(n):
    maxNum = floor(sqrt(n))
    for i in range(maxNum):
        for j in range(maxNum):
            if (2*i*(i+j) == 1000):
                a = i**2 - j**2
                b = 2*i*j
                c = i**2 + j**2
                print("a =",a,"and b =",b,"and c =",c)
                print("product =",a*b*c)

    

    return 0
    


tic = time.perf_counter()
pythagTrip(1000)
toc = time.perf_counter()
print(f"Time taken: {toc-tic:0.4f} seconds")