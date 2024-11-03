# Given an array arr[] of positive integers. Find the number of pairs of integers whose difference equals a given number k.
# Note: (a, b) and (b, a) are considered the same. Also, the same numbers at different indices are considered different.

# Examples:

# Input: arr[] = [1, 5, 3, 4, 2], k = 3
# Output: 2
# Explanation: There are 2 pairs with difference 3,the pairs are {1, 4} and {5, 2} 

def countPairsWithDiffK(self,arr, k):
    occ=[0]*(max(arr)+1)
    count=0
    for i in arr:
        occ[i]+=1
    for i in arr:
        x= i-k
        if x>=0:
            count+= occ[x]
    return count

# create a hash map --> o(n) time and space
