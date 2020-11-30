import building

class Controller:
    
    def __init__(self, theta):
    
        # make the building
        self.building = building.Building(theta)

        # set starting time (seconds before 9am)
        start_time = 0
        for employee in self.building.employees:
            arrival = employee.arrival_time
            if arrival > start_time:
                start_time = arrival
        self.time = start_time
        
    def run_sim(self):
        while self.time >= 0: # make sure this is the fencepost that you want
            self.step()
            self.time -= 1
        # how many employees are late
        employees_delivered = 0
        for emp in self.building.employees:
            if emp.location == "delivered":
                employees_delivered += 1
        return self.building.num_employees - employees_delivered
        
    def step(self):
        self.building.step(self.time)