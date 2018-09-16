import copy
prog=0
def contarFallas(n,arr):
    global prog
    prog+=1
    if(n==27):
        if( arr.count(1)<27):
            return 1
        else:
            return 0
    else:
        con=0
        for i in range(42):
            array=copy.deepcopy(arr)
            j=i
            while(j<42 and array[j]==1):
                j+=1
            if(j<42):
                array[j]=1
            con+=contarFallas(n+1,array)
        return con
print(contarFallas(0,[0 for i in range(42)]))
