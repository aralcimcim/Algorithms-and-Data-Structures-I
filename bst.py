from typing import Any, Generator, Tuple

from tree_node import TreeNode


class BinarySearchTree:
    """Binary-Search-Tree implemented for didactic reasons."""

    def __init__(self, root: TreeNode = None):
        """Initialize BinarySearchTree.

        Args:
            root (TreeNode, optional): Root of the BST. Defaults to None.
        
        Raises:
            ValueError: root is neither a TreeNode nor None.
        """
        self._root = root
        self._size = 0 if root is None else 1
        self._num_of_comparisons = 0

    def insert(self, key: int, value: Any) -> None:
        """Insert a new node into BST.

        Args:
            key (int): Key which is used for placing the value into the tree.
            value (Any): Value to insert.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is already present in the tree.
        """
        #pass
        # TODO
        if not isinstance(key, int):
            raise ValueError("Key must be integer")
        
        if self._root is None:
            self._root = TreeNode(key, value)
        else:
            node = self._root
            prev_node = self._root

            while node is not None:
                if key == node.key:
                    raise KeyError("Key is already present in tree")
                
                prev_node = node
                if key < node.key:
                    node = node.left
                else:
                    node = node.right
            if prev_node.key < key:
                prev_node.right = TreeNode(key, value, parent=prev_node)
            else:
                prev_node.left = TreeNode(key, value, parent=prev_node)
        self._size += 1


    def find(self, key: int) -> TreeNode:
        """Return node with given key.

        Args:
            key (int): Key of node.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            TreeNode: Node
        """
        # pass
        # TODO

        if not isinstance(key, int):
            raise ValueError("Key must be integer")
        
        if self._root is None:
            raise KeyError("Key not present in tree")
        
        else:
            node = self._root
            while node is not None and node.key is not key:
                if key < node.key:
                    node = node.left
                else:
                    node = node.right
            if node is None:
                raise KeyError("Key not present in the tree")
            else:
                return node

    @property
    def size(self) -> int:
        """Return number of nodes contained in the tree."""
        # pass
        # TODO
        return self._size

    # If users instead call `len(tree)`, this makes it return the same as `tree.size`
    __len__ = size 

    # This is what gets called when you call e.g. `tree[5]`
    def __getitem__(self, key: int) -> Any:
        """Return value of node with given key.

        Args:
            key (int): Key to look for.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.

        Returns:
            Any: [description]
        """
        return self.find(key).value

    def remove(self, key: int) -> None:
        """Remove node with given key, maintaining BST-properties.

        Args:
            key (int): Key of node which should be deleted.

        Raises:
            ValueError: If key is not an integer.
            KeyError: If key is not present in the tree.
        """
        # pass
        # TODO
        if not isinstance(key, int):
            raise ValueError("Key must be an integer")
        
        if self._root is None:
            raise KeyError("Key not present in tree")
        
        key_finder = self.find(key)
        if key_finder.left is None and key_finder.right is None:
            if key_finder == key_finder.parent.left:
                key_finder.parent.left = None
            else:
                key_finder.parent.right = None

        elif key_finder.left is None:
            if key_finder == key_finder.parent.left:
                key_finder.parent.left = key_finder.right
            else:
                key_finder.parent.right = key_finder.right

        elif key_finder.right is None:
            if key_finder == key_finder.parent.left:
                key_finder.parent.left = key_finder.left
            else:
                key_finder.parent.right = key_finder.left

        else:
            node = key_finder.right
            while node.left is not None:
                node = node.left
            key_finder.key = node.key
            key_finder.value = node.value

            if node == node.parent.left:
                node.parent.left = node.right
            else:
                node.parent.right = node.right

        self._size -= 1

    # Hint: The following 3 methods can be implemented recursively, and 
    # the keyword `yield from` might be extremely useful here:
    # http://simeonvisser.com/posts/python-3-using-yield-from-in-generators-part-1.html

    # Also, we use a small syntactic sugar here: 
    # https://www.pythoninformer.com/python-language/intermediate-python/short-circuit-evaluation/

    def inorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in inorder."""
        node = node or self._root
        # This is needed in the case that there are no nodes.
        if not node:
            return iter(())
        yield from self._inorder(node)

    def preorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in preorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._preorder(node)

    def postorder(self, node: TreeNode = None) -> Generator[TreeNode, None, None]:
        """Yield nodes in postorder."""
        node = node or self._root
        if not node:
            return iter(())
        yield from self._postorder(node)

    # this allows for e.g. `for node in tree`, or `list(tree)`.
    def __iter__(self) -> Generator[TreeNode, None, None]: 
        yield from self._preorder(self._root)

    @property
    def is_valid(self, node: TreeNode = None, lower_bound = float('-inf'), upper_bound = float('inf')) -> bool:
        """Return if the tree fulfills BST-criteria."""
        # pass
        # TODO

        if not node:
            return True
        
        value = node.key
        if value < lower_bound or value > upper_bound:
            return False
        
        if not self.is_valid(node.right, value, upper_bound):
            return False
        if not self.is_valid(node.left, lower_bound, value):
            return False
        
        return True
    
    def check_valid(self, node):
        if node is None:
            return True
        if node.left is not None:
            if node.left.key > node.key or node.left.key > self.return_max_key(node.left).key:
                return False
            
        if node.right is not None:
            if node.right.key < node.key or node.right.key < self.return_min_key(node.right).key:
                return False
            
        return self.check_valid(node.left) and self.check_valid(node.right)

    def return_max_key(self, node) -> TreeNode:
        """Return the node with the largest key (None if tree is empty)."""
        # pass

        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node
            
    def return_min_key(self, node: TreeNode = None) -> TreeNode:

        node = node or self._root
        if node is None:
            return None
        while node.left is not None:
            node = node.left
        return node

    def find_comparison(self, key: int) -> Tuple[int, int]:
        """Create an inbuilt python list of BST values in preorder and compute the number of comparisons needed for
           finding the key both in the list and in the BST.
           Return the numbers of comparisons for both, the list and the BST
        """
        python_list = list(node.key for node in self._preorder(self._root))
        # TODO

        comp_count = 0
        for node_key in python_list:
            comp_count += 1
            if node_key == key:
                break

        bst_count = 0
        current_node = self._root
        while current_node is not None:
            bst_count += 1
            if current_node.key == key:
                break
            elif current_node.key < key:
                current_node = current_node.right
            else:
                current_node = current_node.left

        return comp_count, bst_count
        
    def __repr__(self) -> str:
        return f"BinarySearchTree({list(self._inorder(self._root))})"

    ####################################################
    # Helper Functions
    ####################################################

    def get_root(self):
        return self._root

    def _inorder(self, current_node):
        # pass
        # TODO
        if current_node is not None:
            yield from self._inorder(current_node.left)
            yield current_node
            yield from self._inorder(current_node.right)

    def _preorder(self, current_node):
        # pass
        # TODO
        if current_node is not None:
            yield current_node
            yield from self._preorder(current_node.left)
            yield from self._preorder(current_node.right)

    def _postorder(self, current_node):
        # pass
        # TODO
        if current_node is not None:
            yield from self._postorder(current_node.left)
            yield from self._postorder(current_node.right)
            yield current_node

    # You can of course add your own methods and/or functions!
    # (A method is within a class, a function outside of it.)

    def print_tree(self, node: TreeNode = None, level=0):
        if node is not None:
            print("  " * level + str(node.key))
            self.print_tree(node.left, level + 1)
            self.print_tree(node.right, level + 1)
