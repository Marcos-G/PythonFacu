loteria=[["Fecha","Número 1","Número 2","Número 3","Número 4","Número 5","Número 6"],["05/05/2018",15,19,24,27,42,51],["05/02/2018",1,2,16,27,36,38],["04/28/2018",7,12,13,30,33,38],["04/25/2018",2,5,12,26,31,43],["04/21/2018",17,20,24,28,49,53],["04/18/2018",10,14,27,32,45,49],["04/14/2018",1,2,5,29,35,36],["04/11/2018",4,16,24,35,49,53],["04/07/2018",15,18,28,31,33,51],["04/04/2018",3,11,12,34,40,51],["03/31/2018",8,16,26,27,44,51],["03/28/2018",3,13,15,22,27,38],["03/24/2018",4,6,16,34,38,39],["03/21/2018",6,9,19,37,39,51],["03/17/2018",4,25,26,38,48,49],["03/14/2018",11,15,16,30,31,50],["03/10/2018",5,15,27,32,36,46],["03/07/2018",9,16,25,32,41,44],["03/03/2018",5,14,23,32,42,52],["02/28/2018",1,5,18,39,45,52],["02/24/2018",5,9,32,35,51,54],["02/21/2018",9,15,17,35,39,44],["02/17/2018",10,11,13,22,26,46],["02/14/2018",8,19,22,29,50,52],["02/10/2018",2,3,15,22,34,39],["02/07/2018",4,15,35,40,44,50],["02/03/2018",3,12,24,29,38,50],["01/31/2018",1,12,17,31,34,40],["01/27/2018",6,9,12,17,20,23],["01/24/2018",8,16,34,43,45,53],["01/20/2018",8,12,24,25,47,54],["01/17/2018",9,16,19,33,40,46],["01/13/2018",18,19,34,37,40,49],["01/10/2018",4,5,15,17,28,54],["01/06/2018",10,11,30,32,38,44],["01/03/2018",6,8,21,33,34,47]]

def quick_sort(A, p, f):
    if p < f:
        q = pasada(A, p, f)
        quick_sort(A, p, q - 1)
        quick_sort(A, q + 1, f)

def pasada(L,p,f):
    i=p-1
    r=int((p+f)/2)
    L[r]+=L[f]
    L[f]=L[r]-L[f]
    L[r]-=L[f]
    for j in range(p,f):
        if(L[j]<=L[f]):
            i+=1
            L[i]+=L[j]
            L[j]=L[i]-L[j]
            L[i]-=L[j]
    L[i+1]+=L[f]
    L[f]=L[i+1]-L[f]
    L[i+1]-=L[f]
    return i+1
numeros=[]
for i in range(1,len(loteria[0])):
    for j in range(1,len(loteria)):
        numeros.append(loteria[j][i])
print(numeros)
numeros[0]+=numeros[1]
numeros[1]=numeros[0]-numeros[1]
numeros[0]-=numeros[1]
print(numeros)
quick_sort(numeros,0,len(numeros)-1)
print(numeros)
