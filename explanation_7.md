HTTPRouter using a Trie

- Design
    - We use trie to store data and handle all the queries.
- Time Complexity
    - The time complexity of inserting and searching is equal to the length of
      the word. If there are n words with each having length l then the total
      time complexity would be O(n * l).
    - Method - RouteTrie.insert
        - Time Complexity - O(l) where l is the length of the path
        - Space Complexity - O(l) where l is the length of the path
    - Method - RouteTrie.find
        - Time Complexity - O(l) where l is the length of the path
        - Space Complexity - O(1)
    - Method - Router.add_handler
        - Time Complexity - O(l) where l is the length of the path
        - Space Complexity - O(l) where l is the length of the path
    - Method - Router.lookup
        - Time Complexity - O(l) where l is the length of the path
        - Space Complexity - O(1)
- Space Complexity
    - In the worse case if all the words have no common characters then we would
      need to create a node for all the characters which would lead to a space
      complexity of O(n * l).