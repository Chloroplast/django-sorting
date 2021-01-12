from .SortingAlgorithm import SortingAlgorithm

# In insertion sort, the array of data to sort is divided into a sorted subarray and an unsorted subarray. The unsorted
# subarray is iterated through, with each item in the array being placed into the correct place in the sorted subarray.

# Worst Case Time Complexity: O(n^2)


class InsertionSort(SortingAlgorithm):
    def sort(self, data):
        for i in range(1, len(data)):
            current_val = data[i]
            j = i - 1

            while j >= 0 and current_val < data[j]:
                data[j + 1] = data[j]
                j -= 1

            data[j + 1] = current_val
