import unittest
from sorting import bubble_sort

class TestSortingAssignment(unittest.TestCase):

    def test_basic_sorting(self):
        """Test with a standard unsorted list (Worth 40 points)"""
        print("\nRunning basic sorting test...")
        self.assertEqual(bubble_sort([4, 2, 5, 1, 3]), [1, 2, 3, 4, 5])

    def test_already_sorted(self):
        """Test with an already sorted list (Worth 30 points)"""
        print("\nRunning already-sorted test...")
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_empty_and_single_element(self):
        """Test with edge cases: empty list and single element (Worth 30 points)"""
        print("\nRunning edge cases test...")
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([42]), [42])

if __name__ == '__main__':
    unittest.main()
