'''Given an array arr. The task is to sort the array elements by Heap Sort.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]
Explanation: After sorting elements using heap sort, elements will be in order as 1,3,4,7,9.
Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Explanation: After sorting elements using heap sort, elements will be in order as 1, 2,3,4,5,6,7,8,9,10.
Input: arr[] = [2, 1, 5]
Output: [1, 2, 5]
Explanation: After sorting elements using heap sort, elements will be in order as 1,2,5,
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106'''

class Solution:
    def heapify(self, arr, n, i):
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left child index
        right = 2 * i + 2  # right child index

        # If left child is larger than root
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child is larger than largest so far
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is not root
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]  # Swap

            # Recursively heapify the affected sub-tree
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)

        # Build a maxheap
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)

        # One by one extract elements from heap
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]  # Swap
            self.heapify(arr, i, 0)
