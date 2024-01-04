# doubly linked list


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class LinkkedList:
    def __init__(self):
        #using dummy nodes to ensure smooth edge case handling
        self.front = Node('f', 'f')
        self.back = Node('b', 'b')
        self._size = 0

        #set them initiallty pointing to eachtoher
        self.back.next = self.front
        self.front.prev = self.back


    def delete(self, node):

        #deletes a specific node, not necessarily front or back
        #must know the node for this function to work

        node.prev.next = node.next
        node.next.prev = node.prev
        #incase we want to do somthing with the deleted node, return it
        return node

    def addToFront(self, key, val):
        #create the node
        newNode = Node(key, val)

        #insert it to the front, update all pointers involved
        self.front.prev.next = newNode
        newNode.prev = self.front.prev
        self.front.prev = newNode
        newNode.next = self.front
        self._size += 1

        #return the new node if needed
        return newNode
    
    def addToBack(self, key, val):
        #create the node
        newNode = Node(key, val)

        #insert it to the back, update all pointers involved
        self.back.prev.next = newNode
        newNode.prev = self.back.prev
        self.back.prev = newNode
        newNode.next = self.back
        self._size += 1

        #return the new node if needed
        return newNode
    
    def deleteFromFront(self):
        #takes a node from the front
        node = self.front.next
        self.front.next = self.front.next.next
        self.front.next.prev = self.front
        self._size -= 1
        return node

    def deleteFromBack(self):
        #removes a node from the end
        node = self.back.next
        self.back.next = self.back.next.next
        self.back.next.prev = self.back
        self._size -= 1
        return node
    

