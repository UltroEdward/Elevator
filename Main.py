import Building
import Elevator

def start_jobs():
        print("start")
        elevator = Elevator.Elevator()
        building = Building.Building(elevator, 10, 1000)

        building.run_elevator()

start_jobs()
