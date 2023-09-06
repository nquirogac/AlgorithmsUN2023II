import sys
input = sys.stdin.readline

n = int(input())
list = input().split()

max1 = 0
max2 = 0

for x in list:
    if int(x) > max1:
        max2 = max1
        max1 = int(x)
    elif int(x) > max2:
        max2 = int(x)
print(max1 * max2)