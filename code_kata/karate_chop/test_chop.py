from unittest import TestCase

from code_kata.karate_chop.first_method import first_chop


class FirstMethodTest(TestCase):
    def test_all_cases(self):
        self.assertEqual(-1, first_chop(3, []))
        self.assertEqual(-1, first_chop(3, [1]))
        self.assertEqual(0, first_chop(1, [1]))
        #
        self.assertEqual(0, first_chop(1, [1, 3, 5]))
        self.assertEqual(1, first_chop(3, [1, 3, 5]))
        self.assertEqual(2, first_chop(5, [1, 3, 5]))
        self.assertEqual(-1, first_chop(0, [1, 3, 5]))
        self.assertEqual(-1, first_chop(2, [1, 3, 5]))
        self.assertEqual(-1, first_chop(4, [1, 3, 5]))
        self.assertEqual(-1, first_chop(6, [1, 3, 5]))
        #
        self.assertEqual(0, first_chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, first_chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, first_chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, first_chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, first_chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, first_chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, first_chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, first_chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, first_chop(8, [1, 3, 5, 7]))
