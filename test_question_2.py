import unittest
import statistics
import random
from question_2_program import averageList

class averageListTest(unittest.TestCase):

    def test_good_inp(self):
        random.seed()
        cases = []

        for i in range(5):
            cases.append(list())
            for j in range(random.randint(1,20)):
                cases[i].append(random.randint(1,20))

        for current in cases:
            self.assertEqual(averageList(current),statistics.mean(current))

    def test_bad_input(self):
        cases = [
            [],
            ["this","is","a","test"],
            [dict,list,0]
        ]

        with self.assertRaises(ValueError):
            averageList(cases[0])

        with self.assertRaises(TypeError):
            averageList(cases[1])
            averageList(cases[2])

    def test_good_float(self):
        random.seed()
        cases = []

        for i in range(5):
            cases.append(list())
            for j in range(random.randint(1,20)):
                cases[i].append(random.random())

        for current in cases:
            self.assertAlmostEqual(averageList(current),statistics.mean(current))
        


if __name__ == "__main__":
    unittest.main()