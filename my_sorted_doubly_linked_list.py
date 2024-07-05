from my_list_node import MyListNode

class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    # The following methods have to be implemented.

    def get_value(self, index: int) -> int:
        """Return the value (elem) at position 'index' without removing the node.

        Args:
            index (int): 0 <= index < length of list

        Returns:
            (int): Retrieved value.

        Raises:
            ValueError: If the passed index is not an int or out of range.
        """
        # TODO

        if not isinstance(index, int) or index < 0 or index >= self._size:
            raise ValueError("The index is either not an int or out of range")
        
        if self._head is None:
            raise ValueError("The list is empty")

        current_node = self._head

        for i in range(index):
            current_node = current_node.next_node

        return current_node.elem

    def search_value(self, val: int) -> int:
        """Return the index of the first occurrence of 'val' in the list.

        Args:
            val (int): Value to be searched.

        Returns:
            (int): Retrieved index.

        Raises:
            ValueError: If val is not an int.
        """

        if not isinstance(val, int):
            raise ValueError("Val. is not an int.")
        
        index = 0
        current_node = self._head
        while current_node:
            if current_node.elem == val:
                return index
            current_node = current_node.next_node
            index += 1

        return -1


    def insert(self, val: int) -> None:
        """Add a new node containing 'val' to the list, keeping the list in ascending order.

        Args:
            val (int): Value to be added.

        Raises:
            ValueError: If val is not an int.
        """
        
        if not isinstance(val, int):
            raise ValueError("Val. is not an int.")
        
        new_node = MyListNode(val)

        if self._head is None:
            self._head = self._tail = new_node
        
        elif val < self._head.elem:
            new_node.next_node = self._head
            self._head.prev_node = new_node
            self._head = new_node
        
        else:
            current_node = self._head
            while current_node.next_node and current_node.next_node.elem < val:
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            new_node.prev_node = current_node

            if current_node.next_node:
                current_node.next_node.prev_node = new_node
            else:
                self._tail = new_node
            current_node.next_node = new_node

        self._size += 1 

    def remove_first(self, val: int) -> bool:
        """Remove the first occurrence of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether an element was successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        if not isinstance(val, int):
            raise ValueError("Val. is not an int.")
        
        current_node = self._head

        while current_node:
            if current_node.elem == val:
                if current_node.prev_node:
                    current_node.prev_node.next_node = current_node.next_node
                else:
                    self._head = current_node.next_node
                
                if current_node.next_node:
                    current_node.next_node.prev_node = current_node.prev_node
                else:
                    self._tail = current_node.prev_node
                self._size -= 1

                return True
            
            current_node = current_node.next_node

        return False

    def remove_all(self, val: int) -> bool:
        """Remove all occurrences of the parameter 'val'.

        Args:
            val (int): Value to be removed.

        Returns:
            (bool): Whether elements were successfully removed or not.

        Raises:
            ValueError: If val is not an int.
        """
        
        if not isinstance(val, int):
            raise ValueError("Val. is not an int.")
        
        remove_node = False
        while self.remove_first(val):
            remove_node = True

        if remove_node:
            return True
        
        else:
            return False

    def remove_duplicates(self) -> None:
        """Remove all duplicate occurrences of values from the list."""
        
        current_node = self._head

        while current_node:
            while current_node.next_node and current_node.elem == current_node.next_node.elem:
                current_node.next_node = current_node.next_node.next_node
                if current_node.next_node:
                    current_node.next_node.prev_node = current_node
                else:
                    self._tail = current_node
                self._size -= 1
            current_node = current_node.next_node

    def filter_n_max(self, n: int) -> None:
        """Filter the list to only contain the 'n' highest values.

        Args:
            n (int): 0 < n <= length of list

        Raises:
            ValueError: If the passed value n is not an int or out of range.
        """
        
        if not isinstance(n, int) or n <= 0 or n > self._size:
            raise ValueError("Either n is not an int or n is out of range.")
        
        while self._size > n:
            self._head = self._head.next_node
            self._head.prev_node = None
            self._size -= 1

    def filter_odd(self) -> None:
        """Filter the list to only contain odd values."""
        
        current_node = self._head
        while current_node:
            next_node = current_node.next_node

            if current_node.elem % 2 == 0:
                self.remove_first(current_node.elem)

            current_node = next_node

    def filter_even(self) -> None:
        """Filter the list to only contain even values."""

        current_node = self._head
        while current_node:
            next_node = current_node.next_node

            if current_node.elem % 2 != 0:
                self.remove_first(current_node.elem)

            current_node = next_node

