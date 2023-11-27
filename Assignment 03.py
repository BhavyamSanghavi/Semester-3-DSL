if __name__ == '__main__':
    run=1
    while(run):
        n1=int(input("Enter number of rows of matrix 1 :"))
        m1=int(input("Enter number of columns of matrix 1 :"))
        n2=int(input("Enter number of rows of matrix 2 :"))
        m2=int(input("Enter number of columns of matrix 2 :"))

        if(n1!=n2 or m1!=m2):
            print("Operations not possible")
        else :
            mat1=[]
            print("First")
            for i in range(n1):
                row=[]
                for j in range(m1):
                    print("Element at ",i+1," ",j+1)
                    r= int(input("Enter element:"))
                    row.append(r)
                mat1.append(row)
            print(mat1)
            mat2=[]
            print("Second")
            for i in range(n2):
                row=[]
                for j in range(m2):
                    print("Element at ", i + 1, " ", j + 1)
                    r = int(input("Enter Element :"))
                    row.append(r)
                mat2.append(row)

        #addition
            print("ADDITION")
            for i in range(n1):
                for j in range(m1):
                    print(mat1[i][j]+mat2[i][j],end=" ")
                print()
            print("SUBTRACTION")
            for i in range(n1):
                for j in range(m1):
                    print(mat1[i][j] - mat2[i][j], end=" ")
                print()

            if(n2!=m1):
                print("Multiplication not possible")
            else:
                ans=[]
                for i in range(n1):
                    row=[]
                    for k in range(m1):
                        ele = 0
                        for j in range(m1):
                            ele+=mat1[i][j]*mat2[j][k]
                        row.append(ele)
                    ans.append(row)
                print("Multiplication=")
                print(ans)

            if(n1!=m1):
                print("Transpose not possible")
            else:
                print("TRANSPOSE")
                ans2=[[0 for i in range(n1)]for j in range(m1)]
                for i in range(n1):
                    for j in range(m1):
                        ans2[i][j]=mat1[j][i]
                print(ans2)
                run=0
