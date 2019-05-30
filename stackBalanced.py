from stack import Stack

"""
Using the above stack, check if a string has a balanced usage of parenthesis and brackets
"""

# For every opening parenthesis, push it into the stack

# For every closing parenthesis, pop the stack and compare

def isMatch(item1, item2):
    if item1 == "(" and item2 == ")":
        return True
    elif item1 == "[" and item2 == "]":
        return True
    elif item1 == "{" and item2 == "}":
        return True
    else:
        return False


def isBalanced(string_item):
    # Create a stack object
    stk = Stack()
    counter = 0
    is_balanced = True

    while counter < len(string_item) and is_balanced:
        # if the item in the string is an opening parenthesis, then push it into the stack
        if string_item[counter] in "({[":
            stk.pushItem(string_item[counter])

        # if the item in the string is a closing parenthesis, first check if the stack is empty if not pop and compare
        else:
            # check if stack is empty
            if stk.checkIfEmpty():
                is_balanced = False
            else:
                item1 = stk.removeItem()
                item2 = string_item[counter]
                is_balanced = isMatch(item1, item2)

        counter += 1

    if is_balanced and stk.checkIfEmpty():
        return True
    else:
        return False
        

print(isBalanced("(()("))