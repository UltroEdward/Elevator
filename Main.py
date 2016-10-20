import Elevator
import Building

def startJobs():
        print("start")
        elevator = Elevator.Elevator()
        building = Building.Building(elevator, 10, 1000)

        building.run_elevator()

startJobs()