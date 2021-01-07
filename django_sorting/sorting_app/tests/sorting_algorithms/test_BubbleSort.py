from django.test import TestCase
from sorting_app.sorting_algorithms.BubbleSort import BubbleSort


class BubbleSortTests(TestCase):
    def setUp(self):
        self.bubble_sort = BubbleSort()

    def test_data_is_sorted_correctly(self):
        test_data = [8, 2, 1, 3, 600, 8, 6, 7]

        self.bubble_sort.sort(test_data)

        self.assertEquals(sorted(test_data), test_data)

    def test_algorithm_sorts_negative_numbers_and_zero_correctly(self):
        test_data = [8, 2, -1, 3, -600, 8, -6, 7, 0]

        self.bubble_sort.sort(test_data)

        self.assertEquals(sorted(test_data), test_data)

    def test_algorithm_sorts_with_only_one_number(self):
        test_data = [2]

        self.bubble_sort.sort(test_data)

        self.assertEquals(sorted(test_data), test_data)
