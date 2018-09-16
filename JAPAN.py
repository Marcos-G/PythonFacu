import copy
prog=0

def contarFallas(n,arr,s):
    global prog
    prog+=1
    print(prog)
    if(n==s):
        if( arr.count(1)<s):
            return 1
        else:
            return 0
    else:
        con=0
        for i in range(s):
            array=copy.deepcopy(arr)
            j=i
            while(j<s  and array[j]==1):
                j+=1
            if(j<s):
                array[j]=1
            con+=contarFallas(n+1,array)

        return con
print(contarFallas(0,[0 for i in range(42)]))
