'''Given k sorted arrays arranged in the form of a matrix of size k * k. The task is to merge them into one sorted array. Return the merged sorted array ( as a pointer to the merged sorted arrays in cpp, as an ArrayList in java, and list in python).


Examples :

Input: k = 3, arr[][] = {{1,2,3},{4,5,6},{7,8,9}}
Output: 1 2 3 4 5 6 7 8 9
Explanation: Above test case has 3 sorted arrays of size 3, 3, 3 arr[][] = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]. The merged list will be [1, 2, 3, 4, 5, 6, 7, 8, 9].
Input: k = 4, arr[][]={{1,2,3,4},{2,2,3,4},{5,5,6,6},{7,8,9,9}}
Output: 1 2 2 2 3 3 4 4 5 5 6 6 7 8 9 9 
Explanation: Above test case has 4 sorted arrays of size 4, 4, 4, 4 arr[][] = [[1, 2, 2, 2], [3, 3, 4, 4], [5, 5, 6, 6], [7, 8, 9, 9 ]]. The merged list will be [1, 2, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8, 9, 9].
Expected Time Complexity: O(k2*Log(k))
Expected Auxiliary Space: O(k2)

Constraints:
1 <= k <= 100'''

import heapq

class Solution:
    # Function to merge k sorted arrays.
    def mergeKArrays(self, arr, K):
        # Create a min-heap
        min_heap = []
        
        # Step 1: Initialize the heap with the first element of each array
        for i in range(K):
            if arr[i]:  # Check if the array is not empty
                heapq.heappush(min_heap, (arr[i][0], i, 0))  # (value, array index, element index)
        
        merged_array = []
        
        # Step 2: Extract the minimum element and add the next element from the same array
        while min_heap:
            value, array_index, element_index = heapq.heappop(min_heap)
            merged_array.append(value)  # Add the smallest value to the merged array
            
            # If there is a next element in the same array, push it to the heap
            if element_index + 1 < len(arr[array_index]):
                next_value = arr[array_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, array_index, element_index + 1))
        
        return merged_array