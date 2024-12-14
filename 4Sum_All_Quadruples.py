'''Given an array arr of integers and another number k. Find all the unique quadruples from the given array that sum up to k.

Note: All the quadruples which you return should be internally sorted, ie for any quadruple [q1, q2, q3, q4] the following should follow: q1 <= q2 <= q3 <= q4.

Examples :

Input: arr[] = [0, 0, 2, 1, 1], k = 3
Output: [0, 0, 1, 2] 
Explanation: Sum of 0, 0, 1, 2 is equal to k.
Input: arr[] = [10, 2, 3, 4, 5, 7, 8], k = 23
Output: [[2, 3, 8, 10],[2, 4, 7, 10],[3, 5, 7, 8]] 
Explanation: Sum of 2, 3, 8, 10 = 23, sum of 2, 4, 7, 10 = 23 and sum of 3, 5, 7, 8 = 23.
Input: arr[] = [0, 0, 2, 1, 1], k = 2
Output: [0, 0, 1, 1] 
Explanation: Sum of 0, 0, 1, 2 is equal to k.
Constraints:
1 <= arr.size() <= 100
-1000 <= k <= 1000
-100 <= arr[i] <= 100'''

class Solution:
    def fourSum(self, arr, k):
        arr.sort()  # Sort the array
        n = len(arr)
        quadruples = set()  # Use a set to avoid duplicates

        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and arr[i] == arr[i - 1]:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]
                    if total == k:
                        # Found a quadruple
                        quadruples.add((arr[i], arr[j], arr[left], arr[right]))
                        left += 1
                        right -= 1
                        # Skip duplicates for the third number
                        while left < right and arr[left] == arr[left - 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and arr[right] == arr[right + 1]:
                            right -= 1
                    elif total < k:
                        left += 1
                    else:
                        right -= 1

        # Convert set of tuples to a list of lists and sort each quadruple
        return [list(quad) for quad in sorted(quadruples)]
