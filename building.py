import elevator
import employee

class Building:
    
    def __init__(self, theta, num_elevs, restriction, floor_dist):
    
        # number of employees working on each floor (including ground floor)
        #FLOOR_DIST = [0, 10, 30, 100, 100]
        FLOOR_DIST = floor_dist
        #NUM_ELEVATORS = 3
        # convenient for the final tab of how many employees are late
        self.num_employees = sum(FLOOR_DIST)
    
        # instantiate the elevators
        self.elevators = []
        for i in range(num_elevs):
            elevator_i = elevator.Elevator(i, restriction[i])
            self.elevators.append(elevator_i)
            
        # instantiate employees
        self.employees = []
        for floor in range(len(FLOOR_DIST)):
            for i in range(FLOOR_DIST[floor]):
                employee_i = employee.Employee(floor, theta)
                self.employees.append(employee_i)
        
    def step(self, time):
        for emp in self.employees:
            if emp.arrival_time == time:
                emp.location = "lobby"
        for elev in self.elevators:
            # pass the employees in the lobby to the elevator stepper
            employees_lobby = []
            for emp in self.employees:
                if emp.location == "lobby":
                    employees_lobby.append(emp)
            employees_delivered, employees_taken = elev.step( employees_lobby )
            for emp in employees_delivered:
                index = self.employees.index(emp)
                self.employees[index].location = "delivered"
            for emp in employees_taken:
                index = self.employees.index(emp)
                self.employees[index].location = "elevator"
            
                        