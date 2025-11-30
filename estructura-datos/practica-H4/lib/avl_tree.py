from lib.binary_search_tree import TreeMap

class AVLTreeMap(TreeMap):
  """Sorted map implementation using an AVL tree."""

  #-------------------------- nested Node class --------------------------
  class Node(TreeMap.Node):
    """Node class for AVL maintains height value for balancing.

    We use convention that a "None" child has height 0, thus a leaf has height 1.
    """
    __slots__ = '_height'         # additional data member to store height

    def __init__(self, element, parent=None, left=None, right=None):
      super().__init__(element, parent, left, right)
      self._height = 0            # will be recomputed during balancing
      
    def left_height(self):
      return self._left._height if self._left is not None else 0

    def right_height(self):
      return self._right._height if self._right is not None else 0

  #------------------------- positional-based utility methods -------------------------
  def _recompute_height(self, node):
    node._height = 1 + max(node.left_height(), node.right_height())

  def _isbalanced(self, node):
    return abs(node.left_height() - node.right_height()) <= 1

  def _tall_child(self, node, favorleft=False): # parameter controls tiebreaker
    if node.left_height() + (1 if favorleft else 0) > node.right_height():
      return self.left(node)
    else:
      return self.right(node)

  def _tall_grandchild(self, node):
    child = self._tall_child(node)
    # if child is on left, favor left grandchild; else favor right grandchild
    alignment = (child == self.left(node))
    return self._tall_child(child, alignment)

  def _rebalance(self, node):
    while node is not None:
      old_height = node._height                          # trivially 0 if new node
      if not self._isbalanced(node):                           # imbalance detected!
        # perform trinode restructuring, setting node to resulting root,
        # and recompute new local heights after the restructuring
        node = self._restructure(self._tall_grandchild(node))
        self._recompute_height(self.left(node))                
        self._recompute_height(self.right(node))                           
      self._recompute_height(node)                             # adjust for recent changes
      if node._height == old_height:                     # has height changed?
        node = None                                            # no further changes needed
      else:
        node = self.parent(node)                                  # repeat with parent

  #---------------------------- override balancing hooks ----------------------------
  def _rebalance_insert(self, node):
    self._rebalance(node)

  def _rebalance_delete(self, node):
    self._rebalance(node)