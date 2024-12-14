class Solution:
    # Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr):
        # Step 1: Sort the array
        arr.sort()
        n = len(arr)
        count = 0
        
        # Step 2: Iterate through the array
        for k in range(n - 1, 1, -1):  # k is the index of the largest side
            i, j = 0, k - 1  # i is the first side, j is the second side
            while i < j:
                if arr[i] + arr[j] > arr[k]:  # Check the triangle condition
                    count += (j - i)  # All pairs (i, i+1, ..., j) are valid
                    j -= 1  # Move the second pointer left
                else:
                    i += 1  # Move the first pointer right
        
        return count