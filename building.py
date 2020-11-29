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
                
        # keep track of employee locations
        self.employees_outside = self.employees
        self.employees_lobby = []
        self.employees_elevator = []
        self.employees_delivered = []
        
    def update_employees(self):
        for employee in self.employees:
            if employee.location == "outside":
                pass
            elif employee.location == "lobby":
                if not employee in self.employees_lobby:
                    self.employees_lobby.append(employee)
                    self.employees_outside.remove(employee)
            elif employee.location == "elevator":
                if not employee in self.employees_elevator:
                    self.employees_elevator.append(employee)
                    self.employees_lobby.remove(employee)
            elif employee.location == "delivered":
                if not employee in self.employees_delivered:
                    self.employees_delivered.append(employee)
                    self.employees_elevator.remove(employee)
            else:
                raise Exception("Employee location: " + str(employee.location) + " ?")
        
    def step(self, time):
        for employee in self.employees:
            if employee.arrival_time == time:
                employee.location = "lobby"
        for elevator in self.elevators:
            # pass the employees in the lobby to the elevator stepper
            elevator.step( self.employees_lobby )
            self.update_employees()
            
                        