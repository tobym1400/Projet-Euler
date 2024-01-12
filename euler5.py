import time

def smallestMultiple():
    tic = time.perf_counter()
    i = 1
    check = [11,12,13,14,15,16,17,18,19,20]
    while True:
        posAnswer = True
        for j in check:
            if (i % j != 0):
                posAnswer = False
                break
        if (posAnswer):
            toc = time.perf_counter()
            print(i)
            print(f"Time taken: {toc-tic:0.4f} seconds")
            quit()
        i = i + 1

smallestMultiple()