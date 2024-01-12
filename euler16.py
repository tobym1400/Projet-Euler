num=32768
for i in range(16,1001):
    num *= 2
numStr = str(num)
sum = 0
for digit in numStr:
    sum += int(digit)
print(sum)