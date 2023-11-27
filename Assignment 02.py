def solution_a(word):
    max=0
    longest=''
    for i in word:
        if(max<len(i)):
            max=len(i)
            longest=i
    print("Word with longest length=",longest)

def solution_b(str):
    d={'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0,'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0," ":0}
    # d = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    # print(d)
    for i in str:
        d[i]=1+d[i]
    print("Total count of each character=",d)

def solution_c(str):
    str2=str[::-1]
    if(str2==str):
        print("String is palindrome")
    else:
        print("String is not palindrome")


def solution_d(sub, str):
    n = len(sub)
    nw = len(str)
    cnt = 0
    for i in range(nw):
        flag = True
        for x in range(n):
            if (sub[x] != str[i + x]):
                flag = False
                break
        if (flag == True):
            print(sub, "found at index", i)
            break


def solution_e(word):
    count=0
    for i in word:
        for j in word:
            if i==j:
                count+=1
        print("Count of ",i,"=",count)
        count=0

if __name__ == '__main__':
    str=input("Enter String : ")
    word=str.split()
    # print(word)
    solution_a(word)
    solution_b(str)
    solution_c(str)
    sub=input("Enter substring")
    solution_d(sub,str)
    solution_e(word)
