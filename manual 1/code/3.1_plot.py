#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import scipy

#if using termux
import subprocess
import shlex
#end if



x = np.linspace(-4,12,50)#points on the x axis

simlen = int(1e6) #number of samples
err = [] #declaring probability list
#randvar = np.random.normal(0,1,simlen)
#randvar = np.loadtxt('uni.dat',dtype='double')
#randvar = np.loadtxt('gau.dat',dtype='double')
randvar = np.loadtxt('non_uniform.dat',dtype='double')
for i in range(0,50):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list
	
def func(x):
	if x < 0:
		return 0
	else: return 1-np.exp(-x/2)	

vect = scipy.vectorize(func,otypes=[np.float])

plt.plot(x.T,err,'o')#plotting the CDF
plt.plot(x,vect(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Simulation","Analysis"])
#if using termux
#plt.savefig('../figs/uni_cdf.pdf')
#plt.savefig('../figs/uni_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/uni_cdf.pdf"))
#if using termux
#plt.savefig('../figs/gauss_cdf.pdf')
#plt.savefig('../figs/gauss_cdf.eps')
#subprocess.run(shlex.split("termux-open ../figs/gauss_cdf.pdf"))
#else

plt.savefig('./figs/non_uni_cdf.png')
plt.savefig('./figs/non_uni_cdf.eps')
plt.show() #opening the plot window
