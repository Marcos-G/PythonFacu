import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
loteria=[["Fecha","Número 1","Número 2","Número 3","Número 4","Número 5","Número 6"],["05/05/2018",15,19,24,27,42,51],["05/02/2018",1,2,16,27,36,38],["04/28/2018",7,12,13,30,33,38],["04/25/2018",2,5,12,26,31,43],["04/21/2018",17,20,24,28,49,53],["04/18/2018",10,14,27,32,45,49],["04/14/2018",1,2,5,29,35,36],["04/11/2018",4,16,24,35,49,53],["04/07/2018",15,18,28,31,33,51],["04/04/2018",3,11,12,34,40,51],["03/31/2018",8,16,26,27,44,51],["03/28/2018",3,13,15,22,27,38],["03/24/2018",4,6,16,34,38,39],["03/21/2018",6,9,19,37,39,51],["03/17/2018",4,25,26,38,48,49],["03/14/2018",11,15,16,30,31,50],["03/10/2018",5,15,27,32,36,46],["03/07/2018",9,16,25,32,41,44],["03/03/2018",5,14,23,32,42,52],["02/28/2018",1,5,18,39,45,52],["02/24/2018",5,9,32,35,51,54],["02/21/2018",9,15,17,35,39,44],["02/17/2018",10,11,13,22,26,46],["02/14/2018",8,19,22,29,50,52],["02/10/2018",2,3,15,22,34,39],["02/07/2018",4,15,35,40,44,50],["02/03/2018",3,12,24,29,38,50],["01/31/2018",1,12,17,31,34,40],["01/27/2018",6,9,12,17,20,23],["01/24/2018",8,16,34,43,45,53],["01/20/2018",8,12,24,25,47,54],["01/17/2018",9,16,19,33,40,46],["01/13/2018",18,19,34,37,40,49],["01/10/2018",4,5,15,17,28,54],["01/06/2018",10,11,30,32,38,44],["01/03/2018",6,8,21,33,34,47]]

def quick_sort(A, p, f):
    if p < f:
        q = pasada(A, p, f)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, f)
def radixSort(L):
    for p in range(1,10):
        falta=True
        while(falta):
            falta=False
            for e in range(len(L)-1):
                if((L[e]%(10**p))//(10**(p-1))>(L[e+1]%(10**p))//(10**(p-1))):
                    temp=L[e+1]
                    L[e+1]=L[e]
                    L[e]=temp
                    falta=True
def radixSortPalabras(L):
    chars = [" ",",",".","'","-","a","á","b","c","d","e","é","f","g","h","i","í","j","k","l","m","n","o","ó","p","q","r","s","t","u","ú","v","w","x","y","z"]
    dicc={}
    for i in range(len(chars)):
        dicc[chars[i]]=i
    max=0
    for pal in L:
        if(len(pal)>max):
            max=len(pal)
    for pal in L:
        while(len(pal)<max):
            pal.append(" ")
    for p in range(max-1,-1,-1):
        falta=True
        while(falta):
            falta=False
            for e in range(len(L)-1):
                if(dicc[L[e][p]]>dicc[L[e+1][p]]):
                    temp=L[e+1]
                    L[e+1]=L[e]
                    L[e]=temp
                    falta=True
def radixSortAlverre(L):
    for p in range(11,0,-1):
        falta=True
        while(falta):
            falta=False
            for e in range(len(L)-1):
                if((L[e]%(10**p))//(10**(p-1))>(L[e+1]%(10**p))//(10**(p-1))):
                    temp=L[e+1]
                    L[e+1]=L[e]
                    L[e]=temp
                    falta=True
def pasada(L,p,f):
    i=p-1
    r=int((p+f)/2)
    temp=L[f]
    L[f]=L[r]
    L[r]=temp
    for j in range(p,f):
        if(L[j]<=L[f]):
            i+=1
            temp=L[i]
            L[i]=L[j]
            L[j]=temp
    temp=L[i+1]
    L[i+1]=L[f]
    L[f]=temp
    return i+1
numeros=[]
for i in range(1,len(loteria[0])):
    for j in range(1,len(loteria)):
        numeros.append(loteria[j][i])
quick_sort(numeros,0,len(numeros)-1)
masRepetidos=[0,0,0,0,0,0]
repeticiones=[0,0,0,0,0,0]
prev=numeros[0]
rep=0
print(numeros)
for n in numeros:
    if(n!=prev):
        i=0
        while(i<6 and rep<repeticiones[i]):
            i+=1
        masRepetidos.insert(i,prev)
        masRepetidos.pop()
        repeticiones.insert(i,rep)
        repeticiones.pop()
        rep=0

    prev=n
    rep+=1
print("Los numeros que mas salieron fueron:")
print(masRepetidos)
print("Se podría haber implementado sin haber ordenado los valores, quedando en una complejidad de n")
numerosTony=[123,214,345,346,234,4567,435,356,325,56,235,657,234,34577,457623]
Advengers=["viuda negra","caballero negro","she-hulk","bestia","starfox","madame máscara","hulk","visión","ms. marvel","bruja escarlata","torunn","sentry","moonstone","avispa","phil coulson","quicksilver","kate bishop","luke cage","ex nihilo","ojo de halcón","gata infernal","crystal","máquina de guerra","henry peter gyrich","rick jones","wolverine","t´chaka","edwin jarvis","capitán marvel","namor","silverclaw","spider-man","white tiger","carol danvers","viper","espadachín","thor","zabu","iron man","defensor","nick fury","pantera negra","falcon","mantis","monica rambeau","henry pym","capitán britania","hércules","gravitón","sharon carter","venom","wiccan","ant-man","capitán américa","hombre hormiga","hombre maravilla","pepper potts","maria hill"]
radixSort(numerosTony)
print("Al ordenar como Jarvis queda:",numerosTony)
radixSortAlverre(numerosTony)
print("Al ordenar como Tony queda:",numerosTony)
radixSortPalabras(Advengers)
print(Advengers)
