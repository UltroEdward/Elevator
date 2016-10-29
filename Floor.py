import random
import Person


class Floor:

    def __init__(self, position, persons, floors_limit):
        self.floors_limit = floors_limit
        self.position = position
        self.persons = [Person.Person(self.position, self.set_random_desired_floor(floors_limit, position)) for i in range(persons)]
        print(self)

    def set_random_desired_floor(self, end, not_include):
        is_looking = True
        while is_looking:
            desire_floor = random.randrange(1, end, 1)
            if desire_floor != not_include:
                is_looking = False
        return desire_floor

    def get_persons(self, desired_amount, is_wonna_go_up):
        print("Taking persons from floor {}. Current waiters here: {}.".format(self.position, len(self.persons)))
        founded_count = []
        for item in self.persons:
            if item.desired_floor > self.position and is_wonna_go_up is True:
                founded_count.append(item)
                self.persons.remove(item)
            elif item.desired_floor < self.position and is_wonna_go_up is False:
                founded_count.append(item)
                self.persons.remove(item)

            if len(founded_count) >= desired_amount:
                break
        return founded_count

    def __str__(self):
        return "Floor {} contains {} persons".format(self.position, len(self.persons))






