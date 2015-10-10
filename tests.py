import unittest
from block import TimeBlock

class TestBlockMethods(unittest.TestCase):
    def test_basic(self):
        tb1 = TimeBlock(2, 5)
        tb2 = TimeBlock(4, 7)
        collisions = TimeBlock.find_collision(tb1, tb2)
        self.assertEqual(collisions.__repr__(), "(4, 5)")
        tb1 = TimeBlock(2, 5)
        tb2 = TimeBlock(4, 7)
        collisions = TimeBlock.find_collision(tb2, tb1)
        self.assertEqual(collisions.__repr__(), "(4, 5)")
        tb1 = TimeBlock(1, 4)
        tb2 = TimeBlock(4, 7)
        collisions = TimeBlock.find_collision(tb1, tb2)
        self.assertEqual(collisions.__repr__(), "None")


if __name__ == "__main__":
    unittest.main()