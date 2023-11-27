class search_algos:
    def linearSearch(self,list,key):
        index=0
        for i in list:
            if key==i:
                print(key ,   "Found at index ",index)
                print("Comparison=",index+1)
                break
            index+=1
        else:
            print(key,"Not Found comparisons | ",index+1," |")

    def sentinel(self,list,key):
        n=len(list)
        last=list[-1]
        list[-1]=key
        i=0
        while(list[i]!=key):
            i+=1
        list[-1]=last
        if ((i < n - 1) or (list[n - 1] == key)):
            print(key, "is present at index", i)
            print("Comparisons=",i+1)
        else:
            print("Element Not found")
            print("Comparisons=", i+1)


s=search_algos()
list=[]
n=int(input("Enter number of elements : "))
for i in range(n):
    list.append(int(input()))
flag=1
while(flag==1):
    op=int(input("Enter 1 for linear search and 2 for sentinel search :"))
    if(op==1):
        key=int(input("Enter key for linear search: "))
        s.linearSearch(list,key)
    elif(op==2):
        key=int(input("Enter key for sentinel search: "))
        s.sentinel(list,key)
    flag=int(input("Enter 1 to continue : "))
