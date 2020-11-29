class Elevator:

    BETWEENFLOORS = 5
    FLOORSTOP = 15
    REOPEN = 5
    FILL = 25
    CAPACITY = 10
    
    def __init__(self, identity):
    
        self.identity = identity # to identify different elevators
        self.passengers = []
        self.location = 0.0
        self.next_stop = 0
        self.time_left = self.FILL
        
    def fill(self, employees_lobby):
        lobby = employees_lobby
        while len(employees_lobby) != 0 and len(self.passengers) < self.CAPACITY:
            if self.time_left == 0:
                self.time_left += self.REOPEN
            employee = lobby.pop(0)
            employee.location = "elevator"
            self.passengers.append(employee)
        # done ?
        
    def deliver(self):
        for employee in self.passengers:
            if employee.office_floor == int(self.location):
                employee.location = "delivered"
                self.passengers.remove(employee)
        # done ?
        
    def move(self):
        self.next_stop = self.next_delivery()
        if self.time_left == 0:
            if self.next_stop == self.location:
                pass
            elif self.next_stop > self.location:
                self.location += .5
                self.new_location()
            elif self.next_stop < self.location:
                self.location -= .5
                self.new_location()
        else:
            self.time_left -= 1
        
    def new_location(self):
        if self.location == 0:
            self.time_left += self.FILL
        elif self.location % 1 != 0:
            self.time_left += self.BETWEENFLOORS
        else:
            self.time_left += self.FLOORSTOP
        
    def next_delivery(self):
        if len(self.passengers) == 0:
            return 0
        floors = []
        for employee in self.passengers:
            floors.append(employee.office_floor)
        next_del = min(floors)
        if self.location >= next_del:
            raise Exception("Missed a floor!")
        return next_del
        
    def step(self, employees_lobby):
        if self.location % 1 == 0:
            self.deliver()
        if self.location == 0: # in lobby
            self.fill(employees_lobby)
        self.move()
        