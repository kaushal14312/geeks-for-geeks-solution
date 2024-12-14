class Solution {
    int search(int[] arr, int key) {
        int left = 0, right = arr.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            // Check if the mid element is the key
            if (arr[mid] == key) {
                return mid;
            }

            // Check if the left half is sorted
            if (arr[left] <= arr[mid]) {
                // Check if the key is in the left half
                if (arr[left] <= key && key < arr[mid]) {
                    right = mid - 1; // Search in the left half
                } else {
                    left = mid + 1;  // Search in the right half
                }
            } else {
                // The right half must be sorted
                // Check if the key is in the right half
                if (arr[mid] < key && key <= arr[right]) {
                    left = mid + 1;  // Search in the right half
                } else {
                    right = mid - 1; // Search in the left half
                }
            }
        }

        return -1; // Key not found
    }
}