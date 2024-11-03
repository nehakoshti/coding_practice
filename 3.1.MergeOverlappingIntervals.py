# https://www.geeksforgeeks.org/merging-intervals/
"""Given an array of time intervals where arr[i] = [starti, endi], the task is to merge all the overlapping intervals into one and output the result which should have only mutually exclusive intervals.

Examples:

Input: arr[] = {{1, 3}, {2, 4}, {6, 8}, {9, 10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: In the given intervals, we have only two overlapping intervals {1, 3} and {2, 4}. Therefore, we will merge these two and return {{1, 4}, {6, 8}, {9, 10}}.


Input: arr[] = {{6, 8}, {1, 9}, {2, 4}, {4, 7}}
Output: {{1, 9}}
Explanation: Since all the intervals overlap, we will merge them into a single interval."""


def mergeOverlap(arr):
    ans=[[0,0]]
    j=len(ans)-1
    arr=sorted(arr)
    print(arr)
    
    for i in arr:
        print(i[0],i[1])
        if ans[j][1] >i[0]:
            ans[j][1]=i[1]
        else:
            ans.append(i)
            j=len(ans)-1
        print(ans)
    ans.pop(0)
    print(ans)

arr = [[1, 3], [2, 4], [6, 8], [7, 10]]
res = mergeOverlap(arr)

# time --> O(n)
