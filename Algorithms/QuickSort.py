def swap(a,b,arr):
    if a!=b:
        arr[a],arr[b]=arr[b],arr[a]


def Partition(elements,start,end):
    pivot_index=start
    pivot=elements[pivot_index]

    while start<end:
        while start<len(elements) and elements[start]<=pivot:
            start+=1

        while elements[end]>pivot:
            end-=1
        if start<end:
            swap(start,end,elements)
    swap(pivot_index,end,elements)
    return end
def QuickSort(elements,start,end):
    if start<end:
        pi_index=Partition(elements,start,end)
        QuickSort(elements,start,pi_index-1) #left partition
        QuickSort(elements,pi_index+1,end) #right partititon

element=[10,54,3,2,14,6,52,45]
QuickSort(element,0,len(element)-1)
print((element))