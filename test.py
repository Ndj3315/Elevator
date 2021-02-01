import controller
import matplotlib.pyplot as plt
import rationalsplines
import copy
import numpy as np
from scipy.special import gamma
#import math

MAXDF = 900 # maximum degrees of freedom to run simulation
INTERVAL=100 # where to sample
NUMTRIALS = 30 # how many times to run and average for each parameter value
NUMLATE_TARGET = 60

dfrange = list(range(1, MAXDF+1, INTERVAL))

floor_dist = [0, 10, 30, 100, 100]

numbers_late_ave = []

for df in dfrange:
    num_late = []
    for i in range(NUMTRIALS):
        con = controller.Controller(df, 3, [[1,2,3,4],[1,2,3,4],[1,2,3,4]], floor_dist)
        num_late.append(con.run_sim())
    ave_late = sum(num_late) / NUMTRIALS
    numbers_late_ave.append(ave_late)
    
"""
# for testing purposes

print(dfrange)
print(numbers_late_ave)
    
def monotonic(x):
    x = np.array(x)
    dx = np.diff(x)
    return np.all(dx <= 0) or np.all(dx >= 0)
print(monotonic(numbers_late_ave))
"""

spline = rationalsplines.rational_splines(copy.copy(dfrange), copy.copy(numbers_late_ave), 0, 0, .01)
    
rationalsplines.graph_mon_splines(copy.copy(dfrange), copy.copy(numbers_late_ave), 0, 0, .01)
plt.plot(dfrange, NUMLATE_TARGET*np.ones(len(dfrange)), color="black", linewidth=.5)
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
        diff = abs(array[i] - value)
        if diff < best:
            best = diff
            index = i
    return index
    
df_exact = find_nearest(spline_eval, NUMLATE_TARGET) * .01
df_nearest = int(round(df_exact))

strategy0 = [[1,2,3,4],[1,2,3,4],[1,2,3,4]]
strategy1 = [[3],[4],[1,2,3,4]]
strategy2 = [[3,4],[3,4],[1,2,3,4]]

times = []

STRATTRIALS = 100

for strat in [strategy0, strategy1, strategy2]:
    strat_times = []
    for i in range(STRATTRIALS):
        con = controller.Controller(df_nearest, 3, strat, floor_dist)
        strat_times.append(con.run_sim())
    times.append(strat_times)
    
def average(arr):
    return sum(arr) / len(arr)

perfs = [average(time_list) for time_list in times]

plt.bar(["No Strategy", "Strategy 1", "Strategy 2"], perfs)
plt.ylabel("late employees", size=15)
plt.show()

strategy_add = [[1,2,3,4] for i in range(4)]
strategy_add2 = [[1,2,3,4] for i in range(5)]

times_2 = []
strats_2 = [strategy0, strategy_add, strategy_add2]

for j in range(len(strats_2)):
    strat_times = []
    num_elevs = [3,4,5]
    for i in range(STRATTRIALS):
        con = controller.Controller(df_nearest, num_elevs[j], strats_2[j], floor_dist)
        strat_times.append(con.run_sim())
    times_2.append(strat_times)
    
perfs_2 = [average(time_list) for time_list in times_2]

plt.bar(["3 Elevators", "4 Elevators", "5 Elevators"], perfs_2)
plt.ylabel("late employees", size=15)
plt.show()

dfs_pic = [1,2,3,4,5,6,7]

def chi_square(x, df):
    g = gamma(df / 2)
    a = 1 / (2**(df/2) * g)
    b = x**(df/2 - 1)
    c = np.exp(-x/2)
    return a*b*c

INT = .01
x = np.arange(0+INT, 5, INT)

for df in dfs_pic:
    y = chi_square(x, df)
    plt.plot(x, y)
axes = plt.gca()
axes.set_ylim([0,1.2])
plt.xlabel("seconds before 9:00 am")
plt.ylabel("probability density")
plt.legend([str(df) for df in dfs_pic], title="degrees of freedom")
plt.show()    

floor_dist_walk = [0, 0, 0, 100, 100] # make employees on floors 1 and 2 walk

times_3 = []

floordists = [floor_dist, floor_dist_walk]

strategy3 = [[3],[4],[3,4]]

strategies = [strategy0, strategy0]

for i in range(len(floordists)):
    disttimes = []
    for j in range(STRATTRIALS):
        con = controller.Controller(df_nearest, 3, strategies[i], floordists[i])
        disttimes.append(con.run_sim())
    times_3.append(disttimes)

perfs_3 = [average(time_list) for time_list in times_3]

plt.bar(["No Strategy", "First and Second Floors Walk"], perfs_3)
plt.ylabel("late employees", size=15)
plt.show()
  