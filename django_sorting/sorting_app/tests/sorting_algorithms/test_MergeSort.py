from django.test import TestCase
from sorting_app.sorting_algorithms.MergeSort import MergeSort


class MergeSortTests(TestCase):
    def setUp(self):
        self.merge_sort = MergeSort()

    def test_data_is_sorted_correctly(self):
        test_data = [8, 2, 1, 3, 600, 8, 6, 7]
        sorted_test_data = sorted(test_data)

        self.merge_sort.sort(test_data)

        self.assertEquals(sorted_test_data, test_data)

    def test_algorithm_sorts_negative_numbers_and_zero_correctly(self):
        test_data = [8, 2, -1, 3, -600, 8, -6, 7, 0]
        sorted_test_data = sorted(test_data)

        self.merge_sort.sort(test_data)

        self.assertEquals(sorted_test_data, test_data)

    def test_algorithm_sorts_with_only_one_number(self):
        test_data = [2]
        sorted_test_data = sorted(test_data)

        self.merge_sort.sort(test_data)

        self.assertEquals(sorted_test_data, test_data)
