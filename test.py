import controller
import matplotlib.pyplot as plt
import rationalsplines

MAXDF = 1000 # maximum degrees of freedom to run simulation
INTERVAL = 20
#INTERVAL=100 # to speed up testing
NUMTRIALS = 30 # how many times to run and average for each parameter value

dfrange = list(range(1, MAXDF+1, INTERVAL))

numbers_late_ave = []

for df in dfrange:
    num_late = []
    for i in range(NUMTRIALS):
        con = controller.Controller(df)
        num_late.append(con.run_sim())
    ave_late = sum(num_late) / NUMTRIALS
    numbers_late_ave.append(ave_late)
    
import numpy as np
def monotonic(x):
    x = np.array(x)
    dx = np.diff(x)
    return np.all(dx <= 0) or np.all(dx >= 0)
print(monotonic(numbers_late_ave))

spline = rationalsplines.rational_splines(dfrange, numbers_late_ave, 0, 0, .01)
    
rationalsplines.graph_mon_splines(dfrange, numbers_late_ave, 0, 0, .01)
plt.scatter(dfrange, numbers_late_ave, s=4, zorder=2, color="black")
plt.xlabel("df", size=15)
plt.ylabel("late employees", size=15)
plt.show()