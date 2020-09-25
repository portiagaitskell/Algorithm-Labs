import unittest
from find_order import find_order

tests = (
    (
        (4, 3),
        3,
        1,
    ),
    (
        (35, 37, 38, 39, 72, 75, 91, 1, 4, 17),
        75,
        5,
    ),
    (
        (97, 0, 6, 37, 46, 48, 59, 70, 77, 80, 85),
        97,
        0,
    ),
    (
        (22, 28, 30, 33, 58, 85, 94, 99, 8, 12, 17, 19, 20),
        12,
        9,
    ),
    (
        (30, 33, 35, 37, 38, 39, 43, 48, 59, 65, 68, 75, 78, 84, 88, 94, 99, 16, 17, 22),
        85,
        None,
    ),
)

def check(test):
    all_orders, order, staff_sol = test
    student_sol = find_order(all_orders, order)
    return staff_sol == student_sol

class TestCases(unittest.TestCase):
    def test_01(self): self.assertTrue(check(tests[ 0]))
    def test_02(self): self.assertTrue(check(tests[ 1]))
    def test_03(self): self.assertTrue(check(tests[ 2]))
    def test_04(self): self.assertTrue(check(tests[ 3]))
    def test_05(self): self.assertTrue(check(tests[ 4]))

if __name__ == '__main__':
   res = unittest.main(verbosity = 3, exit = False)