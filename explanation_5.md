Autocomplete with Tries

- Design
    - We implement all the basic methods of a Trie.
- Time Complexity
    - The time complexity of inserting and searching is equal to the length of
      the word. If there are n words with each having length l then the total
      time complexity would be O(n * l).
    - Method - Trie.insert
        - Time Complexity - O(l) where l is the length of the word
    - Method - Trie.find
        - Time Complexity - O(l) where l is the length of the word
    - Method - TrieNode.insert
        - Time Complexity - O(1)
    - Method - TrieNode.suffixes
        - Time Complexity - O(l * n) where l is the length of each word and n is
          the total number of words
- Space Complexity
    - In the worse case if all the words have no common characters then we would
      need to create a node for all the characters which would lead to a space
      complexity of O(n * l).
    - Method - Trie.insert
        - Space Complexity - O(l) where l is the length of the word
    - Method - Trie.find
        - Time Complexity - O(l) where l is the length of the word
    - Method - TrieNode.insert
        - Space Complexity - O(1)
    - Method - TrieNode.suffixes
        - Space Complexity - O(l * n) where l is the length of each word and n
          is the total number of words