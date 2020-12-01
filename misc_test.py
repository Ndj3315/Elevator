# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:51:43 2020

@author: Nick
"""


import controller

strategy0 = [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
strategy1 = [[1,2,3],[1,2,3],[4,5]]

con = controller.Controller(622, 3, strategy0)

print(con.run_sim())