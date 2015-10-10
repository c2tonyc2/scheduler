import unittest
from block import TimeBlock
from block import DateBlock

def makeTimeBlocks(values):
    timeblocks = []
    for pair in values:
        timeblocks.append(TimeBlock(pair[0], pair[1]))
    return timeblocks

class Test_TimeBlock_Methods(unittest.TestCase):
    def test_basic(self):
        tblocks = makeTimeBlocks([(2, 5), (4,7)])
        collisions = TimeBlock.find_collision(tblocks[0], tblocks[1])
        self.assertEqual(collisions.__repr__(), "(4, 5)")
        collisions = TimeBlock.find_collision(tblocks[1], tblocks[0])
        self.assertEqual(collisions.__repr__(), "(4, 5)")
        tblocks = makeTimeBlocks([(1, 4), (4,7)])
        collisions = TimeBlock.find_collision(tblocks[0], tblocks[1])
        self.assertEqual(collisions.__repr__(), "None")

class Test_DateBlock_Methods(unittest.TestCase):
    def test_basic(self):
        db1 = DateBlock("Saturday", makeTimeBlocks([(1, 4), (7, 9), 
                                                    (13, 15), (17, 19), 
                                                    (21, 22), (22, 24)]
                                                   ))
        db2 = DateBlock("Saturday", makeTimeBlocks([(2, 3), (5, 7), 
                                                    (10, 13), (15, 18), 
                                                    (19, 21), (22, 23)]
                                                   ))
        db1.find_timeblock_collisions(db2)
        self.assertEqual(db1.__repr__(),
                         "Saturday: [(2, 3), (17, 18), (22, 23)]")

if __name__ == "__main__":
    unittest.main()