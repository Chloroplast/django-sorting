from .SortingAlgorithm import SortingAlgorithm

# Selection Sort repeatedly finds the smallest element in an array and places it at the beginning. Two subarrays are
# kept track of - the sorted subarray and unsorted subarray. When the smallest element in the unsorted subarray is
# found, it is placed at the end of the sorted subarray.

# Worst Case Time Complexity: O(n^2)


class SelectionSort(SortingAlgorithm):
    def sort(self, data):
        for i in range(0, len(data)):
            current_min_index = i

            for j in range(i, len(data)):
                if data[j] < data[current_min_index]:
                    current_min_index = j

            tmp = data[i]
            data[i] = data[current_min_index]
            data[current_min_index] = tmp
