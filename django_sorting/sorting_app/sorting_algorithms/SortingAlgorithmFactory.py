from .InsertionSort import InsertionSort
from .BubbleSort import BubbleSort
from .DefaultPythonSort import DefaultPythonSort
from .SelectionSort import SelectionSort


class SortingAlgorithmFactory:

    @staticmethod
    def build(algorithm):
        if algorithm == "Bubble":
            return BubbleSort()
        elif algorithm == "Selection":
            return SelectionSort()
        elif algorithm == "Insertion":
            return InsertionSort()
        else:
            return DefaultPythonSort()
