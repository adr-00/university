from lib.linked_binary_tree import LinkedBinaryTree

class TreeMap(LinkedBinaryTree):
  """Sorted map implementation using a binary search tree."""

  #---------------------------- override Node class ----------------------------
  class Node(LinkedBinaryTree.Node):
    def key(self):
      """Return key of map's key-value pair."""
      return self.element()._key
    def value(self):
      """Return value of map's key-value pair."""
      return self.element()._value

  #------------------------------- nonpublic utilities -------------------------------
  def _subtree_search(self, node, k):
    """Return Node of node's subtree having key k, or last node searched."""
    if k == node.key():                                   # found match
      return node                                         
    elif k < node.key():                                  # search left subtree
      if self.left(node) is not None:
        return self._subtree_search(self.left(node), k)   
    else:                                              # search right subtree
      if self.right(node) is not None:
        return self._subtree_search(self.right(node), k)
    return node                                           # unsucessful search

  def _subtree_first_position(self, node):
    """Return Node of first item in subtree rooted at node."""
    walk = node
    while self.left(walk) is not None:                 # keep walking left
      walk = self.left(walk)
    return walk

  def _subtree_last_position(self, node):
    """Return Node of last item in subtree rooted at node."""
    walk = node
    while self.right(walk) is not None:                # keep walking right
      walk = self.right(walk)
    return walk
  
  #--------------------- public methods providing "positional" support ---------------------
  def first(self):
    """Return the first Node in the tree (or None if empty)."""
    return self._subtree_first_position(self.root()) if len(self) > 0 else None

  def last(self):
    """Return the last Node in the tree (or None if empty)."""
    return self._subtree_last_position(self.root()) if len(self) > 0 else None

  def before(self, node):
    """Return the Node just before node in the natural order.

    Return None if node is in the first position.
    """
    if self.left(node):
      return self._subtree_last_position(self.left(node))
    else:
      # walk upward
      walk = node
      above = self.parent(walk)
      while above is not None and walk is self.left(above):
        walk = above
        above = self.parent(walk)
      return above

  def after(self, node):
    """Return the Node just after node in the natural order.

    Return None if node is in the last position.
    """
    if self.right(node):
      return self._subtree_first_position(self.right(node))
    else:
      walk = node
      above = self.parent(walk)
      while above is not None and walk is self.right(above):
        walk = above
        above = self.parent(walk)
      return above

  def find_node(self, k):
    """Return position with key k, or else neighbor (or None if empty)."""
    if self.is_empty():
      return None
    else:
      node = self._subtree_search(self.root(), k)
      return node

  def _delete(self, node):
    """Remove the item at given Position."""
    if self.left(node) and self.right(node):           # node has two children
      replacement = self._subtree_last_position(self.left(node))
      self.replace(node, replacement.element())    # from LinkedBinaryTree
      node = replacement
    # now p has at most one child
    parent = self.parent(node)
    self.delete(node)                              # inherited from LinkedBinaryTree
    self._rebalance_delete(parent)               # if root deleted, parent is None
      
  #--------------------- public methods for (standard) map interface ---------------------

  class _Item:
    def __init__(self, k, v):
      self._key = k
      self._value = v

    def __eq__(self, other):
      return self._key == other._key

    def __ne__(self, other):
      return not (self == other)

    def __lt__(self, other):
      return self._key < other._key

    def __str__(self):
      return '(' + str(self._key) + ',' + str(self._value) + ')'

  def __getitem__(self, k):
    """Return value associated with key k (raise KeyError if not found)."""
    if self.is_empty():
      raise KeyError('Key Error: ' + repr(k))
    else:
      node = self._subtree_search(self.root(), k)
      if k != node.key():
        raise KeyError('Key Error: ' + repr(k))
      return node.value()

  def __setitem__(self, k, v):
    """Assign value v to key k, overwriting existing value if present."""
    if self.is_empty():
      leaf = self.add_root(self._Item(k,v))     # from LinkedBinaryTree
    else:
      node = self._subtree_search(self.root(), k)
      if node.key() == k:
        node.element()._value = v                   # replace existing item's value
        return
      else:
        item = self._Item(k,v)
        if node.key() < k:
          leaf = self.add_right(node, item)        # inherited from LinkedBinaryTree
        else:
          leaf = self.add_left(node, item)         # inherited from LinkedBinaryTree
    self._rebalance_insert(leaf)                 # hook for balanced tree subclasses

  def __delitem__(self, k):
    """Remove item associated with key k (raise KeyError if not found)."""
    if not self.is_empty():
      node = self._subtree_search(self.root(), k)
      if k == node.key():
        self._delete(node)                           # rely on positional version
        return                                   # successful deletion complete
    raise KeyError('Key Error: ' + repr(k))

  def __iter__(self):
    """Generate an iteration of all keys in the map in order."""
    node = self.first()
    while node is not None:
      yield node.key()
      node = self.after(node)

  #--------------------- public methods for sorted map interface ---------------------
  def __reversed__(self):
    """Generate an iteration of all keys in the map in reverse order."""
    node = self.last()
    while node is not None:
      yield node.key()
      node = self.before(node)

  def find_min(self):
    """Return (key,value) pair with minimum key (or None if empty)."""
    if self.is_empty():
      return None
    else:
      node = self.first()
      return (node.key(), node.value()) if node is not None else None

  def find_max(self):
    """Return (key,value) pair with maximum key (or None if empty)."""
    if self.is_empty():
      return None
    else:
      node = self.last()
      return (node.key(), node.value()) if node is not None else None

  def find_le(self, k):
    """Return (key,value) pair with greatest key less than or equal to k.

    Return None if there does not exist such a key.
    """
    if self.is_empty():
      return None
    else:
      node = self.find_node(k)
      if node is not None and k < node.key():
        node = self.before(node)
      return (node.key(), node.value()) if node is not None else None

  def find_lt(self, k):
    """Return (key,value) pair with greatest key strictly less than k.

    Return None if there does not exist such a key.
    """
    if self.is_empty():
      return None
    else:
      node = self.find_node(k)
      if node is not None and not node.key() < k:
        node = self.before(node)
      return (node.key(), node.value()) if node is not None else None

  def find_ge(self, k):
    """Return (key,value) pair with least key greater than or equal to k.

    Return None if there does not exist such a key.
    """
    if self.is_empty():
      return None
    else:
      node = self.find_node(k)                   # may not find exact match
      if node is not None and node.key() < k:                             # node's key is too small
        node = self.after(node)
      return (node.key(), node.value()) if node is not None else None

  def find_gt(self, k):
    """Return (key,value) pair with least key strictly greater than k.

    Return None if there does not exist such a key.
    """
    if self.is_empty():
      return None
    else:
      node = self.find_node(k)
      if node is not None and not k < node.key():                   
        node = self.after(node)
      return (node.key(), node.value()) if node is not None else None
  
  def find_range(self, start, stop):
    """Iterate all (key,value) pairs such that start <= key < stop.

    If start is None, iteration begins with minimum key of map.
    If stop is None, iteration continues through the maximum key of map.
    """
    if not self.is_empty():
      if start is None:
        node = self.first()
      else:
        # we initialize node with logic similar to find_ge
        node = self.find_node(start)
        if node is not None and node.key() < start:
          node = self.after(node)
      while node is not None and (stop is None or node.key() < stop):
        yield (node.key(), node.value())
        node = self.after(node)

  #--------------------- hooks used by subclasses to balance a tree ---------------------
  def _rebalance_insert(self, node):
    """Call to indicate that node is newly added."""
    pass

  def _rebalance_delete(self, node):
    """Call to indicate that a child of node has been removed."""
    pass

  #--------------------- nonpublic methods to support tree balancing ---------------------

  def _relink(self, parent, child, make_left_child):
    """Relink parent node with child node (we allow child to be None)."""
    if make_left_child:                           # make it a left child
      parent._left = child
    else:                                         # make it a right child
      parent._right = child
    if child is not None:                         # make child point to parent
      child._parent = parent

  def _rotate(self, node):
    """Rotate node above its parent.

    Switches between these configurations, depending on whether node==a or node==b.

          b                  a
         / \                /  \
        a  t2             t0   b
       / \                     / \
      t0  t1                  t1  t2

    Caller should ensure that node is not the root.
    """
    """Rotate node above its parent."""
    x = node
    y = x._parent                                 # we assume this exists
    z = y._parent                                 # grandparent (possibly None)
    if z is None:            
      self._root = x                              # x becomes root
      x._parent = None        
    else:
      self._relink(z, x, y == z._left)            # x becomes a direct child of z
    # now rotate x and y, including transfer of middle subtree
    if x == y._left:
      self._relink(y, x._right, True)             # x._right becomes left child of y
      self._relink(x, y, False)                   # y becomes right child of x
    else:
      self._relink(y, x._left, False)             # x._left becomes right child of y
      self._relink(x, y, True)                    # y becomes left child of x

  def _restructure(self, x):
    """Perform a trinode restructure among Position x, its parent, and its grandparent.

    Return the Node that becomes root of the restructured subtree.

    Assumes the nodes are in one of the following configurations:

        z=a                 z=c           z=a               z=c  
       /  \                /  \          /  \              /  \  
      t0  y=b             y=b  t3       t0   y=c          y=a  t3 
         /  \            /  \               /  \         /  \     
        t1  x=c         x=a  t2            x=b  t3      t0   x=b    
           /  \        /  \               /  \              /  \    
          t2  t3      t0  t1             t1  t2            t1  t2   

    The subtree will be restructured so that the node with key b becomes its root.

              b
            /   \
          a       c
         / \     / \
        t0  t1  t2  t3

    Caller should ensure that x has a grandparent.
    """
    """Perform trinode restructure of Position x with parent/grandparent."""
    y = self.parent(x)
    z = self.parent(y)
    if (x == self.right(y)) == (y == self.right(z)):  # matching alignments
      self._rotate(y)                                 # single rotation (of y)
      return y                                        # y is new subtree root
    else:                                             # opposite alignments
      self._rotate(x)                                 # double rotation (of x)     
      self._rotate(x)
      return x                                        # x is new subtree root
