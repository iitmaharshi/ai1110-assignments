#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,4,80)#points on the x axis


simlen = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('uni.dat',dtype='double')
for i in range(0,80):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def func(x):
	if x>=0 and x<=1:
		return x
	elif x>1:
		return 1
	else: return 0

vect = scipy.vectorize(func,otypes=[np.float])

plt.plot(x.T,err,'o')#plotting the CDF
plt.plot(x,vect(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Simulation", "Analysis"])
#if using termux
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
plt.savefig('./figs/uni_cdf.png')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else
plt.show() #opening the plot window
