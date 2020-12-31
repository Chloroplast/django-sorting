from .SortingAlgorithm import SortingAlgorithm


class BubbleSort(SortingAlgorithm):
    def sort(self, data):
        for i in range(0, len(data)):
            for j in range(0, len(data)):
                if data[i] < data[j]:
                    tmp = data[j]
                    data[j] = data[i]
                    data[i] = tmp

        print(data)