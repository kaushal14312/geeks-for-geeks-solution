class Solution {
    // Function to merge the arrays.
    public void mergeArrays(int a[], int b[]) {
        int n = a.length;
        int m = b.length;

        // Start from the end of both arrays
        int i = n - 1; // Pointer for array a
        int j = 0;     // Pointer for array b

        // Move elements of a[] to the end of a[] to make space for merging
        while (i >= 0 && j < m) {
            if (a[i] > b[j]) {
                // If the current element of a is greater than the current element of b
                // Swap them
                int temp = a[i];
                a[i] = b[j];
                b[j] = temp;
            }
            i--;
            j++;
        }

        // Sort the first n elements of a[]
        Arrays.sort(a);
        // Sort the last m elements of b[]
        Arrays.sort(b);
    }
}
