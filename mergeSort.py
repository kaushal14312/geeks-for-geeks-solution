'''Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Input: arr[] = [1, 3 , 2]
Output: [1, 2, 3]
Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105'''

class Solution:
    
    def merge(self, arr, l, m, r):
        # Create temporary arrays to hold the two halves
        left = arr[l:m + 1]
        right = arr[m + 1:r + 1]

        i = 0  # Initial index of the first subarray
        j = 0  # Initial index of the second subarray
        k = l  # Initial index of the merged subarray

        # Merge the temporary arrays back into arr[l..r]
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy the remaining elements of left[], if there are any
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy the remaining elements of right[], if there are any
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def mergeSort(self, arr, l, r):
        if l < r:
            # Find the middle point
            m = (l + r) // 2

            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)

            # Merge the sorted halves
            self.merge(arr, l, m, r)