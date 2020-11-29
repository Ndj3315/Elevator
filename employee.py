import numpy as np

class Employee:
    def __init__(self, office_floor, theta):
        self.office_floor = office_floor # 0 through (5)
        self.arrival_time = int( self.__chi_square_sample(theta) )
        self.location = "outside" # then "lobby" then "elevator" then "delivered"

    def __chi_square_sample(self, df):
        # df does not have to be an integer
        return np.random.chisquare(df)
        
    def __expon_sample(self, lam):
        beta = 1.0 / lam
        return np.random.exponential(scale=beta)
        