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
        
    def deliver(self):
        employees_to_remove = []
        for i in range(len(self.passengers)):
            if self.passengers[i].office_floor == int(self.location):
                #self.passengers[i].location = "delivered"
                employees_to_remove.append(self.passengers[i])
        for employee in employees_to_remove:
            self.passengers.remove(employee)
        return employees_to_remove
        
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
        floors = [emp.office_floor for emp in self.passengers]
        stop = int(self.location) in floors
        if self.location == 0:
            self.time_left += self.FILL
        elif self.location % 1 != 0:
            self.time_left += self.BETWEENFLOORS
        elif stop:
            self.time_left += self.FLOORSTOP
        
    def next_delivery(self):
        if len(self.passengers) == 0:
            return 0
        floors = []
        for employee in self.passengers:
            floors.append(employee.office_floor)
        next_del = min(floors)
        
        """
        if self.identity == 0:
            print("Location: " + str(self.location))
            print("Next stop: " + str(next_del))
            print(floors)
            print()
        """
        
        if self.location >= next_del:
            raise Exception("Missed a floor!")
        return next_del
        
    def step(self, employees_lobby):
        employees_delivered = []
        if self.location % 1 == 0:
            employees_delivered = self.deliver()
        if self.location == 0: # in lobby
            self.fill(employees_lobby)
        self.move()
        return employees_delivered
        