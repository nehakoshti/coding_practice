def setZeroes( matrix):
    # print(matrix)
    row=len(matrix)
    col=len(matrix[0])
    print(row,col)
    zcol=[]
    zrow=[]
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                if i not in zrow:
                    zrow.append(i)
                if j not in zcol:
                    zcol.append(j)
    # print(zrow,zcol)
    for m in zrow:
        for i in range(col):
            matrix[m][i]=0
    for n in zcol:
        for i in range(row):
            matrix[i][n]=0
            
    print(matrix)
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes( matrix)
