# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.

#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        cnt0=0
        cnt1=0
        cnt2=0
        for i in range(len(arr)):
            if(arr[i]==0):
              cnt0+=1
            elif(arr[i]==1):
                cnt1+=1
            else:
                cnt2+=1
        i=0      
        while(cnt0>0):
            arr[i]=0
            i+=1
            cnt0-=1
        while(cnt1>0):
            arr[i]=1
            i+=1
            cnt1-=1
        while(cnt2>0):
            arr[i]=2
            i+=1
            cnt2-=1
        return arr

              


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,len(arr))
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends