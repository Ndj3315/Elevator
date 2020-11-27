class Elevator:
    
    def __init__(self, identity):
    
        BETWEENFLOORS = 5
        FLOORSTOP = 15
        REOPEN = 5
        FILL = 25
    
        self.identity = identity # to identify different elevators
        self.passengers = []
        self.location = 0.0
        self.next_stop = 0
        self.time_left = FILL
        
    # decide what the behavior of the elevator should be
    # should the elevator figure out its next destination based on its passengers, or should controller do that? 