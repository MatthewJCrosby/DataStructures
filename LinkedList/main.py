# doubly linked list


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class LinkedList:
    def __init__(self):
        #using dummy nodes to ensure smooth edge case handling
        self.front = Node('f', 'f')
        self.back = Node('b', 'b')
        self._size = 0

        #set them initiallty pointing to eachtoher
        self.back.prev = self.front
        self.front.next = self.back


    def delete(self, node):
        if self._size < 1:
            return ' no nodes tp delete'

        #deletes a specific node, not necessarily front or back
        #must know the node for this function to work

        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -=1
        #incase we want to do somthing with the deleted node, return it
        return node

    def addToFront(self, key, val):
        # create the node
        newNode = Node(key, val)

        # insert it to the front, update all pointers involved
        newNode.next = self.front.next
        self.front.next.prev = newNode  # Update the prev pointer of the previous first node
        self.front.next = newNode
        newNode.prev = self.front

        self._size += 1

        # return the new node if needed
        return newNode
    
    def addToBack(self, key, val):
        # create the node
        newNode = Node(key, val)

        # insert it to the back, update all pointers involved
        newNode.prev = self.back.prev
        self.back.prev.next = newNode  # Update the next pointer of the previous last node
        self.back.prev = newNode
        newNode.next = self.back
        self._size += 1

        #return the new node if needed
        return newNode
    
    def deleteFromFront(self):

        if self._size < 1:
            return ' no nodes tp delete'
        #takes a node from the front
        node = self.front.next
        self.front.next = node.next
        node.next.prev = self.front
        self._size -= 1
        return node

    def deleteFromBack(self):
        if self._size < 1:
            return ' no nodes tp delete'
        #removes a node from the end
        node = self.back.prev
        self.back.prev = node.prev
        node.prev.next = self.back
        self._size -= 1
        return node
    
    def __iter__(self):
        current = self.front.next
        while current != self.back:
            yield current
            current = current.next
    

#basic testing
if __name__ == "__main__":
    myLL = LinkedList()
    myLL.addToFront(1,1)
    myLL.addToBack(2,2)
    myLL.addToFront(3,3)
    myLL.addToBack(4,4)

    nodes = []
    for node in myLL:
        nodes.append(node.val)
    print(nodes)

    myLL.deleteFromBack()
    myLL.deleteFromFront()
    myLL.deleteFromFront()
    myLL.deleteFromFront()
    myLL.deleteFromFront()
    #print nodes
    nodes = []
    for node in myLL:
        nodes.append(node.val)
    print(nodes)