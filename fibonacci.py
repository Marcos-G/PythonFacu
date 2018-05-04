from array import array
from time import time

arr=[0]*10000000
arr[1]=1
def fibDivVen(n):
    return fibRec(n)

def fibRec(n):
    if (n==1):
        return 1
    elif(n==0):
        return 0
    return fibRec(n-1)+fibRec(n-2)
def fibDin(n):
    global arr
    return fibDinRec(n)
def fibDinRec(n):
    global arr
    if (n==0):
        return 0
    if(arr[n]!=0):
        return arr[n]
    print n
    arr[n]=fibDinRec(n-1)+fibDinRec(n-2)
    return arr[n]
inicio=time()
print fibDin(50)
print time()-inicio
inicio=time()
print fibDin(50)
print time()-inicio
inicio=time()
print fibDin(50)
print time()-inicio
inicio=time()
print fibDin(50)
print time()-inicio
