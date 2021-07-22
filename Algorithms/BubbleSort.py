def BubbleSort(ls):
    size=len(ls)
    for i in range(size-1):
        swapped=False # to check if elements are already sorted
        for j in range(size-1-i):
            if ls[j]>ls[j+1]:
                #swap
                ls[j],ls[j+1]=ls[j+1],ls[j]
                swapped=True
        if not swapped:
            break

ls=[12,125,11,41,54,45,545,545454,212,3,5,64,50]
BubbleSort(ls)
print(ls)
