import time

def prime(n):
    counter = 1 #2 is prime
    primes=[2]
    i=3
    while (counter < n):
        isPrime = True
        for prime in primes:
            if (i % prime == 0):
                isPrime = False
                break
            if (i < prime**2):
                break
        if (isPrime):
            primes.append(i)
            counter += 1
        i += 2
    print(primes)



tic = time.perf_counter()
prime(10001)
toc = time.perf_counter()
print(f"Time taken: {toc-tic:0.4f} seconds")