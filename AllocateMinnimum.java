class Solution {
    public static int findPages(int[] arr, int k) {
        int n = arr.length;

        // If number of students is greater than number of books
        if (k > n) {
            return -1;
        }

        // Initialize binary search bounds
        int low = 0; // Minimum pages a student can take (0 is not valid, but we will set it to max later)
        int high = 0; // Maximum pages a student can take (sum of all pages)
        
        for (int pages : arr) {
            high += pages; // Total pages
            low = Math.max(low, pages); // Maximum single book pages
        }

        int result = high; // Initialize result to the maximum possible value

        // Binary search for the minimum possible maximum pages
        while (low <= high) {
            int mid = (low + high) / 2;

            if (canAllocate(arr, n, k, mid)) {
                result = mid; // Found a valid allocation, try for a smaller max
                high = mid - 1;
            } else {
                low = mid + 1; // Increase the max pages since allocation failed
            }
        }

        return result;
    }

    // Helper function to check if allocation is possible
    private static boolean canAllocate(int[] arr, int n, int k, int maxPages) {
        int studentCount = 1; // Start with one student
        int currentPages = 0; // Pages assigned to the current student

        for (int pages : arr) {
            // If adding this book exceeds maxPages, allocate to the next student
            if (currentPages + pages > maxPages) {
                studentCount++;
                currentPages = pages; // Start new student with this book
                if (studentCount > k) {
                    return false; // More students needed than available
                }
            } else {
                currentPages += pages; // Add pages to current student
            }
        }

        return true; // Allocation is possible
    }
}