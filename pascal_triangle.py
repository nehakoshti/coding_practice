# https://leetcode.com/problems/pascals-triangle/
n=5
li=[]  # main list
for i in range(n):
    kli=[]  # sub list
    print(li)
    
    if i==0:   # for 1st ele as [1]
        kli.append(1)
        print("----")
    else:     # from 2nd sub array onwards       
        m=len(li[i-1])
        print(li[i-1], m ,"--last subarray & its len")
        # 1st and last append 1 then add things in between --> [1,....,1]
        kli.append(1)        
        for j in range(m-1):
            print(j,"-->", li[i-1][j],li[i-1][j+1])
            # add current num (i) and its next num (i+1) in array, till i = n-1th 
            kli.append( li[i-1][j]+li[i-1][j+1] )            
        kli.append(1)
        
    li.append(kli)
    print(li)
    print()
print(li)

#  O(n^2)  
