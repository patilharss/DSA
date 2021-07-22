import time
def timeittakes(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__+' took '+str((end-start)*1000)+' mil sec')
        return result
    return wrapper


@timeittakes
def linear_search(list,find):
    for index,element in enumerate(list):
        if element==find:
            return index

    else:
        return -1
@timeittakes
def binary_search(list,find):
    leftindex=0
    rightIndex=len(list)-1
    midindex=0

    while leftindex<=rightIndex:
        midindex=(leftindex+rightIndex)//2
        midnumber=list[midindex]

        if midnumber==find:
            return midindex
        if midnumber<find:
            leftindex=midindex+1
        else:
            rightIndex=midindex-1
    return -1




ls=[i for i in range(0,1000000)]
find=1000000
linear_search(ls,find)
binary_search(ls,find)
