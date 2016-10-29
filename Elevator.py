class Elevator:

    def __init__(self, max_size=15, cur_floor=0):
        self.max_size = max_size
        self.cur_persons = []
        self.cur_floor = cur_floor

    def __str__(self):
        print("Elevator created")

    def take_persons(self, persons_arr):
        before = len(self.cur_persons)
        for person in persons_arr:
            while len(self.cur_persons) < self.max_size:
                self.cur_persons.append(person)
        if len(self.cur_persons) - before > 0:
            print("Persons taken {}".format(len(self.cur_persons) - before))

    def remove_persons(self):
        before = len(self.cur_persons)
        for person in self.cur_persons:
            if person.desired_floor == self.cur_floor:
                self.cur_persons.remove(person)
        if before - len(self.cur_persons) > 0:
            print("Persons removed {}".format(before - len(self.cur_persons)))

    def move_to_floor(self, desired_floor):
        self.cur_floor = desired_floor
        print("###Moving to  floor {}###".format(desired_floor))

    def get_available_count_to_take(self):
        return self.max_size - len(self.cur_persons)
