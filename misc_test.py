"""
use this file to test individual aspects of the program
"""


import controller

strategy0 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
strategy1 = [[1,2,3],[1,2,3],[4,5]]
strategy2 = [[1,2],[3,4,5],[3,4,5]]

strategy_add = [[1,2,3,4,5] for i in range(4)]
strategy_add2 = [[1,2,3,4,5] for i in range(5)]

con = controller.Controller(622, 3, strategy2)

print(con.run_sim())