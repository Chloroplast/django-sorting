from .SortingAlgorithm import SortingAlgorithm


class DefaultPythonSort(SortingAlgorithm):
    def sort(self, data):
        list.sort(data)