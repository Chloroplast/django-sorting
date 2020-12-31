from .BubbleSort import BubbleSort
from .DefaultPythonSort import DefaultPythonSort


class SortingAlgortihmFactory:

    @staticmethod
    def build(algorithm):
        if algorithm == "Bubble":
            return BubbleSort()
        else:
            return DefaultPythonSort()
