



def binarSearchIterative(data, target):
    # get mid point
    low = 0
    high = len(data)-1
    
    while low <= high: # the reason we are using <= is because we have to check the whole list and compare it to our target
        mid = (high + low ) // 2
        if target == data[mid]:
            return True

        elif target > data[mid]:
            low = mid + 1

        else:
            high = mid - 1

    return False


print(binarSearchIterative([1,2,3,4,5,6,7,8], 15))
        