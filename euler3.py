from math import sqrt 


def prime(n):
    largest = -1
    while n % 2 == 0:
        largest = 2
        n >>= 1 # equivalent to n /= 2
    for i in range(3,int(sqrt(n))+1,2):
        while (n % i == 0):
            largest = i
            n /= i
    if (n > 2):
        largest = n
    return int(largest)
#print(prime(13195))
#print(prime(25698751364526))
print(prime(600851475143))
# SUCCESS
