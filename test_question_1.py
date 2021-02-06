import unittest
from question_1_program import cube

class cubeTest(unittest.TestCase):
        
    def test_cube_positive(self):
        for i in range(1,10):
            for j in range(1,10):
                for k in range(1,10):
                    self.assertEqual(cube(i,j,k), i*j*k)

    def test_cube_bad_type(self):
        with self.assertRaises(TypeError):
            cube("Hello","World","!")
            cube(1.0,"World",dict)
            cube("Hello",list,"!")

    def test_cube_bad_num(self):
        with self.assertRaises(ValueError):
            for i in range(0,-10,-1):
                for j in range(0,-10,-1):
                    for k in range(0,-10,-1):
                        cube(i,j,k)




if __name__ == "__main__":
    unittest.main()