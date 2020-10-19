x, n, L = map(int,input().split())
numrefill = 0
currentrefill = 0
x = [0]*n
def minrefill(x, n , L):    
    while(currentrefill<=n):
        lastrefill = currentrefill
        while(currentrefill<=n and (x[currentrefill+1]-x[lastrefill]<=L)):
            currentrefill+=1
        if currentrefill == lastrefill:
            return -1
        if currentrefill<n:
            numrefill+=1
    return numrefill

minrefill(x,n,L)