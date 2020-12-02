# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:51:43 2020

@author: Nick
"""


import controller

strategy0 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
strategy1 = [[1,2,3],[1,2,3],[4,5]]
strategy2 = [[1,2],[3,4,5],[3,4,5]]

strategy_add = [[1,2,3,4,5] for i in range(4)]
strategy_add2 = [[1,2,3,4,5] for i in range(5)]

con = controller.Controller(622, 3, strategyX)

print(con.run_sim())