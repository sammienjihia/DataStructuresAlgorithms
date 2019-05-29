
def bubbleSort(a_list):
    x = len(a_list)

    for i in range(x):

        for n in range(x-1):
            if a_list[n] > a_list[n+1]:
                a_list[n], a_list[n+1]=a_list[n+1], a_list[n]
            else:
                pass

    return a_list

print(bubbleSort([4,2,3,8,5,9,7,6,10, 1]))