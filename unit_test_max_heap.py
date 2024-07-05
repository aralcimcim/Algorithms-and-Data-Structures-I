import unittest
from datetime import date

from max_heap import MaxHeap

heap0 = [0]
heap201 = [2, 0, 1]
heap102 = [1, 0, 2]
heap01234 = [0, 1, 2, 3, 4]
test_array = [3, 9, 17, 2, 23, 1, 5, 4, 19, 17, 7, 18, 8, 67, 6, 11, 0]
test_array_sorted = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 17, 17, 18, 19, 23, 67]

maxPoints = 10.0  # defines the maximum achievable points for the example tested here
points = maxPoints  # stores the actually achieved points based on failed unit tests
summary = ""


def deduct_pts(value):
    global points
    points = points - value
    if points < 0:
        points = 0


def resolve_amount_of_pts_to_deduct(argument):
    pool = {
        "test_heap_bottom_up_with_arr_one_element": 0.5,
        "test_heap_bottom_up_with_arr_without_downheap": 0.5,
        "test_heap_bottom_up_with_arr_with_single_downheap": 1,
        "test_heap_bottom_up_with_arr_with_multiple_downheap": 1,
        "test_heap_bottom_up_init_with_none": 0.5,
        "test_heap_bottom_up_construction_large": 0.5,
        "test_heap_bottom_up_remove_max_last_element": 0.5,
        "test_heap_bottom_up_remove_max_without_downheap": 0.5,
        "test_heap_bottom_up_remove_max_with_downheap": 1,
        "test_heap_bottom_up_contains_existing": 0.5,
        "test_heap_bottom_up_contains_not_existing": 0.5,
        "test_heap_bottom_up_sort": 3,
    }
    # resolve the pts to deduct from pool
    return pool.get(argument, 0)


def children(heap, index):
    index += 1
    c1 = 2 * index - 1
    c2 = 2 * index
    if c1 > len(heap) - 1:
        return []
    if c2 > len(heap) - 1:
        return [c1]
    return [c1, c2]


def test_heap_structure(heap, index):
    c = children(heap, index)
    if len(c) <= 0:
        return True
    if heap[c[0]] > heap[index]:
        return False
    if len(c) <= 1:
        return True
    if heap[c[1]] > heap[index]:
        return False
    return test_heap_structure(heap, c[0]) and test_heap_structure(heap, c[1])


class UnitTestTemplate(unittest.TestCase):
    def setUp(self):
        pass

    ####################################################
    # Definition of test cases
    ####################################################

    def test_heap_bottom_up_with_arr_one_element(self):
        heap = MaxHeap(heap0.copy())
        heap_arr = heap.get_heap()
        self.assertEqual(1, heap.get_size(),
                         "ERROR: Bottom-Up construction of heap with input array {0} failed, incorrect size")
        self.assertEqual(heap0[0], heap_arr[0],
                         "ERROR: Bottom-Up construction of heap with input array {0} failed, incorrect element")

    def test_heap_bottom_up_with_arr_without_downheap(self):
        heap = MaxHeap(heap201.copy())
        self.assertEqual(len(heap201), heap.get_size(),
                         f"ERROR: Bottom-Up construction of heap with input array {heap201} returned wrong size")
        self.assertTrue(test_heap_structure(heap.get_heap(), 0),
                        f"ERROR: Bottom-Up construction of heap with input array {heap01234} had an incorrect heap "
                        f"structure")

    def test_heap_bottom_up_with_arr_with_single_downheap(self):
        heap = MaxHeap(heap102.copy())
        self.assertEqual(len(heap102), heap.get_size(),
                         f"ERROR: Bottom-Up construction of heap with input array {heap102} returned wrong size")
        self.assertTrue(test_heap_structure(heap.get_heap(), 0),
                        f"ERROR: Bottom-Up construction of heap with input array {heap01234} had an incorrect heap "
                        f"structure")

    def test_heap_bottom_up_with_arr_with_multiple_downheap(self):
        heap = MaxHeap(heap01234.copy())
        self.assertEqual(len(heap01234), heap.get_size(),
                         f"ERROR: Bottom-Up construction of heap with input array {heap01234} returned wrong size")
        self.assertTrue(test_heap_structure(heap.get_heap(), 0),
                        f"ERROR: Bottom-Up construction of heap with input array {heap01234} had an incorrect heap "
                        f"structure")

    def test_heap_bottom_up_init_with_none(self):
        with self.assertRaises(ValueError):
            MaxHeap(None)

    def test_heap_bottom_up_construction_large(self):
        heap = MaxHeap(test_array.copy())
        self.assertEqual(len(test_array), heap.get_size(),
                         f"ERROR: Bottom-Up construction of heap with input array {test_array} returned wrong size")
        self.assertTrue(test_heap_structure(heap.get_heap(), 0),
                        f"ERROR: Bottom-Up construction of heap with input array {test_array} had an incorrect heap "
                        f"structure")

    def test_heap_bottom_up_remove_max_last_element(self):
        heap = MaxHeap(heap0.copy())
        self.assertEqual(0, heap.remove_max(),
                         f"ERROR: remove_max returned incorrect element for input sequence {heap0}")

    def test_heap_bottom_up_remove_max_without_downheap(self):
        heap = MaxHeap(heap201.copy())
        self.assertEqual(len(heap201), heap.get_size(),
                         f"ERROR: remove_max could not be tested because heap could not be created using input "
                         f"sequence {heap201}")
        self.assertTrue(test_heap_structure(heap.get_heap(), 0),
                        f"ERROR: remove_max could not be tested because heap could not be created using input "
                        f"sequence {heap201}")

        self.assertEqual(2, heap.remove_max(),
                         f"ERROR: remove_max returned incorrect element for input sequence {heap201}")

        self.assertEqual(len(heap201) - 1, heap.get_size(),
                         f"ERROR: heap has an incorrect size after remove_max with input sequence {heap201}")
        self.assertTrue(test_heap_structure(heap.get_heap(), 0),
                        f"ERROR: heap has an incorrect size after remove_max with input sequence {heap201}")

    def test_heap_bottom_up_remove_max_with_downheap(self):
        heap = MaxHeap(heap01234.copy())
        self.assertEqual(len(heap01234), heap.get_size(),
                         f"ERROR: remove_max could not be tested because heap could not be created using input "
                         f"sequence {heap01234}")
        self.assertTrue(test_heap_structure(heap.get_heap(), 0),
                        f"ERROR: remove_max could not be tested because heap could not be created using input "
                        f"sequence {heap01234}")

        self.assertEqual(4, heap.remove_max(),
                         f"ERROR: remove_max returned incorrect element for input sequence {heap01234}")
        self.assertEqual(len(heap01234) - 1, heap.get_size(),
                         f"ERROR: heap has an incorrect size after remove_max with input sequence {heap01234}")

    def test_heap_bottom_up_contains_existing(self):
        heap = MaxHeap(test_array.copy())
        message = "ERROR: contains returned False for element "
        self.assertTrue(heap.contains(3), message + f"3 using input sequence {test_array}")
        self.assertTrue(heap.contains(9), message + f"9 using input sequence {test_array}")
        self.assertTrue(heap.contains(17), message + f"17 using input sequence {test_array}")
        self.assertTrue(heap.contains(2), message + f"2 using input sequence {test_array}")
        self.assertTrue(heap.contains(23), message + f"23 using input sequence {test_array}")
        self.assertTrue(heap.contains(1), message + f"1 using input sequence {test_array}")
        self.assertTrue(heap.contains(5), message + f"5 using input sequence {test_array}")
        self.assertTrue(heap.contains(4), message + f"4 using input sequence {test_array}")
        self.assertTrue(heap.contains(19), message + f"19 using input sequence {test_array}")
        self.assertTrue(heap.contains(17), message + f"17 using input sequence {test_array}")
        self.assertTrue(heap.contains(7), message + f"7 using input sequence {test_array}")
        self.assertTrue(heap.contains(18), message + f"18 using input sequence {test_array}")
        self.assertTrue(heap.contains(8), message + f"8 using input sequence {test_array}")
        self.assertTrue(heap.contains(67), message + f"67 using input sequence {test_array}")
        self.assertTrue(heap.contains(6), message + f"6 using input sequence {test_array}")
        self.assertTrue(heap.contains(11), message + f"11 using input sequence {test_array}")
        self.assertTrue(heap.contains(0), message + f"0 using input sequence {test_array}")

    def test_heap_bottom_up_contains_not_existing(self):
        heap = MaxHeap(test_array.copy())
        message = "ERROR: contains returned True for element "
        self.assertFalse(heap.contains(44), message + f"44 using input sequence {test_array}")
        self.assertFalse(heap.contains(-1), message + f"-1 using input sequence {test_array}")
        self.assertFalse(heap.contains(10), message + f"10 using input sequence {test_array}")
        self.assertFalse(heap.contains(13), message + f"13 using input sequence {test_array}")
        self.assertFalse(heap.contains(102), message + f"102 using input sequence {test_array}")
        self.assertFalse(heap.contains(3489), message + f"3489 using input sequence {test_array}")

    def test_heap_bottom_up_sort(self):
        tmp = test_array.copy()
        heap = MaxHeap(tmp)
        heap.sort()
        self.assertEqual(len(tmp), len(test_array_sorted), f"ERROR: sort failed because of incorrect list size")
        for i in range(0, len(test_array_sorted)):
            self.assertEqual(test_array_sorted[i], tmp[i], f"ERROR: sort failed with input sequence {test_array} at "
                                                           f"index {i}")


if __name__ == "__main__":
    unittest.main()
