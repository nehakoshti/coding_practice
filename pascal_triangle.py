# https://leetcode.com/problems/pascals-triangle/
n=5
li=[]
for i in range(n):
    kli=[]
    print(li)
    if i==0:
        kli.append(1)
        print("----")
    else:
        m=len(li[i-1])
        print(li[i-1],m,"--last len")
        kli.append(1)
        
        for j in range(m-1):
            print(j,"-->", li[i-1][j],li[i-1][j+1])
            kli.append( li[i-1][j]+li[i-1][j+1] )
            
        kli.append(1)
    li.append(kli)
    print(li)
    print()
print(li)

# O(n*log(n))
