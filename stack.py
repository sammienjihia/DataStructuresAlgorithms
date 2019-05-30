
#  Implementing a Stack data strucuture

# A stack object is simply a python 

class Stack():
    def __init__(self):
        self.items = []

    def pushItem(self, item):
        self.items.append(item)


    def removeItem(self):
        return self.items.pop()

    def getLen(self):
        return len(self.items)

    def getStackItems(self):
        return self.items

    def checkIfEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def peek(self):
        if self.checkIfEmpty():
            return None
        else:
            return self.items[-1]




stk = Stack()
print(stk.checkIfEmpty())
stk.pushItem(3)
stk.pushItem(1)
stk.pushItem(4)
stk.pushItem(6)
stk.pushItem(5)

print(stk.getLen())
print(stk.getStackItems())

stk.removeItem()
print(stk.getStackItems())
print(stk.checkIfEmpty())
print(stk.peek())