Square Root of an Integer

- Design
    - In this problem we can use binary search to find the floored square root
      since we can divide the whole search space (0, n) into two halves
      depending on the square of the middle value. If mid * mid > n then we know
      the answer should be smaller than mid and vice versa.
- Time Complexity
    - O(log(n))
- Space Complexity
    - O(1)
