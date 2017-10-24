file = open("frame2.txt")
count = 0
for line in file:
    num = line.split(" ")
    count += len(num)
print(count)
