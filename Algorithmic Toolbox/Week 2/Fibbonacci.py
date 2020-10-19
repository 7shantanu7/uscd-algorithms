n = int(input())
first = 0
second = 1
for i in range(0,n):
    print(first)
    next = first + second
    first = second
    second = next

