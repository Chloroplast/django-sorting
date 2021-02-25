from .SortingAlgorithm import SortingAlgorithm

# Merge Sort repeatedly divides an array into two subarrays until each subarray only has one element. It then merges the
# arrays back together into sorted subarrays until only the sorted original array remains.

# Worst Case Time Complexity: O(nlogn)


class MergeSort(SortingAlgorithm):
    def sort(self, data):
        if len(data) <= 1:
            return

        center_index = len(data)//2

        left_subarray = data[:center_index]
        right_subarray = data[center_index:]

        self.sort(left_subarray)
        self.sort(right_subarray)

        i = 0
        j = 0

        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] < right_subarray[j]:
                data[i + j] = left_subarray[i]
                i += 1
            else:
                data[i + j] = right_subarray[j]
                j += 1

        while i < len(left_subarray):
            data[i + j] = left_subarray[i]
            i += 1

        while j < len(right_subarray):
            data[i + j] = right_subarray[j]
            j += 1



