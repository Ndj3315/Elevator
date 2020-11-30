import elevator
import employee

class Building:
    
    def __init__(self, theta):
    
        # number of employees working on each floor (including ground floor)
        FLOOR_DIST = [0, 60, 60, 60, 60, 60]
        NUM_ELEVATORS = 3
        # convenient for the final tab of how many employees are late
        self.num_employees = sum(FLOOR_DIST)
    
        # instantiate the elevators
        self.elevators = []
        for i in range(NUM_ELEVATORS):
            elevator_i = elevator.Elevator(i)
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
            employees_delivered = elev.step( employees_lobby )
            for emp in employees_delivered:
                index = self.employees.index(emp)
                self.employees[index].location = "delivered"
            
                        