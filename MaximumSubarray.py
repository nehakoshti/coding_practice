# https://leetcode.com/problems/maximum-subarray/description/
# Kadane's Algorithm

def maxSubArray( arr):
    maxend=arr[0]
    res=arr[0]
    for i in range(1,len(nums)):
        
        maxend=max(nums[i] , maxend+nums[i])
        res=max(maxend,  res)
        print("curr:",maxend,"ans:",res,"\n")
    print(res)
        
    
        
nums = [-2,1,-3,4,-1,2,1,-5,4]
maxSubArray( nums)
