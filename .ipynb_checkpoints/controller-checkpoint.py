import building

class Controller:
    
    def __init__(self, theta):
    
        # make the building
        self.building = building.Building(theta)

        # set starting time (seconds before 9am)
        start_time = 0
        for employee in self.building.employees_outside:
            arrival = employee.arrival_time
            if arrival > start_time:
                start_time = arrival
        self.time = start_time
        
    def run_sim():
        while self.time >= 0: # make sure this is the fencepost that you want
            step()
            self.time -= 1
        # how many employees are late
        return self.building.num_employees - len( self.building.employees_delivered )
        
    def step():
        self.building.step()