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
        employees = []
        for number in FLOOR_DIST:
            for i in range(number):
                employee_i = employee.Employee(number, theta)
                employees.append(employee_i)
                
        # keep track of employee locations
        employees_outside = employees
        employees_lobby = []
        employees_elevator = []
        employees_delivered = []
        
    def step():
        # maybe pass the time to this stepper method from controller