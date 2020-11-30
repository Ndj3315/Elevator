import controller
import matplotlib.pyplot as plt
import rationalsplines
import copy
import numpy as np
import math

MAXDF = 1000 # maximum degrees of freedom to run simulation
INTERVAL=100 # where to sample
NUMTRIALS = 30 # how many times to run and average for each parameter value
NUMLATE_TARGET = 60

dfrange = list(range(1, MAXDF+1, INTERVAL))

numbers_late_ave = []

for df in dfrange:
    num_late = []
    for i in range(NUMTRIALS):
        con = controller.Controller(df)
        num_late.append(con.run_sim())
    ave_late = sum(num_late) / NUMTRIALS
    numbers_late_ave.append(ave_late)
    
"""
# for testing purposes

print(dfrange)
print(numbers_late_ave)
    
import numpy as np
def monotonic(x):
    x = np.array(x)
    dx = np.diff(x)
    return np.all(dx <= 0) or np.all(dx >= 0)
print(monotonic(numbers_late_ave))
"""

spline = rationalsplines.rational_splines(copy.copy(dfrange), copy.copy(numbers_late_ave), 0, 0, .01)
    
rationalsplines.graph_mon_splines(copy.copy(dfrange), copy.copy(numbers_late_ave), 0, 0, .01)
plt.scatter(dfrange, numbers_late_ave, s=4, zorder=2, color="black")
plt.xlabel("df", size=15)
plt.ylabel("late employees", size=15)
plt.show()

# now find the df value that leads to "60" late employees

T, spline_eval = rationalsplines.spline_list(copy.copy(dfrange), copy.copy(numbers_late_ave), 0, 0, .01)

def find_nearest(array,value):
    index = 0
    best = 100
    for i in range(len(array)):
        diff = abs(array[i] - NUMLATE_TARGET)
        if diff < best:
            best = diff
            index = i
    return index
    
df_exact = find_nearest(spline_eval, NUMLATE_TARGET) * .01
df_nearest = int(round(df_exact))

print(df_nearest)