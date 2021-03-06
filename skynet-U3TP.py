from math import sqrt
from random import randint
from viajero import optimizarViaje,generate_mendoza
from time import *
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
            return (best,[])
    (n1Best,sol1)=optimizarTareas(aplicaciones[1:],c,a,M,best)
    c+=aplicaciones[0][2]
    if(c>M):
        if(n1Best>best):
            return (n1Best,sol1.insert(0,False))
        else:
            return(best,[])
    a+=aplicaciones[0][1]
    (n2Best,sol2)=optimizarTareas(aplicaciones[1:],c,a,M,n1Best)
    if(n2Best>n1Best):
        sol2.insert(0,True)
        return (n2Best,sol2)
    elif(n1Best>best):
        sol1.insert(0,False)
        return (n1Best,sol1)
    else:
        return (best,[])
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
    while( i<len(aplicaciones) and (c+aplicaciones[i][2])<M):
        c+=aplicaciones[i][2]
        uti+=aplicaciones[i][1]
        i+=1
    print("Se mantuvieron las siguientes aplicaciones:")
    for n in range(len(aplicaciones)):
        if(n==i):
            print("Se cerraron las siguientes aplicaciones:")
        print(aplicaciones[n][0])
    print("El consumo actual es menor a ",M," y la utilidad es de ",uti)
def terminators(costos):
    destruidas=1
    primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
    for n in range(len(costos)):
        mini=0
        while(destruidas%primos[mini]==0):
            mini+=1
        min=costos[n][mini]
        for i in range(0,len(costos)):
            if(min>costos[n][i] and destruidas%primos[i]!=0):#si el costo es menor a el ultimo minimo encontrado y la ciudad aún no tiene un terminator asignado la guardo como posible objetivo
                min=costos[n][i]
                mini=i
        print("El T800-",n," destruira la ciudad ",mini)
        destruidas*=primos[mini]
    print("pero es mas eficiente si se dan las siguientes combinaciones: 0-2, 1-3, 2-1, 3-4, 4-0")


while(True):
    print("MENU PRINCIPAL")
    print("1-TEST DE CONTRASENA")
    print("2-CONFIGURAR TOLERANCIA DE CONTRASENA")
    print("3-DESPERTADOR!!")
    print("4-OPTIMIZAR USO DE BATERIA")
    print("5-DESTRUIR EL MUNDO")
    print("6-ASESINAR AL LIDER")
    respuesta=input("Ingrese que opcion quiere utilizar:")
    if(respuesta=='1'):
        longitud=int(input("Ingrese longitud de su contrasena:"))
        caracteres=int(input("Ingrese cantidad de caracteres posibles:"))
        milisPD=time()
        posibilidades=fuerzaBrutaPD(caracteres,longitud)
        milisPD=(time()-milisPD)*1000000
        milisDV=time()
        posibilidades=fuerzaBrutaDyV(caracteres,longitud)
        milisDV=(time()-milisDV)*1000000
        print("Un ataque por fuerza Bruta tendra exito en menos de",posibilidades*1.3,"segundos")
        print("Divide y venceras demoro",milisDV,"microsegundos mientras que Programacion dinamica demoro",milisPD,"microsegundos")
    elif(respuesta=='2'):
        contra=input("Ingrese contrasena:")
        tolerancia=int(input("Ingrese tolerancia:"))
        valido=False
        while(not valido):
            valido=(distLevenshtein(contra,input("Ingrese contrasena:"))<tolerancia)
            if(not valido):
                print("Incorrecto")
        print("Correcto")
    elif(respuesta=='3'):
        despierto=False
        while(not despierto):
            if(randint(0,1)==0):
                num1=randint(1,2000)
                num2=randint(1,2000)
                print("Ingrese la fraccion simplificada de",num1,"/",num2,":")
                respuesta=input()
                div=maximoComunDivisor(num1,num2)
                num1/=div
                num2/=div
                nums=respuesta.split('/')
                if(len(nums)==2 and num1==int(nums[0]) and num2==int(nums[1])):
                    print("Estas despierto!")
                    despierto=True
            else:
                num=randint(1,2000)
                print(num,"es primo?(S/N):")
                respuesta=input()
                primo=esPrimo(num)
                if(( primo and respuesta=='S') or (not primo and respuesta=='N')):
                    print("Estas despierto")
                    despierto=True

    elif(respuesta=='4'):
        aplicaciones=[["App1",randint(1,10),randint(0,100)],["App2",randint(1,10),randint(0,100)],["App3",randint(1,10),randint(0,100)],["App4",randint(1,10),randint(0,100)],["App5",randint(1,10),randint(0,100)],["App6",randint(1,10),randint(0,100)],["App7",randint(1,10),randint(0,100)],["App8",randint(1,10),randint(0,100)],["App9",randint(1,10),randint(0,100)],["App10",randint(1,10),randint(0,100)]]
        consumo=int(input("Ingrese el consumo maximo:"))
        print("Programacion dinamica y Backtracking")
        milisPD=time()
        gestorDeTareas(aplicaciones,consumo)
        milisPD=(time()-milisPD)*1000000
        print("Demoro",milisPD,"microsegundos")
        aplicaciones=[["App1",randint(1,10),randint(0,100)],["App2",randint(1,10),randint(0,100)],["App3",randint(1,10),randint(0,100)],["App4",randint(1,10),randint(0,100)],["App5",randint(1,10),randint(0,100)],["App6",randint(1,10),randint(0,100)],["App7",randint(1,10),randint(0,100)],["App8",randint(1,10),randint(0,100)],["App9",randint(1,10),randint(0,100)],["App10",randint(1,10),randint(0,100)]]
        print("Voraz")
        milisV=time()
        gestorDeTareasVoraz(aplicaciones,consumo)
        milisV=(time()-milisV)*1000000
        print("Demoro",milisV,"microsegundos")

    elif(respuesta=='5'):
        mat=[[29, 27, 9, 4, 31],
        [26, 7, 55, 1, 83],
        [85, 1, 88, 1, 17],
        [19, 1, 41, 1, 1],
        [1, 1, 83, 1, 1]]
        terminators(mat)
    elif(respuesta=='6'):
        optimizarViaje(generate_mendoza(5))
    else:
        print("Opcion incorrecta")
