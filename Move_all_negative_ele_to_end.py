# Given an unsorted array arr[ ] having both negative and positive integers. The task is to place all negative elements at the end of the array without changing the order of positive elements and negative elements.

# Examples:

# Input : arr[] = [1, -1, 3, 2, -7, -5, 11, 6 ]
# Output : [1, 3, 2, 11, 6, -1, -7, -5]
# Explanation: By doing operations we separated the integers without changing the order.
# Input : arr[] = [-5, 7, -3, -4, 9, 10, -1, 11]
# Output : [7, 9, 10, 11, -5, -3, -4, -1]
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 ≤ arr.size ≤ 106
# -109 ≤ arr[i] ≤ 109

#User function Template for python3


def segregateElements(arr):
    # Your code goes here
    pos_arr=[]
    neg_arr=[]
    for i in arr:
        if i<0:
            neg_arr.append(i)
        else:
            pos_arr.append(i)
    ans= pos_arr + neg_arr
    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
  
    a = [int(x) for x in input().strip().split()]
    ob = segregateElements(a)
    print(ob)


if __name__ == "__main__":
    main()

# } Driver Code Ends