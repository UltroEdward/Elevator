import Person
import random

class Floor():

    def __init__(self, position, persons, floors_limit):
        self.floors_limit = floors_limit
        self.set_position(position)
        self.persons = [Person.Person(position, self.set_random_desired_floor(floors_limit, position)) for i in range(persons)]
        print(self)

    def get_position(self):
        return self._position

    def set_position(self, position):
        if(position < 1 ):
            raise Exception("The lower floor is 1")
        self._position = position

    position = property(fget=get_position, fset=set_position)

    def set_random_desired_floor(self, end, not_include):
        isLooking = True
        while(isLooking):
            desire_floor = random.randrange(1, end, 1)
            if(desire_floor != not_include):
                isLooking =False
                return desire_floor

    def get_persons(self, desired_amount, is_wonna_go_up):
        print("Persons on floor {} waiting elevator {}".format (self.position, len(self.persons)) )
        founded_count = []
        for item in self.persons:
            if (item.desired_floor >  self.position and is_wonna_go_up==True):
                founded_count.append(item)
                self.persons.remove(item)
            elif(item.desired_floor <  self.position and is_wonna_go_up==False):
                founded_count.append(item)
                self.persons.remove(item)

            if(len(founded_count) == desired_amount):
                return founded_count
        return founded_count

    def __str__(self):
        return "Floor {} contains {} persons".format(self.position, len(self.persons))






