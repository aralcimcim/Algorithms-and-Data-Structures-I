class MaxHeap:
    def __init__(self, input_array):
        """
        @param input_array from which the heap should be created
        @raises ValueError if list is None.
        Creates a bottom-up max heap in place.
        """
        if input_array is None:
            raise ValueError("Input array (list) is None.")
        
        self.heap = input_array
        self.size = len(input_array)
        self.last_elem = self.size // 2 - 1

        for i in range(self.last_elem, -1, -1):
            self.heapify(i)

    def get_heap(self):
        # helper function for testing, do not change
        return self.heap

    def get_size(self):
        """
        @return size of the max heap
        """
        return self.size

    def contains(self, val):
        """
        @param val to check if it is contained in the max heap
        @return True if val is contained in the heap else False
        @raises ValueError if val is None.
        Tests if an item (val) is contained in the heap. Does not search the entire array sequentially, but uses the
        properties of a heap.
        """
        # TODO
        if val is None:
            raise ValueError("Container value is None.")

        s_root = [0]
        while s_root:
            idx = s_root.pop()
            if self.heap[idx] == val:
                return True
            left_child = self.left_child(idx)
            right_child = self.right_child(idx)
    
            if left_child < self.size:
                s_root.append(left_child)
            if right_child < self.size:
                s_root.append(right_child)

        return False
        
    def sort(self):
        """
        This method sorts (ascending) the list in-place using HeapSort, e.g. [1,3,5,7,8,9]
        """
        # TODO
        for i in range(self.size - 1, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            self.size -= 1
            self.down_heap(0)
    
    def remove_max(self):
        """
        Removes and returns the maximum element of the heap
        @return maximum element of the heap or None if heap is empty
        """
        # TODO
        max_val = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        self.down_heap(0)

        return max_val
    
    def swap(self, idx1, idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]
    
    def left_child(self, idx):
        return 2 * idx + 1
    
    def right_child(self, idx):
        return 2 * idx + 2
    
    def heapify(self, idx):
        while True:
            left_child = 2 * idx + 1
            right_child = 2 * idx + 2
            largest = idx

            if left_child < self.size and self.heap[left_child] > self.heap[largest]:
                largest = left_child

            if right_child < self.size and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            if largest == idx:
                break

            self.swap(idx, largest)
            idx = largest
    
    def down_heap(self, idx):
        left_child = self.left_child(idx)
        right_child = self.right_child(idx)
        largest = idx

        if left_child < self.size and self.heap[left_child] > self.heap[largest]:
            largest = left_child

        if right_child < self.size and self.heap[right_child] > self.heap[largest]:
            largest = right_child

        if largest != idx:
            self.swap(idx, largest)
            self.down_heap(largest)