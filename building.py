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
        for number in FLOOR_DIST:
            for i in range(number):
                employee_i = employee.Employee(number, theta)
                employees.append(employee_i)
                
        # keep track of employee locations
        self.employees_outside = set(employees)
        self.employees_lobby = set([])
        self.employees_elevator = set([])
        self.employees_delivered = set([])
        
    def step(time):
        for employee in self.employees:
            if employee.arrival_time == time:
                employee.location = "lobby"
        for elevator in self.elevators:
            elevator.step()
            for employee in self.employees:
                    if employee.location == "outside":
                        self.employees_outside.add(employee)
                    elif employee.location == "lobby":
                        self.employees_lobby.add(employee)
                    elif employee.location == "elevator":
                        self.employees_elevator.add(employee)
                    elif: employee.location == "delived":
                        self.employees_delivered.add(employee)
                    else:
                        raise Exception("Employee location: " + str(employee.location) + " ?")
                        