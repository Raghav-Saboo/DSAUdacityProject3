Search in a Rotated Sorted Array

- Design
    - To find the pivot index we can apply binary search as if the middle
      element is smaller than the first element we know that this element is
      part of the second array and vice versa. After finding the pivot index we
      can apply binary search on the two sorted arrays.
- Time Complexity
    - O(log(n)) where n is the number of elements in the array.
- Space Complexity
    - O(1)