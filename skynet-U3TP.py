from math import sqrt
from random import randint
def fuerzaBrutaDyV(caracteres,longitud):
    n1=1
    n2=1
    for n in range(longitud+1,caracteres+1):
        n1*=n
    for n in range(1,caracteres-longitud+1):
        n2*=n
    return (n1/n2)
def fuerzaBrutaPD(caracteres,longitud):
    cache=[0]*(longitud+1)
    for c in range(caracteres+1):
        for n in range(min(c,longitud),max(-1,c+longitud-caracteres-1),-1):
            if(c==n or n==0):
                cache[n]=1
            else:
                cache[n]=cache[n]+cache[n-1]
    return cache[longitud]
def distLevenshtein(str1,str2):
    d=dict()
    for i in range(len(str1)+1):
        d[i]=dict()
        d[i][0]=i
        for i in range(len(str2)+1):
            d[0][i] = i
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            d[i][j] = min(d[i][j-1]+1, d[i-1][j]+1, d[i-1][j-1]+(not str1[i-1] == str2[j-1]))
    return d[len(str1)][len(str2)]
def maximoComunDivisor(a,b):
    if(a<b):
        a+=b
        b=a-b
        a-=b
    a%=b
    while(a!=0):
        a+=b
        b=a-b
        a-=b
        a%=b
    return b
primos=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
def esPrimo(a):
    if(a>2000):
        print("algoritmo valido hasta 2000")
    n=1
    sq=sqrt(a)
    i=0
    while(primos[i]<sq):
            n*=primos[i]
            i+=1
    if(maximoComunDivisor(n,a)==1):
        return True
    return False
def gestorDeTareas(aplicaciones,M):#matriz de nx3(nombre,prioridad,consumo)
    falta=True
    while(falta):
        falta=False
        for i in range(len(aplicaciones)-1):
            if(aplicaciones[i][2]<aplicaciones[i+1][2]):
                temp=aplicaciones[i]
                aplicaciones[i]=aplicaciones[i+1]
                aplicaciones[i+1]=temp
                falta=True
    falta=True
    while(falta):
        falta=False
        for i in range(len(aplicaciones)-1):
            if(aplicaciones[i][1]>aplicaciones[i+1][1]):
                temp=aplicaciones[i]
                aplicaciones[i]=aplicaciones[i+1]
                aplicaciones[i+1]=temp
                falta=True
    (best,sol)=optimizarTareas(aplicaciones,0,0,M,0)
    print (aplicaciones)
    print (sol)
    print("Se cerraron las siguientes aplicaciones:")
    for i in range(len(aplicaciones)):
        if(not sol[i]):
            print(aplicaciones[i][0])
    print("Se mantuvieron las siguientes aplicaciones:")
    for i in range(len(aplicaciones)):
        if(sol[i]):
            print(aplicaciones[i][0])
    print("El consumo actual es menor a ",M," y la utilidad es de ",best)

def optimizarTareas(aplicaciones,c,a,M,best):
    if(len(aplicaciones)==0):
        if(a>best):
            return (a,[])
        else:
            return (best,None)
    (n1Best,sol1)=optimizarTareas(aplicaciones[1:],c,a,M,best)
    c+=aplicaciones[0][2]
    if(c>M):
        if(n1Best>best):
            return (n1Best,sol1.insert(0,False))
        else:
            return(best,None)
    a+=aplicaciones[0][1]
    (n2Best,sol2)=optimizarTareas(aplicaciones[1:],c,a,M,n1Best)
    if(n2Best>n1Best):
        sol2.insert(0,True)
        return (n2Best,sol2)
    elif(n1Best>best):
        sol1.insert(0,False)
        return (n1Best,sol1)
    else:
        return (best,None)
def gestorDeTareasVoraz(aplicaciones,M):#matriz de nx3(nombre,prioridad,consumo)
    falta=True
    while(falta):
        falta=False
        for i in range(len(aplicaciones)-1):
            if(aplicaciones[i][2]>aplicaciones[i+1][2]):
                temp=aplicaciones[i]
                aplicaciones[i]=aplicaciones[i+1]
                aplicaciones[i+1]=temp
                falta=True
    uti=0
    c=0
    i=0
    while((c+aplicaciones[i][2])<M):
        c+=aplicaciones[i][2]
        uti+=aplicaciones[i][1]
        i+=1
    print (aplicaciones)
    print("Se mantuvieron las siguientes aplicaciones:")
    for n in range(len(aplicaciones)):
        if(n==i):
            print("Se cerraron las siguientes aplicaciones:")
        print(aplicaciones[n][0])
    print("El consumo actual es menor a ",M," y la utilidad es de ",uti)
def t800(costos):
    destruidas=1
    primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    for n in range(len(costos)):
        mini=0
        while(destruidas%primos[mini]==0):
            mini+=1
        min=costos[n][mini]
        for i in range(0,len(costos)):
            if(min>costos[n][i] and destruidas%primos[i]!=0):
                min=costos[n][i]
                mini=i
        print("El T800-",n," destruira la ciudad ",mini)
        destruidas*=primos[mini]

mat=[[randint(1,100) for i in range(5)] for n in range(5)]
print(mat)
t800(mat)
