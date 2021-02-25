from .InsertionSort import InsertionSort
from .BubbleSort import BubbleSort
from .DefaultPythonSort import DefaultPythonSort
from .SelectionSort import SelectionSort
from .MergeSort import MergeSort

class SortingAlgorithmFactory:

    @staticmethod
    def build(algorithm):
        if algorithm == "Bubble":
            return BubbleSort()
        elif algorithm == "Selection":
            return SelectionSort()
        elif algorithm == "Insertion":
            return InsertionSort()
        elif algorithm == "Merge":
            return MergeSort()
        else:
            return DefaultPythonSort()
