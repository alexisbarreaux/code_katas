from unittest import TestCase

from code_kata.karate_chop.methods.first_method import chop as first_chop
from code_kata.karate_chop.methods.second_method import chop as second_chop


class FirstMethodTest(TestCase):
    def test_all_cases(self):
        for method in [first_chop, second_chop]:
            self.assertEqual(-1, method(3, []))
            self.assertEqual(-1, method(3, [1]))
            self.assertEqual(0, method(1, [1]))
            #
            self.assertEqual(0, method(1, [1, 3, 5]))
            self.assertEqual(1, method(3, [1, 3, 5]))
            self.assertEqual(2, method(5, [1, 3, 5]))
            self.assertEqual(-1, method(0, [1, 3, 5]))
            self.assertEqual(-1, method(2, [1, 3, 5]))
            self.assertEqual(-1, method(4, [1, 3, 5]))
            self.assertEqual(-1, method(6, [1, 3, 5]))
            #
            self.assertEqual(0, method(1, [1, 3, 5, 7]))
            self.assertEqual(1, method(3, [1, 3, 5, 7]))
            self.assertEqual(2, method(5, [1, 3, 5, 7]))
            self.assertEqual(3, method(7, [1, 3, 5, 7]))
            self.assertEqual(-1, method(0, [1, 3, 5, 7]))
            self.assertEqual(-1, method(2, [1, 3, 5, 7]))
            self.assertEqual(-1, method(4, [1, 3, 5, 7]))
            self.assertEqual(-1, method(6, [1, 3, 5, 7]))
            self.assertEqual(-1, method(8, [1, 3, 5, 7]))
