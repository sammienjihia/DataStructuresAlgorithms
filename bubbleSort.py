
def bubbleSort(a_list):
    x = len(a_list)

    for i in range(x):

        for n in range(x-1): # the x-1 is to handle the k+1 when comparing. Example 
            if a_list[n] > a_list[n+1]:
                a_list[n], a_list[n+1]=a_list[n+1], a_list[n]
            else:
                pass

    return a_list

print(bubbleSort([6,4,3,2,1]))

# Time complexity is of Big O (n2)

# NB range(3) shall return [0,1,2]