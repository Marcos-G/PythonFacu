class Node:
    value = None
    nextNode = None

class LinkedList:
    head = None

    # Pretty print the list
    def __str__(self):
        # print("--------------------------")
        # print("Head: " + str(self.head.value) if self.head else "Head: None")
        out = ""
        head = self.head
        while head != None:
            out += str(head.value) + " -> "
            head = head.nextNode
        return out + "None" + "\n"

def add(List, el):
    newNode = Node()
    newNode.value = el
    newNode.nextNode = List.head
    List.head = newNode

def search(List, value):
    index = 0
    currentNode = List.head
    while currentNode != None:
        if currentNode.value == value:
            return index
        currentNode = currentNode.nextNode
        index += 1
    return None

def insert(List, el, position):
    # Verify position in boundaries
    if position > length(List):
        return None
    index = 0
    prevNode = List.head
    newNode = Node()
    newNode.value = el
    if position == 0 or List.head == None:
        add(List, el)
        return 0
    # traverse list until one node before desired
    # position, verifing it's not the end of the list
    while prevNode.nextNode and index != position - 1:
        prevNode = prevNode.nextNode
        index += 1
    nextNode = prevNode.nextNode
    prevNode.nextNode = newNode
    newNode.nextNode = nextNode
    return position

def delete(List, value):
    pos = search(List, value)
    if pos != None:
        prevNode = List.head
        # if it's the first, attach head to next node
        if pos == 0:
            List.head = prevNode.nextNode
        else:
            # traverse the list to get the reference of the node
            # that's behind the one we want to delete
            while pos > 1:
                prevNode = prevNode.nextNode
                pos -= 1
            newNextNode = prevNode.nextNode.nextNode if prevNode.nextNode != None else None
            prevNode.nextNode = newNextNode
    else:
        return None

def append(List, el):
    index = 0
    prevNode = List.head
    newNode = Node()
    newNode.value = el
    if List.head == None:
        add(List, el)
        return
    # traverse list till the end
    while prevNode.nextNode:
        prevNode = prevNode.nextNode
    prevNode.nextNode = newNode

def length(List):
    if List:
        node = List.head
        i = 0
        while node:
            i += 1
            node = node.nextNode
        return i

def enqueue(L, el):
    append(L, el)

def dequeue(L):
    if L and L.head:
        node = L.head
        L.head = node.nextNode
        return node.value
    return None

def pop(L):
    if L and L.head:
        node = L.head
        L.head = node.nextNode
        return node.value
    return None

def push(L, el):
    add(L, el)

def access(List, index):
    i = 0
    node = List.head
    while node and i != index:
        node = node.nextNode
        i += 1
    return None if not node else node.value

def update(L, el, position):
    if L and length(L) > position:
        node = L.head
        i = 0
        while i < position:
            node = node.nextNode
            i += 1
        node.value = el
        return True
    else:
        return None
