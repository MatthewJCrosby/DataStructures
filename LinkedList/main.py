# doubly linked list


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
    

class LinkkedList:
    def __init__(self):
        self.front = Node('f', 'f')
        self.back = Node('b', 'b')
        self.back.next = self.front
        self.front.prev = self.back


    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def addToFront(self, key, val):
        newNode = Node(key, val)
        self.front.prev.next = newNode
        newNode.prev = self.front.prev
        self.front.prev = newNode
        newNode.next = self.front

        return newNode

    def deleteFromBack(self):
        key = self.back.next.key
        self.back.next = self.back.next.next
        self.back.next.prev = self.back
        return key
