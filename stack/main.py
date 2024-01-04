from LinkedList.main import *
class Stack:
    def __init__(self):
        self.ll = LinkedList()
        

    def add(self, key, val):
        self.ll.addToFront(key, val)

    def pop(self):
        if self.ll._size > 0:
            node = self.ll.deleteFromFront
            return node
        
    
if __name__ == "__main__":
    mystack = Stack()
    mystack.add(1,1)
    mystack.add(2,2)
    mystack.add(3,3)

    print(mystack.ll.front.val)