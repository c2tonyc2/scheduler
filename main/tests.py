import unittest
from block import TimeBlock
from block import DateBlock
from block import ScheduleBlock

def makeTimeBlocks(values):
    timeblocks = []
    for pair in values:
        timeblocks.append(TimeBlock(pair[0], pair[1]))
    return timeblocks

class Test_TimeBlock_Methods(unittest.TestCase):
    def test_basic(self):
        tblocks = makeTimeBlocks([(2, 5), (4,7)])
        collisions = TimeBlock.find_collision(tblocks[0], tblocks[1])
        self.assertEqual(collisions.__repr__(), '(4, 5)')
        collisions = TimeBlock.find_collision(tblocks[1], tblocks[0])
        self.assertEqual(collisions.__repr__(), '(4, 5)')
        tblocks = makeTimeBlocks([(1, 4), (4,7)])
        collisions = TimeBlock.find_collision(tblocks[0], tblocks[1])
        self.assertEqual(collisions.__repr__(), 'None')

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
        self.assertEqual('{0}: {1}'.format(db1.name, db1.collisions.__repr__()),
                         'Saturday: [(2, 3), (17, 18), (22, 23)]')

class Test_ScheduleBlock_Methods(unittest.TestCase):
    def test_basic(self):
        db1 = DateBlock("Saturday", makeTimeBlocks([(1, 4), (7, 9), 
                                                    (13, 15), (17, 19), 
                                                    (21, 22), (22, 24)]
                                                   ))
        db2 = DateBlock("Sunday", makeTimeBlocks([(3, 9), (12, 15), 
                                                    (18, 19), (21, 24)]
                                                   ))
        db3 = DateBlock("Saturday", makeTimeBlocks([(2, 3), (5, 7), 
                                                    (10, 13), (15, 18), 
                                                    (19, 21), (22, 23)]
                                                   ))
        db4 = DateBlock("Sunday", makeTimeBlocks([(1, 7), (11, 17), 
                                                    (18, 22), (23, 24)]
                                                   ))

        sb1 = ScheduleBlock("John", [db1, db2])
        sb2 = ScheduleBlock("Cena", [db3, db4])

        sb1.find_dateblock_collisions(sb2)
        self.assertEqual('{0}: {1}'.format(sb1.dateblocks[0].name, 
                                           sb1.dateblocks[0].collisions),
                         'Saturday: [(2, 3), (17, 18), (22, 23)]')
        self.assertEqual('{0}: {1}'.format(sb1.dateblocks[1].name, 
                                           sb1.dateblocks[1].collisions),
                         'Sunday: [(3, 7), (12, 15), (18, 19), (23, 24)]')

if __name__ == "__main__":
    unittest.main()