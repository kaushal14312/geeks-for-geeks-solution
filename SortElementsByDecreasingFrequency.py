from collections import Counter

class Solution:
    # Function to sort the array according to frequency of elements.
    def sortByFreq(self, arr):
        # Step 1: Count frequencies
        frequency = Counter(arr)
        
        # Step 2: Sort the array based on frequency and value
        sorted_arr = sorted(arr, key=lambda x: (-frequency[x], x))
        
        return sorted_arr