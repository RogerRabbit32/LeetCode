from copy import copy

class MyLinkedList:

    def __init__(self, head=None):
        self.head = head
        self.prev = None
        self.nextval = None

    def get(self, index: int) -> int:
        n = self
        for i in range(index):
            if n.nextval is None:
                return -1
            else:
                n = n.nextval
        if n.head is None:
            return -1
        return n.head if n else -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = val
        else:
            self.nextval = copy(self)
            self.head = val

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.head = val
        else:
            newTail = MyLinkedList(val)
            n = self
            while n.nextval:
                n = n.nextval
            n.nextval = newTail


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.nextval = copy(self)
            self.head = val
        else:
            newNode = MyLinkedList(val)
            n = self
            for i in range(index - 1):
                if n.nextval is None:
                    return -1
                else:
                    n = n.nextval
            newNode.nextval = n.nextval
            n.nextval = newNode
        

    def deleteAtIndex(self, index: int) -> None:
       
        if index == 0:
            x = self
            while x.nextval is not None:
                x.head = x.nextval.head
                x = x.nextval
            x.head = None
        else:
            n = self
            x = 0
            while x != index:
                if n.nextval is None:
                    return -1
                else:
                    n = n.nextval
                    x += 1
            if n is None:
                return
            else:
                z = n.nextval
                x = 0
                y = self
                while x != index - 1:
                    y = y.nextval
                    x += 1
                y.nextval = z
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)