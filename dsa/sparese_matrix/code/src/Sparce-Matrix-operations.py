#importing os module to help in locating files
import os

#getting tuples from file location
def LoadTuples(location):
    #checking if file location exist
    if os.path.exists(location):
        with open(location,'r') as file:
            try:
                rows=int(file.readline().strip().split("=")[1])+1
                cols=int(file.readline().strip().split("=")[1])+1
            except:
                raise ValueError("Input file has wrong format")
            
            #getting list of tuples
            Tuples=[]
            for line in file:
                if line.startswith("(") and line.endswith(")\n"):
                    try:
                        Tuple=line.strip("()\n").split(",")
                        if len(Tuple)!=3:
                            raise ValueError("Input file has wrong format")
                        Tuples.append(tuple(map(int,Tuple)))
                    except:
                        raise ValueError("Input file has wrong format")
                else:
                    raise ValueError("Input file has wrong format")
        return (rows,cols,Tuples)



#creating zero matrix
def Zero_Matrix(rows,cols):
    matrix=[]
    for _ in range(rows):
        row=[]
        for _ in range(cols):
            row.append(0)
        matrix.append(row)
    return matrix

#creeating sparce matrix from list of tuples
def SparseMatrix(rows,cols,Tuples):
    #loading zero matrix
    matrix=Zero_Matrix(rows=rows,cols=cols)
    #filling non zero values in matrix
    for T in Tuples:
        i,j,v =T
        matrix[i][j]=v
    return matrix

#defining Add function to Add two matrix
def Add(A,B):
    i=len(A) #getting rows of Matrix A
    j=len(A[0]) #getting columns of Matrix A
    m=len(B) #getting rows of Matrix B
    n=len(B[0]) #getting columns of matrix B

    #checking if Matrice can be added
    if i==m and j==n:
        #adding Matrix A and B
        sum=[]
        for r in range(i):
            row=[]
            for v in range(j):
                row.append(A[r][v]+B[r][v])
            sum.append(row)
        #returning sum Matrix
        return sum
    print("can't add these matrice, rows and columns of 1st mastix have to equal to that of 2nd matrix ")

#defining Sub function to subtract two matrix
def Sub(A,B):
    i=len(A) #getting rows of Matrix A
    j=len(A[0]) #getting columns of Matrix A
    m=len(B) #getting rows of Matrix B
    n=len(B[0]) #getting columns of matrix B

    #checking if Matrice can be subtracted
    if i==m and j==n:
        #subtracting Matrix B from A
        sub=[]
        for r in range(i):
            row=[]
            for v in range(j):
                row.append(A[r][v]-B[r][v])
            sub.append(row)
        #returning subtraction Matrix
        return sub
    print("can't subtract these matrice, rows and columns of 1st mastix have to equal to that of 2nd matrix ")

#defining Multi function to multiply two matrix
def Multi(A,B):
    i=len(A) #getting rows of Matrix A
    j=len(A[0]) #getting columns of Matrix A
    m=len(B) #getting rows of Matrix B
    n=len(B[0]) #getting columns of matrix B

    #checking if Matrice can be multplied
    if j==m:
        #multipliying Matrix A and B
        multi=[]
        for r in range(i):
            row=[]
            for v in range(n):
                sum=0
                for k in  range(j):
                    sum+=A[r][k]* B[k][v]
                row.append(sum)
            multi.append(row)
        #returning product Matrix
        return multi
    print("can't multply these matrice, rows of 1st mastix have to equal to columns of 2nd matrix ")

#converting sparce matrix into tuples
def toTuples(A):
    rows=len(A)
    cols=len(A[0])
    tuples=[]
    for i in range(rows):
        for j in range(cols):
            if A[i][j]!=0:
                tuples.append((i,j,A[i][j]))
    return tuples

#creating function that writes tuples of sparce matrix to files
def toFile(A,locaion):
    rows=len(A)-1
    cols=len(A[0])-1
    Tuples=toTuples(A)
    with open(locaion,'w') as file:
        file.write(f"rows = {rows}\n")
        file.write(f"columns = {cols}\n")
        for T in Tuples:
            file.write(f"{T}\n")


#creating main function 
def main():
    
    #locating main directories
    baseDir=os.path.dirname(__file__)
    inputDir=os.path.join(baseDir,"../../sample_inputs")
    outputDir=os.path.join(baseDir,"../../sample_outputs")

    #locating input files
    
    matrix1=os.path.join(inputDir,input("enter file name of first matrix from sample_inputs/ directory: "))
    matrix2=os.path.join(inputDir,input("enter file name of first matrix from sample_inputs/ directory: "))

    #Extracting tuples
    i,j,M1=LoadTuples(matrix1)
    m,n,M2=LoadTuples(matrix2)

    #loading Sparce Matrix
    A=SparseMatrix(i,j,M1)
    B=SparseMatrix(m,n,M2)

    #prompting user to choose operation
    print("select what you want to do with these matrice: ")
    print(". 1 :Add")
    print(". 2 :subtract")
    print(". 3 :Multiply")
    choice=int(input())

    #performing operations on matrix A and B
    #and writing out put to their specific file location based on user's choice
    match choice:
        case 1:
            sum=Add(A,B)
            if sum:
                toFile(sum,f"{outputDir}/summation.txt")
                print("summation was succefuly stored in sample_outputs/ ")
        case 2:
            sub=Sub(A,B)
            if sub:
                toFile(sub,f"{outputDir}/subtraction.txt")
                print("subutraction was succefuly stored in sample_outputs/ ")
        case 3:
            prod=Multi(A,B)
            if prod:
                toFile(prod,f"{outputDir}/Multiplication.txt")
                print("multiplication was succefuly stored in sample_outputs/ ")
        case _:
            print("invalid choice")
        

if __name__== "__main__":
    main()


