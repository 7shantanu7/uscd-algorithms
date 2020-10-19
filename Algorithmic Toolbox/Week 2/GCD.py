a,b = map(int,input().split())

#Iterative way:
def itgcd(a,b):
    while(b!=0):
        a, b = b, a%b
    return a

print(itgcd(a,b))

#Recursive way:
def regcd(a, b):
    if(b==0):
        return a
    else:
        return regcd(b,a%b)

print(itgcd(a,b))
