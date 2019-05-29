
# binary search iterative

def binarySearchIterative(a_list, target_item):
    # Ask if the list is sorted
    # If list is sorted get the mid point
    low = 0
    high =len(a_list)-1

    found = False
    while high>= low: # This is done to ensure we've captured the last item in the list
        mid = (low + high)//2
        
        if target_item == a_list[mid]:
           found = True
           return found
        elif target_item < a_list[mid]:
            high = mid-1

        else:
            low = mid+1

    return found

       
    

print(binarySearchIterative([1,2,3,4,5,6], 5))

def binarySearchRecursive(a_list, target_item):
    low = 0
    high = len(a_list)-1

    
    def _binary_search(low, high):
        mid = (low + high)//2
        found = False

        if high>=low:

            if target_item == a_list[mid]:
                found = True
                return found

            elif target_item < a_list[mid]:
                return _binary_search(low, mid -1)

            else:
                return _binary_search(mid+1, high)

        else:
            return found

    return _binary_search(low, high)


print(binarySearchRecursive([1,2,3,4,5,6], 1))

