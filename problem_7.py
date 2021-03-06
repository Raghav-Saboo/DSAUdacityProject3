# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
  def __init__(self):
    self.children = {}
    self.handler = None

  # Initialize the node with children as before, plus a handler

  def insert(self, path):
    if path not in self.children:
      self.children[path] = RouteTrieNode()


# Insert the node as before

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
  def __init__(self, root_handler):
    self.root = RouteTrieNode()
    self.root.handler = root_handler

  # Initialize the trie with an root node and a handler, this is the root path or home page node

  def insert(self, path, handler):
    node = self.root
    for sub_path in path:
      if sub_path not in node.children:
        node.children[sub_path] = RouteTrieNode()
      node = node.children[sub_path]
    node.handler = handler

  # Similar to our previous example you will want to recursively add nodes
  # Make sure you assign the handler to only the leaf (deepest) node of this path

  def find(self, path):
    node = self.root
    for sub_path in path:
      if sub_path not in node.children:
        return None
      node = node.children[sub_path]
    return node.handler


# The Router class will wrap the Trie and handle
class Router:
  def __init__(self, root_handler, not_found_handler):
    self.trie = RouteTrie(root_handler)
    self.root_handler = root_handler
    self.not_found_handler = not_found_handler

  # Create a new RouteTrie for holding our routes
  # You could also add a handler for 404 page not found responses as well!

  def add_handler(self, path, handler):
    parsed_path = self.split_path(path)
    self.trie.insert(parsed_path, handler)

  # Add a handler for a path
  # You will need to split the path and pass the pass parts
  # as a list to the RouteTrie

  def lookup(self, path):
    parsed_path = self.split_path(path)
    handler = self.trie.find(parsed_path)
    return self.not_found_handler if handler is None else handler

  # lookup path (by parts) and return the associated handler
  # you can return None if it's not found or
  # return the "not found" handler if you added one
  # bonus points if a path works with and without a trailing slash
  # e.g. /about and /about/ both return the /about handler

  def split_path(self, path):
    path_elements = path.split('/')
    return [ele for ele in path_elements if len(ele) > 0]


# you need to split the path into parts for
# both the add_handler and loopup functions,
# so it should be placed in a function here

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler",
                "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup(
    "/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup(
    "/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup(
    "/home/about/me"))  # should print 'not found handler' or None if you did not implement one
