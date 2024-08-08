# Given an array arr[] and an integer k where k is smaller than the size of the array, the task is to find the kth smallest element in the given array. It is given that all array elements are distinct.
# Input:
# n = 6
# arr[] = 7 10 4 3 20 15
# k = 3
# l=0 r=5

# Output : 
# 7

# Explanation :
# 3rd smallest element in the given 
# array is 7.

#User function Template for python3
class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        return arr[k-1]
        
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    import random 
    t=int(input())
    for tcs in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        k=int(input())
        ob=Solution()
        print(ob.kthSmallest(arr, 0, n-1, k))
        
# } Driver Code Ends