class Solution {
    public int findMin(int[] arr) {
        int left = 0, right = arr.length - 1;

        while (left < right) {
            int mid = (left + right) / 2;

            // If mid element is greater than right element,
            // then the minimum is in the right half
            if (arr[mid] > arr[right]) {
                left = mid + 1;
            } else {
                // Otherwise, the minimum is in the left half
                right = mid;
            }
        }

        // When left == right, we have found the minimum element
        return arr[left];
    }
}