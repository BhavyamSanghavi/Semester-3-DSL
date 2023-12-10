def bubblesort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j+1]<l[j]:
                l[j+1],l[j]=l[j],l[j+1]
        print(i+1," Pass=",l)

def insertionsort(a):
    if len(a)<=1:
        return
    else:
        for i in range(1,len(a)):
            j=i-1
            key=a[i]
            while(j>=0 and key<a[j]):
                a[j+1]=a[j]
                j=j-1
            a[j+1]=key
            print(i, " Pass=", a)

def shellsort(a):
    n = len(a)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                j -= gap
            a[j] = temp
        gap //= 2
    print("Sorted=",a)

def selectionsort(a):
    for i in range(len(a)):
        index=i
        for j in range(i+1,len(a)):
            if a[j]<a[index]:
                index=j
        a[i],a[index]=a[index],a[i]
        print(i+1,"Pass=",a)

if __name__ == '__main__':
    l=[5,4,3,2,1]
    # n=int(input("Enter total number of elements :"))
    # for i in range(n):
    #     l.append(int(input()))

    # bubblesort(l)
    # insertionsort(l)
    # shellsort(l)
    selectionsort(l)
    # print(l)
