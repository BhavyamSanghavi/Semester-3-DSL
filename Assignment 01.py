def solution_a(ckt,bmt):
    ans1=[]
    for i in ckt:
        if i in bmt:
            ans1.append(i)
    return ans1
def solution_b(ckt,bmt,ans1):
    ans2=[]
    for i in ckt:
        if(i not in ans1):
            ans2.append(i)
    for i in bmt:
        if(i not in ans1):
            ans2.append(i)
    return ans2
def solution_c(ckt,bmt,uni):
    ans3=[]
    for i in uni:
        if((i not in ckt) and (i not in bmt)):
            ans3.append(i)
    return ans3
def solution_d(ckt,bmt,fb):
    ans4=[]
    for i in fb:
        if(i not in bmt)and (i in ckt):
            ans4.append(i)
    return ans4

if __name__ == '__main__':
    uni=[]
    ckt=[]
    bmt=[]
    fb=[]
    u = int(input("Enter total number of students : "))
    for i in range(u):
        uni.append(int(input()))
    c = int(input("Enter total number of students playing cricket: "))
    for i in range(c):
        ckt.append(int(input()))
    b = int(input("Enter total number of students playing badminton: "))
    for i in range(b):
        bmt.append(int(input()))
    f = int(input("Enter total number of students playing football: "))
    for i in range(f):
        fb.append(int(input()))
    ans1=solution_a(ckt,bmt)
    ans2=solution_b(ckt,bmt,ans1)
    ans3=solution_c(ckt,bmt,uni)
    ans4=solution_d(ckt,bmt,fb)
    print(ans1)
    print(ans2)
    print(ans3)
    print(ans4)
