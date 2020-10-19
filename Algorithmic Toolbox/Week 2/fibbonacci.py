n = int(input())
first = 0
second = 1
for i in range(0,n):
    print(first)
    first, second = second, (first+second)
        
