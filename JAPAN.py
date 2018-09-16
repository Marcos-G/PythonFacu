import copy
def contarFallas(n,arr):
    if(n==27):
        if( count(arr,1)<27):
            return 1
        else:
            return 0
    else:
        con=0
        for i in range(42):
            array=deepcopy(arr)
            j=i
            while(j<42 and array[j]==1):
                j+=1
            if(j<42):
                array[j]=1
            cont+=contarFallas(n+1,array)
print(contarFallas(0,[]))
