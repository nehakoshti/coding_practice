# https://leetcode.com/problems/next-permutation/description/

"""A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory."""

def nextPermutation(nums):
    
    n=len(nums)
    prev=nums[n-1]
    # find ele 
    print(nums)
    for i in range(n-2,-1,-1):
        print("p:",prev,"curr:",nums[i])
        if nums[i]<prev:
            prev=nums[i]
            ind=i
            break
        prev=nums[i]
        ind=i
    # ind=nums.index(prev)
    print("ele:",prev,ind,"---")
    
    if ind!=0:
        # next larger of ele
        x=max(nums)
        ind1= nums.index(max(nums))
        
        for i in range(ind+1,n):
            if nums[i]>prev and nums[i]<x:
                x=nums[i]
                ind1=i
        print("swap with:",x, ind1,"---")
        
        # swap
        print(nums)
        nums[ind],nums[ind1]=nums[ind1],nums[ind]
        print(nums)
        # reverse
        nums[ind+1:n]= reversed(nums[ind+1:n])
        print("ans:",nums,"\n") 
    else:
        nums=list(reversed(nums))
        print("ans_:",nums,"\n") 

    
nums = [1,2,3]
nextPermutation(nums)
nums = [3,2,1]
nextPermutation(nums)
nums = [1,1,5]
nextPermutation(nums)
nums = [9, 5, 4, 3, 1]
nextPermutation(nums)


"""solution trick : 4,3,5,2,1
  decreasing number in reverse order = 3  --> 4,_3_,5,2,1
  ele = index of 3 = 1
  number bigger than 3 in its RHS = 5   --> 4,3,_5_,2,1
  swap 3 and 5 --> 4,5,3,2,1
  reverse entire array next to ele (2 to n)--> 4,5, 1,2,3 = answer
  
"""



