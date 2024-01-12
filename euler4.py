def palindrome():
    totalNumPal = 9*10*10

    largestPosPal = 999999

    largestPal=10000

    for i in range (999,100,-1):
        for j in range (999,100,-1):
            posNum = i * j
            posStr = str(posNum)
            if (posNum > 100000 and posStr[0] == posStr[5] and posStr[1] == posStr[4] and posStr[2] == posStr[3]):
                if (posNum > largestPal):
                    largestPal = posNum
    return largestPal
print(palindrome())