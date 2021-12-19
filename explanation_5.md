Autocomplete with Tries

- Design
    - We implement all the basic methods of a Trie.
- Time Complexity
    - The time complexity of inserting and searching is equal to the length of
      the word. If there are n words with each having length l then the total
      time complexity would be O(n * l).
- Space Complexity
    - In the worse case if all the words have no common characters then we would
      need to create a node for all the characters which would lead to a space
      complexity of O(n * l).