"Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 

Examples :

Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 2
Output: 4
Explanation: target = 2 occurs 4 times in the given array so the output is 4.
Input: arr[] = [1, 1, 2, 2, 2, 2, 3], target = 4
Output: 0
Explanation: target = 4 is not present in the given array so the output is 0.
Input: arr[] = [8, 9, 10, 12, 12, 12], target = 12
Output: 3
Explanation: target = 12 occurs 3 times in the given array so the output is 3.
Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i] ≤ 106
1 ≤ target ≤ 106"
class Solution {
    int countFreq(int[] arr, int target) {
        int firstIndex = findFirstOccurrence(arr, target);
        if (firstIndex == -1) {
            return 0; // Target not found
        }
        int lastIndex = findLastOccurrence(arr, target);
        return lastIndex - firstIndex + 1; // Count of occurrences
    }

    private int findFirstOccurrence(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        int firstIndex = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                firstIndex = mid; // Found target, look for earlier occurrences
                right = mid - 1;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return firstIndex;
    }

    private int findLastOccurrence(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        int lastIndex = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr[mid] == target) {
                lastIndex = mid; // Found target, look for later occurrences
                left = mid + 1;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return lastIndex;
    }
}