import time

def prime(n):
    primes=[2]
    sum = 2
    i=3
    while (i < n):
        isPrime = True
        for prime in primes:
            if (i % prime == 0):
                isPrime = False
                break
            if (i < prime**2):
                break
        if (isPrime):
            primes.append(i)
            sum += i
            print(i)
        i += 2
    return sum



tic = time.perf_counter()
print("Sum =",prime(2000000))
toc = time.perf_counter()
print(f"Total time taken: {toc-tic:0.4f} seconds")