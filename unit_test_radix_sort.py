import unittest
from datetime import date

from radix_sort import RadixSort

test_array = [33, 614, 10216, 2123, 21523, 164504, 5142, 402, 6411, 21, 10123515, 0]
test_array_equals = [111, 4, 4, 4]
test_array_presorted = [0, 12, 15, 234, 5562]

maxPoints = 12.0  # defines the maximum achievable points for the example tested here
points = maxPoints  # stores the actually achieved points based on failed unit tests
summary = ""


def deduct_pts(value):
    global points
    points = points - value
    if points < 0:
        points = 0


def resolve_amount_of_pts_to_deduct(argument):
    pool = {
        "test_radix_sort_result": 3,
        "test_radix_sort_result_one_element": 1,
        "test_radix_sort_equal_elements": 1,
        "test_radix_sort_presorted_array": 1,
        "test_radix_sort_bucket_lists_iteration_1": 0.75,
        "test_radix_sort_bucket_lists_iteration_2": 0.75,
        "test_radix_sort_bucket_lists_iteration_3": 0.75,
        "test_radix_sort_bucket_lists_iteration_4": 0.75,
        "test_radix_sort_bucket_lists_iteration_5": 0.75,
        "test_radix_sort_bucket_lists_iteration_6": 0.75,
        "test_radix_sort_bucket_lists_iteration_7": 0.75,
        "test_radix_sort_bucket_lists_iteration_8": 0.75,
    }
    # resolve the pts to deduct from pool
    return pool.get(argument, 0)


class UnitTestTemplate(unittest.TestCase):
    def setUp(self):
        pass

    ####################################################
    # Definition of test cases
    ####################################################

    def test_radix_sort_result(self):
        r = RadixSort()
        result = r.sort(test_array.copy())
        test_array.sort(reverse=True)
        for i in range(0, len(test_array)):
            self.assertEqual(test_array[i], result[i],
                             f"ERROR: sort with input sequence {test_array} failed at index {i}: {result}")
        

    def test_radix_sort_result_one_element(self):
        r = RadixSort()
        result = r.sort([1])
        self.assertEqual(1, result[0], f"ERROR: sort with input sequence [1] failed at index 1: {result}")
        self.assertEqual(1, len(result), f"ERROR: sort with input sequence [1] failed because of incorrect size")
        

    def test_radix_sort_equal_elements(self):
        r = RadixSort()
        result = r.sort(test_array_equals.copy())
        test_array_equals.sort(reverse=True)
        for i in range(0, len(test_array_equals)):
            self.assertEqual(test_array_equals[i], result[i],
                             f"ERROR: sort with input sequence {test_array_equals} failed at index {i}: {result}")
        

    def test_radix_sort_presorted_array(self):
        r = RadixSort()
        result = r.sort(test_array_presorted.copy())
        test_array_presorted.sort(reverse=True)
        for i in range(0, len(test_array_presorted)):
            self.assertEqual(test_array_presorted[i], result[i],
                             f"ERROR: sort with input sequence {test_array_presorted} failed at index {i}: {result}")
    

    def test_radix_sort_bucket_lists_iteration_1(self):
        it_idx = 0
        err_msg = f"Radix sort of input array {test_array} failed in iteration {it_idx + 1} on bucket"
        r = RadixSort()
        r.sort(test_array.copy())
        bucket_list_history = r.get_bucket_list_history()

        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,
                        f"ERROR: bucket_list_history[{it_idx}] is of wrong size, must contain 7 buckets")

        self.assertEqual(1, len(bucket_list_history[it_idx][0]), err_msg + " 0 because of wrong size")
        self.assertTrue(10216 in bucket_list_history[it_idx][0], err_msg + " 0 because of missing element 10216")

        self.assertEqual(1, len(bucket_list_history[it_idx][1]), err_msg + " 1 because of wrong size")
        self.assertTrue(10123515 in bucket_list_history[it_idx][1], err_msg + " 1 because of missing element 10123515")

        self.assertEqual(2, len(bucket_list_history[it_idx][2]), err_msg + " 2 because of wrong size")
        self.assertTrue(614 in bucket_list_history[it_idx][2], err_msg + " 2 because of missing element 614")
        self.assertTrue(164504 in bucket_list_history[it_idx][2], err_msg + " 2 because of missing element 164504")

        self.assertEqual(3, len(bucket_list_history[it_idx][3]), err_msg + " 3 because of wrong size")
        self.assertTrue(33 in bucket_list_history[it_idx][3], err_msg + " 3 because of missing element 33")
        self.assertTrue(2123 in bucket_list_history[it_idx][3], err_msg + " 3 because of missing element 2123")
        self.assertTrue(21523 in bucket_list_history[it_idx][3], err_msg + " 3 because of missing element 21523")

        self.assertEqual(2, len(bucket_list_history[it_idx][4]), err_msg + " 4 because of wrong size")
        self.assertTrue(5142 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 5142")
        self.assertTrue(402 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 402")

        self.assertEqual(2, len(bucket_list_history[it_idx][5]), err_msg + " 5 because of wrong size")
        self.assertTrue(6411 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 6411")
        self.assertTrue(21 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 21")

        self.assertEqual(1, len(bucket_list_history[it_idx][6]), err_msg + " 6 because of wrong size")
        self.assertTrue(0 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 0")
        #print(len(bucket_list_history[it_idx][6]))

    def test_radix_sort_bucket_lists_iteration_2(self):
        it_idx = 1
        err_msg = f"Radix sort of input array {test_array} failed in iteration {it_idx + 1} on bucket"
        r = RadixSort()
        r.sort(test_array.copy())
        bucket_list_history = r.get_bucket_list_history()

        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,
                        "ERROR: bucket_list_history[" + str(it_idx) + "] is of wrong size, must contain 7 buckets")

        self.assertEqual(0, len(bucket_list_history[it_idx][0]), err_msg + " 0 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][1]), err_msg + " 1 because of wrong size")

        self.assertEqual(1, len(bucket_list_history[it_idx][2]), err_msg + " 2 because of wrong size")
        self.assertTrue(5142 in bucket_list_history[it_idx][2], err_msg + " 2 because of missing element 5142")

        self.assertEqual(1, len(bucket_list_history[it_idx][3]), err_msg + " 3 because of wrong size")
        self.assertTrue(33 in bucket_list_history[it_idx][3], err_msg + " 3 because of missing element 33")

        self.assertEqual(3, len(bucket_list_history[it_idx][4]), err_msg + " 4 because of wrong size")
        self.assertTrue(2123 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 2123")
        self.assertTrue(21523 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 21523")
        self.assertTrue(21 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 21")

        self.assertEqual(4, len(bucket_list_history[it_idx][5]), err_msg + " 5 because of wrong size")
        self.assertTrue(614 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 614")
        self.assertTrue(10216 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 10216")
        self.assertTrue(6411 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 6411")
        self.assertTrue(10123515 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 10123515")

        self.assertEqual(3, len(bucket_list_history[it_idx][6]), err_msg + " 6 because of wrong size")
        self.assertTrue(164504 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 164504")
        self.assertTrue(402 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 402")
        self.assertTrue(0 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 0")

    def test_radix_sort_bucket_lists_iteration_3(self):
        it_idx = 2
        err_msg = f"Radix sort of input array {test_array} failed in iteration {it_idx + 1} on bucket"
        r = RadixSort()
        r.sort(test_array.copy())
        bucket_list_history = r.get_bucket_list_history()

        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,
                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")

        self.assertEqual(1, len(bucket_list_history[it_idx][0]), err_msg + " 0 because of wrong size")
        self.assertTrue(614 in bucket_list_history[it_idx][0], err_msg + " 0 because of missing element 614")

        self.assertEqual(3, len(bucket_list_history[it_idx][1]), err_msg + " 1 because of wrong size")
        self.assertTrue(21523 in bucket_list_history[it_idx][1], err_msg + " 1 because of missing element 21523")
        self.assertTrue(164504 in bucket_list_history[it_idx][1], err_msg + " 1 because of missing element 164504")
        self.assertTrue(10123515 in bucket_list_history[it_idx][1], err_msg + " 1 because of missing element 10123515")

        self.assertEqual(2, len(bucket_list_history[it_idx][2]), err_msg + " 2 because of wrong size")
        self.assertTrue(402 in bucket_list_history[it_idx][2], err_msg + " 2 because of missing element 402")
        self.assertTrue(6411 in bucket_list_history[it_idx][2], err_msg + " 2 because of missing element 6411")

        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " 3 because of wrong size")

        self.assertEqual(1, len(bucket_list_history[it_idx][4]), err_msg + " 4 because of wrong size")
        self.assertTrue(10216 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 10216")

        self.assertEqual(2, len(bucket_list_history[it_idx][5]), err_msg + " 5 because of wrong size")
        self.assertTrue(2123 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 2123")
        self.assertTrue(5142 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 5142")

        self.assertEqual(3, len(bucket_list_history[it_idx][6]), err_msg + " 6 because of wrong size")
        self.assertTrue(33 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 33")
        self.assertTrue(21 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21")
        self.assertTrue(0 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 0")

    def test_radix_sort_bucket_lists_iteration_4(self):
        it_idx = 3
        err_msg = f"Radix sort of input array {test_array} failed in iteration {it_idx + 1} on bucket"
        r = RadixSort()
        r.sort(test_array.copy())
        bucket_list_history = r.get_bucket_list_history()

        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,
                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")

        self.assertEqual(1, len(bucket_list_history[it_idx][0]), err_msg + " 0 because of wrong size")
        self.assertTrue(6411 in bucket_list_history[it_idx][0], err_msg + " 0 because of missing element 6411")

        self.assertEqual(1, len(bucket_list_history[it_idx][1]), err_msg + " 1 because of wrong size")
        self.assertTrue(5142 in bucket_list_history[it_idx][1], err_msg + " 1 because of missing element 5142")

        self.assertEqual(1, len(bucket_list_history[it_idx][2]), err_msg + " 2 because of wrong size")
        self.assertTrue(164504 in bucket_list_history[it_idx][2], err_msg + " 2 because of missing element 164504")

        self.assertEqual(1, len(bucket_list_history[it_idx][3]), err_msg + " 3 because of wrong size")
        self.assertTrue(10123515 in bucket_list_history[it_idx][3], err_msg + " 3 because of missing element 10123515")

        self.assertEqual(1, len(bucket_list_history[it_idx][4]), err_msg + " 4 because of wrong size")
        self.assertTrue(2123 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 2123")

        self.assertEqual(1, len(bucket_list_history[it_idx][5]), err_msg + " 5 because of wrong size")
        self.assertTrue(21523 in bucket_list_history[it_idx][5], err_msg + " 4 because of missing element 21523")

        self.assertEqual(6, len(bucket_list_history[it_idx][6]), err_msg + " 6 because of wrong size")
        self.assertTrue(33 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 33")
        self.assertTrue(614 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 614")
        self.assertTrue(10216 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 10216")
        self.assertTrue(402 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 402")
        self.assertTrue(21 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21")
        self.assertTrue(0 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 0")

    def test_radix_sort_bucket_lists_iteration_5(self):
        it_idx = 4
        err_msg = f"Radix sort of input array {test_array} failed in iteration {it_idx + 1} on bucket"
        r = RadixSort()
        r.sort(test_array.copy())
        bucket_list_history = r.get_bucket_list_history()

        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,
                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")

        self.assertEqual(1, len(bucket_list_history[it_idx][0]), err_msg + " 0 because of wrong size")
        self.assertTrue(164504 in bucket_list_history[it_idx][0], err_msg + " 0 because of missing element 164504")

        self.assertEqual(0, len(bucket_list_history[it_idx][1]), err_msg + " 1 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][2]), err_msg + " 2 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " 3 because of wrong size")

        self.assertEqual(2, len(bucket_list_history[it_idx][4]), err_msg + " 4 because of wrong size")
        self.assertTrue(21523 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 21523")
        self.assertTrue(10123515 in bucket_list_history[it_idx][4], err_msg + " 4 because of missing element 10123515")

        self.assertEqual(1, len(bucket_list_history[it_idx][5]), err_msg + " 5 because of wrong size")
        self.assertTrue(10216 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 10216")

        self.assertEqual(8, len(bucket_list_history[it_idx][6]), err_msg + " 6 because of wrong size")
        self.assertTrue(33 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 33")
        self.assertTrue(614 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 614")
        self.assertTrue(2123 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 2123")
        self.assertTrue(5142 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 5142")
        self.assertTrue(402 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 402")
        self.assertTrue(6411 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 6411")
        self.assertTrue(21 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21")
        self.assertTrue(0 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 0")

    def test_radix_sort_bucket_lists_iteration_6(self):
        it_idx = 5
        err_msg = f"Radix sort of input array {test_array} failed in iteration {it_idx + 1} on bucket"
        r = RadixSort()
        r.sort(test_array.copy())
        bucket_list_history = r.get_bucket_list_history()

        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,
                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")

        self.assertEqual(0, len(bucket_list_history[it_idx][0]), err_msg + " 0 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][1]), err_msg + " 1 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][2]), err_msg + " 2 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " 3 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][4]), err_msg + " 4 because of wrong size")

        self.assertEqual(2, len(bucket_list_history[it_idx][5]), err_msg + " 5 because of wrong size")
        self.assertTrue(164504 in bucket_list_history[it_idx][5], err_msg + " 0 because of missing element 164504")
        self.assertTrue(10123515 in bucket_list_history[it_idx][5], err_msg + " 0 because of missing element 10123515")

        self.assertEqual(10, len(bucket_list_history[it_idx][6]), err_msg + " 6 because of wrong size")
        self.assertTrue(33 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 33")
        self.assertTrue(614 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 614")
        self.assertTrue(10216 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 10216")
        self.assertTrue(2123 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 2123")
        self.assertTrue(21523 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21523")
        self.assertTrue(5142 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 5142")
        self.assertTrue(402 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 402")
        self.assertTrue(6411 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 6411")
        self.assertTrue(21 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21")
        self.assertTrue(0 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 0")

    def test_radix_sort_bucket_lists_iteration_7(self):
        it_idx = 6
        err_msg = f"Radix sort of input array {test_array} failed in iteration {it_idx + 1} on bucket"
        r = RadixSort()
        r.sort(test_array.copy())
        bucket_list_history = r.get_bucket_list_history()

        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,
                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")

        self.assertEqual(0, len(bucket_list_history[it_idx][0]), err_msg + " 0 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][1]), err_msg + " 1 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][2]), err_msg + " 2 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " 3 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][4]), err_msg + " 4 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][5]), err_msg + " 5 because of wrong size")

        self.assertEqual(12, len(bucket_list_history[it_idx][6]), err_msg + " 6 because of wrong size")
        self.assertTrue(33 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 33")
        self.assertTrue(614 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 614")
        self.assertTrue(10216 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 10216")
        self.assertTrue(2123 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 2123")
        self.assertTrue(21523 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21523")
        self.assertTrue(164504 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 164504")
        self.assertTrue(5142 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 5142")
        self.assertTrue(402 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 402")
        self.assertTrue(6411 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 6411")
        self.assertTrue(21 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21")
        self.assertTrue(10123515 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 10123515")
        self.assertTrue(0 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 0")

    def test_radix_sort_bucket_lists_iteration_8(self):
        it_idx = 7
        err_msg = f"Radix sort of input array {test_array} failed in iteration {it_idx + 1} on bucket"
        r = RadixSort()
        r.sort(test_array.copy())
        bucket_list_history = r.get_bucket_list_history()

        self.assertTrue(len(bucket_list_history) > 0, "ERROR: bucket_list_history is empty")
        self.assertTrue(len(bucket_list_history[it_idx]) >= 7,
                        "ERROR: bucket_list_history[" + str(it_idx + 1) + "] is of wrong size, must contain 7 buckets")

        self.assertEqual(0, len(bucket_list_history[it_idx][0]), err_msg + " 0 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][1]), err_msg + " 1 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][2]), err_msg + " 2 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][3]), err_msg + " 3 because of wrong size")

        self.assertEqual(0, len(bucket_list_history[it_idx][4]), err_msg + " 4 because of wrong size")

        self.assertEqual(1, len(bucket_list_history[it_idx][5]), err_msg + " 5 because of wrong size")
        self.assertTrue(10123515 in bucket_list_history[it_idx][5], err_msg + " 5 because of missing element 10123515")

        self.assertEqual(11, len(bucket_list_history[it_idx][6]), err_msg + " 6 because of wrong size")
        self.assertTrue(33 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 33")
        self.assertTrue(614 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 614")
        self.assertTrue(10216 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 10216")
        self.assertTrue(2123 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 2123")
        self.assertTrue(21523 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21523")
        self.assertTrue(164504 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 164504")
        self.assertTrue(5142 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 5142")
        self.assertTrue(402 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 402")
        self.assertTrue(6411 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 6411")
        self.assertTrue(21 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 21")
        self.assertTrue(0 in bucket_list_history[it_idx][6], err_msg + " 6 because of missing element 0")


if __name__ == "__main__":
    unittest.main()
