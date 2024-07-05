# Runtime Complexity O(d*(n+m))
class RadixSort:
    def __init__(self):
        self.base = 7
        self.bucket_list_history = []

    def get_bucket_list_history(self):
        return self.bucket_list_history

    def sort(self, input_array):
        """
        Sorts a given list using radix sort in descending order
        @param input_array to be sorted
        @returns a sorted list
        """
        self.bucket_list_history.clear()  # clear history list at beginning of sorting
        # TODO
        
        max_num = max(input_array)
        max_digits = len(str(max_num))
        
        for digit in range(max_digits):
            expo = 10 ** digit
            bucket_list = []
            for i in range(self.base):
                bucket_list.append([])
            
            for number in input_array:
                bucket_list[number // expo % 10].append(number)
            self._add_bucket_list_to_history(bucket_list[::-1])
            
            #print(f"Iteration: {digit + 1}: {bucket_list}")
            
            input_array = []
            for bucket in reversed(bucket_list):
                input_array.extend(bucket)

        # print(f"After merge: {input_array}")
        # print('='*111)
        
        return input_array

    # Helper functions
    def _add_bucket_list_to_history(self, bucket_list):
        """
        This method creates a snapshot (clone) of the bucket list and adds it to the bucket list history.
        @param bucket_list is your current bucket list, after assigning all elements to be sorted to the buckets.
        """
        arr_clone = []
        for i in range(0, len(bucket_list)):
            arr_clone.append([])
            for j in bucket_list[i]:
                arr_clone[i].append(j)
        self.bucket_list_history.append(arr_clone)