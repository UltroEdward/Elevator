import Floor
import random


class Building:

    def __init__(self, elevator, floors_count=10, persons_count=1000):
        self.elevator = elevator
        self.floors_count = floors_count
        self.persons_count = persons_count
        self.map_of_floor_and_persons = self.get_rand_persons_map(floors_count, persons_count)
        self.floors = [Floor.Floor(key, value, floors_count) for key, value in self.map_of_floor_and_persons.items()]
        print("Building created")

    def get_rand_persons_map(self, floors_count, persons_count):
        map_of_persons = {}
        for i in range(floors_count):
            if persons_count > 2:
                map_of_persons[i + 1] = random.randrange(1, persons_count, 1)
                persons_count = persons_count - map_of_persons[i + 1]
            else:
                map_of_persons[i + 1] = persons_count
                persons_count = 0

            if i == floors_count:
                map_of_persons[i + 1] = persons_count

        return map_of_persons

    def run_elevator(self):
        is_moving_up = True
        counter = 0
        while self.get_elevator_waiters_count() > 0:

            if is_moving_up:
                for i in range(1, self.floors_count + 1):
                    self.elevator.remove_persons()
                    self.elevator.take_persons(self.floors[i-1].get_persons(self.elevator.get_available_count_to_take(), is_moving_up))
                    if i < self.floors_count:
                        self.elevator.move_to_floor(i+1)
            else:
                for i in range(self.floors_count, 1, -1):
                    self.elevator.remove_persons()
                    self.elevator.take_persons(self.floors[i-1].get_persons(self.elevator.get_available_count_to_take(), is_moving_up))
                    if i != 1:
                        self.elevator.move_to_floor(i-1)

            is_moving_up = False if is_moving_up else True
            counter += 1

        print("Iteration (1 iteration = way from 1 to last floor, or from last to one) count is: #####{}#####".format(counter))

    def get_elevator_waiters_count(self):
        cur_waiters_count = 0
        for floor in self.floors:
            cur_waiters_count = cur_waiters_count + len(floor.persons)
        print("All desired elevator waiters count is: {}".format(str(cur_waiters_count)))
        return cur_waiters_count

    def __str__(self):
        print("Building created, floors: {}, persons: {}".format(self.floors_count, self.persons_count))

