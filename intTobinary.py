"""
Use a stack data structure to convert integers values to binary
"""
from  stack import Stack

def toBinary(number):
    stk = Stack()

    while number > 0:
        remainder = number % 2
        stk.pushItem(remainder)
        number = number // 2

    binaryNumber = ""
    while not stk.checkIfEmpty():
        binaryNumber += str(stk.removeItem())

    return binaryNumber

print(toBinary(242))