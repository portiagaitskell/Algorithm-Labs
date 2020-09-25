import unittest
from mode import mode

tests = (
    (
        (2, 2, 4, 1, 4),
        3,
    ),
    (
        (7, 8, 5, 7, 7, 3, 2, 8),
        7,
    ),
    (
        (7, 8, 5, 7, 7, 8, 2, 8),
        7.5,
    ),
    (
        (7, 7, 9, 1, 2, 11, 9, 6, 2, 8, 9),
        9,
    ),
    (
        (4, 18, 10, 8, 13, 16, 18, 1, 9, 6, 11, 13, 12, 5, 7, 17, 13, 3),
        13,
    ),
)

def check(test):
    A, staff_sol = test
    student_sol = mode(A)
    return staff_sol == student_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)