from typing import Optional


class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = len(self.heap)

    def get_size(self) -> int:
        """
        @return number of elements in the min heap
        """
        return self.size

    def is_empty(self) -> bool:
        """
        @return True if the min heap is empty, False otherwise
        """
        # TODO
        if self.size == 0:
            return True
        else:
            return False

    def insert(self, integer_val: int) -> None:
        """
        inserts integer_val into the min heap
        @param integer_val: the value to be inserted
        @raises ValueError if integer_val is None or not an int
        """
        # TODO
        if integer_val is None or not isinstance(integer_val, int):
            raise ValueError("integer_val is None or not an int")
        
        self.heap.append(integer_val)
        self.size += 1
        self.up_heap(self.size - 1)

    def get_min(self) -> Optional[int]:
        """
        returns the value of the minimum element of the PQ without removing it
        @return the minimum value of the PQ or None if no element exists
        """
        # TODO
        if self.size == 0:
            return None
        else:
            return self.heap[0]

    def remove_min(self) -> Optional[int]:
        """
        removes the minimum element from the PQ and returns its value
        @return the value of the removed element or None if no element exists
        """
        # TODO
        if self.size == 0:
            return None
        else:
            min_val = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.heap.pop()
            self.size -= 1
            self.down_heap(0)
            return min_val
        
    def parent(self, index: int) -> int:
        return (index - 1) // 2
    
    def left_child(self, index: int) -> int:
        return 2 * index + 1
    
    def right_child(self, index: int) -> int:
        return 2 * index + 2
    
    def swap(self, index1: int, index2: int) -> None:
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def up_heap(self, index: int) -> None:
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def down_heap(self, index: int) -> None:

        #min([(index, self.heap[index])
        smallest = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < self.size and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < self.size and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.swap(index, smallest)
            self.down_heap(smallest)

