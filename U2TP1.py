from linkedlist import *
from mergesort import *
def esPar(x):
    if x <= 0:
        x = -x
    return (x - (x % 1)) % 2 == 0

def ordenRaro(vector):
    ordenado = mergeSort(vector)
    izq = LinkedList()
    der = LinkedList()
    while length(ordenado) > 1:
        valor = pop(ordenado)
        if esPar(valor):
            add(der, valor)
        else:
            append(izq, valor)

    medio = pop(ordenado)

    while length(izq) > 0:
        append(ordenado, pop(izq))

    append(ordenado, medio)

    while length(der) > 0:
        append(ordenado, pop(der))
list=LinkedList()
append(list,3)
append(list,36)
append(list,32)
append(list,45)
append(list,0)
print(list)
print(ordenRaro(list))
