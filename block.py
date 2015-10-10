import time

class TimeBlock:
    def __init__(self, start, end):
        # TODO Handle edge cases for start and end being unexpected variables
        self.start = start
        self.end = end

    # Returns a timeblock with a time where two time blocks collide
    @staticmethod
    def find_collision(tb1, tb2):
        # Detect collision between time blocks
        new_start, new_end = None, None
        if (tb2.start <= tb1.start < tb2.end):
            new_start = tb1.start
            if tb1.end <= tb2.end:
                new_end = tb1.end
            new_end = tb2.end
        elif (tb2.start < tb1.end <= tb2.end):
            new_start = tb2.start
            new_end = tb1.end
        else:
            return None
        return TimeBlock(new_start, new_end)

class DateBlock:
    def __init__(self, name, timeblocks=[], collisions=[]):
        self.name = name
        self.timeblocks = timeblocks
        self.collisions = collisions

    def find_timeblock_collisions(self, db2):
        self_counter, db2_counter = 0, 0
        while self_counter < len(self.timeblocks) and \
               db2_counter < len(db2.timeblocks):

            tb1 = self.timeblocks[self_counter]
            tb2 = db2.timeblocks[db2_counter]
            collision_block = TimeBlock.find_collision(tb1, tb2)
            if collision_block:
                self.collisions.append(collision_block)
            # update the counters
            if tb1.start < tb2.start:
                self_counter += 1
            else: 
                db2_counter += 1

class ScheduleBlock:
    def __init__(self, name, dateblocks=[]):
        self.name = name
        self.dateblocks = dateblocks

    def find_dateblock_collisions(self, sb2):
        date_counter = 0
        while date_counter < len(self.timeblocks):

            tb1 = self.timeblocks[date_counter]
            tb2 = db2.timeblocks[date_counter]
            tb1.find_timeblock_collisions(tb2)
            # Destructive buildup may have to save meta data based on features
            self.dateblocks[date_counter] = DateBlock(tb1.name, 
                                            collisions=tb1.collisions)
            date_counter += 1

def scheduler(scheduleblocks):
    if len(scheduleblocks) < 2:
        return scheduleblocks
    scheduleblocks[0].find_dateblock_collisions(scheduleblocks[1])
    # parse the rest of the schedules
    for i in range(2, len(scheduleblocks)):
        scheduleblocks[0].find_dateblock_collisions(scheduleblocks[i])
    return scheduleblocks[0]

