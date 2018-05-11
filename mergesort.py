# UNCuyo - Licenciatura en Ciencias de la computación
# Algorítmos y estructuras de datos I
# TP Algoritmos de ordenamiento
# Merge Sort
# Arlandis, Luciano.
# Leg: 09723
#
#-----------------------------------------------------------------

from linkedlist import LinkedList, add, pop, length, append

def split(L):
    leftL = LinkedList()
    rightL = LinkedList()
    n = length(L)

    node = L.head
    # Fill left list
    for i in range(n // 2):
        append(leftL, node.value)
        node = node.nextNode
    # Fill right list
    while node:
        append(rightL, node.value)
        node = node.nextNode

    return leftL, rightL

def merge(leftL, rightL):
    L = LinkedList()
    # Comparamos las cabezas de las listas hasta que una esté vacia
    while leftL.head is not None and rightL.head is not None:
        leftValue = leftL.head.value
        rightValue = rightL.head.value
        if leftValue >= rightValue:
            append(L, pop(rightL))
        else:
            append(L, pop(leftL))
    # Si nos quedan elementos en la lista izquierda los agregamos
    while leftL.head is not None:
        append(L, pop(leftL))
    # Si nos quedan elementos en la lista derecha los agregamos
    while rightL.head is not None:
        append(L, pop(rightL))
    return L

def mergeSort(L):
    if L.head is None or L.head.nextNode is None:
        return L
    leftL, rightL = split(L)
    leftL = mergeSort(leftL)
    rightL = mergeSort(rightL)
    return merge(leftL, rightL)
