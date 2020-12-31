import abc


class SortingAlgorithm(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def sort(self, data):
        return
