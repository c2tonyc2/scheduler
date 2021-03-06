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
            if tb1.end <= tb2.end:
                return tb1
            new_start = tb1.start
            new_end = tb2.end
        elif (tb2.start < tb1.end <= tb2.end):
            new_start = tb2.start
            new_end = tb1.end
        elif (tb1.start < tb2.start and tb1.end > tb2.end):
            return tb2
        else:
            return None
        return TimeBlock(new_start, new_end)

    def __repr__(self):
        return "({0}, {1})".format(self.start, self.end)

class DateBlock:
    def __init__(self, name, timeblocks=[], collisions=[]):
        self.name = name
        self.timeblocks = timeblocks
        self.collisions = collisions

    def find_timeblock_collisions(self, db2):
        self.collisions = []
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

    def __repr__(self):
        return "{0}: {1}".format(self.name, self.timeblocks.__str__())

class ScheduleBlock:
    def __init__(self, name, dateblocks=[]):
        self.name = name
        self.dateblocks = dateblocks

    def find_dateblock_collisions(self, sb2):
        date_counter = 0
        while date_counter < len(self.dateblocks):

            tb1 = self.dateblocks[date_counter]
            tb2 = sb2.dateblocks[date_counter]
            tb1.find_timeblock_collisions(tb2)
            # Destructive constuction!! Save meta data based on features
            self.dateblocks[date_counter] = DateBlock(tb1.name,
                                              collisions=tb1.collisions)
            date_counter += 1

    def __repr__(self):
        string = ""
        for dateblock in self.dateblocks:
            string += "{0}\n".format(dateblock.__str__())
        return string

class ScheduleGroup:
    def __init__(self, scheduleblocks, group_id):
        self.id = group_id
        self.scheduleblocks = scheduleblocks

def scheduler(group):
    if len(group.scheduleblocks) < 2:
        return group.scheduleblocks
    group.scheduleblocks[0].find_dateblock_collisions(
                                group.scheduleblocks[1])
    # parse the rest of the schedules
    for i in range(2, len(group.scheduleblocks)):
        group.scheduleblocks[0].find_dateblock_collisions(
                                group.scheduleblocks[i])
    return group.scheduleblocks[0]

