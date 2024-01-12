previous = 1
current = 2
sum = 2
while (current < 4e6) :
    temp = current
    current = current + previous
    previous = temp
    if (current % 2 == 0):
        sum += current
print(sum)
# SUCCESS