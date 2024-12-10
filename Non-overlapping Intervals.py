'''Given a 2D array intervals[][] of representing intervals where intervals [i] = [starti, endi ]. Return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Examples:

Input: intervals[][] = [[1, 2], [2, 3], [3, 4], [1, 3]]
Output: 1
Explanation: [1, 3] can be removed and the rest of the intervals are non-overlapping.
Input: intervals[][] = [[1, 3], [1, 3], [1, 3]]
Output: 2
Explanation: You need to remove two [1, 3] to make the rest of the intervals non-overlapping.
Input: intervals[][] = [[1, 2], [5, 10], [18, 35], [40, 45]]
Output: 0
Explanation: All ranges are already non overlapping.'''
class Solution:
    def minRemoval(self, intervals):
        # If the intervals list is empty, no removal is needed
        if not intervals:
            return 0

        # Step 1: Sort intervals based on their end time
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize variables
        end = float('-inf')  # The end of the last interval selected
        removals = 0  # Number of intervals to remove

        # Step 3: Iterate over the intervals
        for interval in intervals:
            if interval[0] < end:
                # If the current interval overlaps with the last selected interval
                removals += 1
            else:
                # If there's no overlap, update the end
                end = interval[1]

        return removals