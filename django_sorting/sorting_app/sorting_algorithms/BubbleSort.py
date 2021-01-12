from .SortingAlgorithm import SortingAlgorithm

# Bubble Sort compares adjacent elements in an array and swaps them if the first element is larger than the second
# such that the largest number 'bubble up' to the top

# Worst Case Time Complexity: O(n^2)


class BubbleSort(SortingAlgorithm):
    def sort(self, data):
        for i in range(0, len(data)):
            for j in range(0, len(data) - 1):
                if data[j] > data[j + 1]:
                    tmp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = tmp
