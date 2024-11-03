#User function Template for python3
""" Given an array arr[ ] of positive elements. Consider the array as a circular array, meaning 
the element after the last element is the first element of the array. The task is to find the maximum sum 
of the absolute differences between consecutive elements with shuffling of array elements allowed i.e. shuffle 
the array elements and make [a1..an] such order that  |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1| is maximized.

Examples:

Input: arr[] = [4, 2, 1, 8]
Output: 18
Explanation: After Shuffling, we get [1, 8, 2, 4]. 
Sum of absolute difference between consecutive elements after rearrangement 
= |1 - 8| + |8 - 2| + |2 - 4| + |4 - 1| = 7 + 6 + 2 + 3 = 18."""

class Solution:
    def maxSum(self,arr):
        arr=sorted(arr)
        # print(arr)
        n=len(arr)
        s1=sum(arr[0:len(arr)//2])
        # print(s1)
        if n%2==0:
            s2=sum(arr[len(arr)//2 : len(arr)])
            # print(s2)
        else:
            s2=sum(arr[len(arr)//2+1 : len(arr)])
            
        ans= 2*s2 - 2*s1
        return(ans)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    # t = int(input())
    t=1
    for _ in range(t):
        # arr = list(map(int, input().split()))
        arr= [4, 2, 1, 8]
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
