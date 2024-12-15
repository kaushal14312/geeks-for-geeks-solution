class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # Check if mid is a peak
            if (mid == 0 or arr[mid] > arr[mid - 1]) and (mid == n - 1 or arr[mid] > arr[mid + 1]):
                return mid  # Return the index of the peak
            
            # If the left neighbor is greater, then there must be a peak on the left side
            if mid > 0 and arr[mid - 1] > arr[mid]:
                high = mid - 1
            else:  # If the right neighbor is greater, then there must be a peak on the right side
                low = mid + 1
                
        return -1  # This should never be reached if the input constraints are followed

# Function to validate the peak
def is_peak(arr, index):
    n = len(arr)
    if index < 0 or index >= n:
        return False
    if (index == 0 or arr[index] > arr[index - 1]) and (index == n - 1 or arr[index] > arr[index + 1]):
        return True
    return False