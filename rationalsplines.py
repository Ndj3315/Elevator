import matplotlib.pyplot as plt
import numpy as np

INTE = .0001

#currently, values must be strictly monotonic

#values (and nodes...) must be monotonic
# i runs from 1 to n
def rational_splines(nodes, values, d1, dn, epsilon):
	n = len(nodes)
	#accounting for python's 0-indexing
	nodes.insert(0,None)
	values.insert(0,None)
	h = [None]
	delta = [None]
	#build up h and delta
	for i in range(1, n):
		h.append(nodes[i+1] - nodes[i])
		delta.append( (values[i+1] - values[i]) / (1.0*h[i]) )
	#build up a,b,c,d
	#there is no b[1], c[1], hence the double None
	a = [None] ; b = [None, None] ; c = [None, None]
	d = [0]*(n+1)
	d[1] = d1 ; d[n] = dn ; d[0] = None
	for i in range(1,n):
		a.append( 1.0 / (h[i]*delta[i]) )
	for i in range(2, n):
		b.append( 1.0*delta[i-1]/h[i-1] + 1.0*delta[i]/h[i] )
		c.append( 1.0/h[i-1] + 1.0/h[i] )
	#iteratively build up the d's 	
	err = epsilon + 1
	while(err >= epsilon):
		dkp1 = [0] * (n+1)
		dkp1[0] = None 
		dkp1[1] = d[1]
		dkp1[n] = d[n]
		for i in range(2,n):
			term1 = 1.0 / ( 2*(a[i-1] + a[i]) )
			term2 = c[i] - a[i-1]*d[i-1] - a[i]*d[i+1]
			term3 = ( c[i] - a[i-1]*d[i-1] - a[i]*d[i+1] )**2
			term4 = 4*( a[i-1] + a[i] )*b[i]
			dkp1[i] = term1 * (term2 + (term3 + term4)**.5)
		err = max_diff(d, dkp1)
		d = dkp1
	#return lists of coefficients
	return [h, delta, d]
		 	
def max_diff(list1, list2):
	#lists have same size
	max_diff = 0
	for i in range(1, len(list1)):
		diff = abs( list1[i] - list2[i] )
		if( diff > max_diff ):
			max_diff = diff
	return max_diff

def theta(x, xi, hi):
	return (x - xi) / (1.0*hi)

def spline_func(h, theta, delta, dm, di, dp, fm, fi, fp, x):
	num1 = fp * theta**2
	num2 = delta**-1 * ( fp*di + fi*dp ) * theta * (1 - theta)
	num3 = fi * (1 - theta)**2
	numerator = num1 + num2 + num3
	dem1 = theta**2
	dem2 = delta**-1 * (di + dp) * theta * (1 - theta)
	dem3 = (1 - theta)**2
	denominator = dem1 + dem2 + dem3
	return (1.0 * numerator) / (1.0 * denominator)

def graph_mon_splines(nodes, values, d1, dn, epsilon):
	"""
	only works for monotonic data
	"""
	n = len(nodes) - 1
	splines = rational_splines(nodes, values, d1, dn, epsilon)
	h = splines[0]
	delta = splines[1]
	d = splines[2]
	for i in range(1,n+1):
		xi = nodes[i]
		t = np.arange(nodes[i], nodes[i+1] + INTE, INTE)
		c1 = h[i]
		c2 = theta(t,xi,h[i])
		c3 = delta[i]
		c4 = d[i-1]
		c5 = d[i]
		c6 = d[i+1]
		c7 = values[i-1]
		c8 = values[i]
		c9 = values[i+1]
		c10 = t
		plt.plot(t, spline_func(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10), color="grey", linewidth=1, alpha=.75) 
	#plt.show()

def spline_list(nodes, values, d1, dn, epsilon):
    spline_eval = np.array([])
    T = np.array([])
    n = len(nodes) - 1
    splines = rational_splines(nodes, values, d1, dn, epsilon)
    h = splines[0]
    delta = splines[1]
    d = splines[2]
    for i in range(1,n+1):
        xi = nodes[i]
        t = np.arange(nodes[i], nodes[i+1], epsilon)
        c1 = h[i]
        c2 = theta(t,xi,h[i])
        c3 = delta[i]
        c4 = d[i-1]
        c5 = d[i]
        c6 = d[i+1]
        c7 = values[i-1]
        c8 = values[i]
        c9 = values[i+1]
        c10 = t
        spline_eval = np.append(spline_eval, spline_func(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10))
        T = np.append(T, t)
    return T, spline_eval

"""
#the data used by Delbourgo and Gregory
xtable3 = [7.99, 8.09, 8.19, 8.7, 9.2, 10, 12, 15, 20]
ytable3 = [0, 2.76429*10**-5, 4.37498*10**-2, 0.169183, 0.469428, 0.943740, 0.998636, 0.999919, 0.999994]

xtable4 = [0, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15]
ytable4 = [10, 10, 10, 10, 10, 10, 10.5, 15, 50, 60, 85]

xtable5 = [22, 22.5, 22.6, 22.7, 22.8, 22.9, 23, 23.1, 23.2, 23.3, 23.4, 23.5, 24]
ytable5 = [523, 543, 550, 557, 565, 575, 590, 620, 860, 915, 944, 958, 986]

#just drawing some lines above and below the curve to make space in the picture
t = np.arange( 21.8 , 24.2 , INTE )
plt.plot(t, t*0 + 500)
plt.plot(t, t*0 + 1000)
graph_mon_splines(xtable5, ytable5, 0, 0, INTE)
"""

"""
t = np.arange( 7.99 , 21 , INTE )
plt.plot(t, t*0 + -.1)
plt.plot(t, t*0 + 1.1)
graph_mon_splines(xtable3, ytable3, 0, 0, INTE)
"""

"""
t = np.arange( -1 , 16 , INTE )
plt.plot(t, t*0 + -1)
plt.plot(t, t*0 + 86)
#drawing a line through the first few points...
t = np.arange(0, 8 + INTE, INTE)
plt.plot(t, t*0 + 10)
# ...and plotting the rest of them as usual
graph_mon_splines(xtable4[5:11], ytable4[5:11], 0, 0, INTE)
"""	 
