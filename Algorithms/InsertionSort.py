import statistics
def insertionsort(ls):
    for i in range(1,len(ls)):
        anchor=ls[i]
        j=i-1
        while j >=0 and anchor<ls[j]:
            ls[j+1]=ls[j]
            j-=1
        ls[j+1]=anchor


ls=[2,1,5,7,2,0,5]
insertionsort(ls)
print(ls)