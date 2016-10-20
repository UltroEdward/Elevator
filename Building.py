import Floor
import random

class Building():

    def __init__(self, elevator, floors_count=10, persons_count=1000):
        self.elevator = elevator
        self.persons_count = persons_count
        self.floors_count = floors_count
        map = self.get_rand_persons_map(floors_count, persons_count)
        self.floors = [Floor.Floor(key, value, floors_count) for key, value in map.items()]

    def get_rand_persons_map(self, floors_count, persons_count):
        map = {}
        for i in range(floors_count):
            if (persons_count > 2):
                map[i + 1] = random.randrange(1, persons_count, 1)
                persons_count = persons_count - map[i + 1]
                continue
            else:
                map[i + 1] = persons_count
                persons_count = 0
            if (i == floors_count):
                map[i + 1] = persons_count
                continue
        return map

    def run_elevator(self):
        isMovingUp = True
        while(self.get_elevator_waiters_count() > 0):

            if (isMovingUp):
                for i in range(self.floors_count):
                    self.elevator.remove_persons()
                    self.elevator.take_persons(self.floors[i].get_persons(15, isMovingUp)) #TODO
                    if(i != self.floors_count-1):
                        self.elevator.move_to_floor(i+2)
            else:
                for i in reversed(range(self.floors_count)):
                    self.elevator.remove_persons()
                    self.elevator.take_persons(self.floors[i].get_persons(15, isMovingUp)) #TODO
                    if(i != self.floors_count-1):
                        self.elevator.move_to_floor(i-2)

        isMovingUp = False if isMovingUp else True




    def get_elevator_waiters_count(self):
        sum = 0
        for floor in self.floors:
            sum = sum + len(floor.persons)
        print("desired elevator waiters count is: " + str(sum))
        return sum

    def __str__(self):
        print("Building created, floors: {}, persons: {}".format(self.floors_count, self.persons_count))

