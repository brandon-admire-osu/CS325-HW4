import unittest
from question_3_program import name

class averageListTest(unittest.TestCase):

    def test_good_input(self):
        self.assertEqual(name("Brandon","Admire"),"Brandon Admire")
        self.assertEqual(name("Cpt.","Underpants"),"Cpt. Underpants")
        self.assertEqual(name("Weird","Name"),"Weird Name")

    def test_bad_input(self):
        with self.assertRaises(TypeError):
            name(list, dict)
            name(23,19)

    def test_bad_args(self):
        with self.assertRaises(TypeError):
            name("Jacob","Jingle","Heimer","Scmidt")

        


if __name__ == "__main__":
    unittest.main()