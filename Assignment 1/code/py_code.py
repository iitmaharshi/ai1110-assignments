import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

def dir_vec(A,B):
  return B-A

def ccircle(A,B,C):
  p = np.zeros(2)
  n1 = dir_vec(B,A)
  p[0] = 0.5*(np.linalg.norm(A)**2-np.linalg.norm(B)**2)
  n2 = dir_vec(C,B)
  p[1] = 0.5*(np.linalg.norm(B)**2-np.linalg.norm(C)**2)
  #Intersection
  N=np.vstack((n1,n2))
  O=np.linalg.inv(N)@p
  r = np.linalg.norm(A -O)
  return O,r

A = np.array([0, 0])
B = np.array([6.5, 0])
C = np.array([9,2.5*(3**0.5)])
E,r = ccircle(A,B,C)
D = np.array([0.727,9.9])
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_circ = circ_gen(E,r)
x_AD = line_gen(A,D)
x_CD = line_gen(C,D)
plt.axis('off')
plt.plot(0,0,marker = "o",markeredgecolor = "red",markerfacecolor = "red")
plt.plot(6.5,0,marker = "o",markeredgecolor = "red",markerfacecolor = "red")
plt.plot(8.95,4.33,marker = "o",markeredgecolor = "red",markerfacecolor = "red")
plt.plot(3.25,4.76,marker = "o",markeredgecolor = "red",markerfacecolor = "red")
plt.plot(0.727,9.9,marker = "o",markeredgecolor = "red",markerfacecolor = "red")
plt.plot(x_AB[0,:], x_AB[1,:], 'k')
plt.plot(x_BC[0,:], x_BC[1,:], 'k')
plt.plot(x_CA[0,:], x_CA[1,:], 'k')
plt.plot(x_circ[0,:],x_circ[1,:],'k')
plt.plot(x_AD[0,:], x_AD[1,:], 'k')
plt.plot(x_CD[0,:], x_CD[1,:], 'k')
plt.annotate("A",(-0.3,-0.4))
plt.annotate("B",(6.6,-0.5))
plt.annotate("C",(9.15,4.23))
plt.annotate("6.5",(3.25,0.18))
plt.annotate("E",(3.25,5))
plt.annotate("120",(5.9,0.3))
plt.annotate("D",(0.6,10.3))
plt.show()
print("1. Draw a line segment AB of length 6.5 cm.\n"
      "2. Draw a line segment emerging from B at angle 120 in anticlockwise direction from BA of length 5 cm.\n"
      "3. Name the other endpoint of the line segment as C.\n"
      "4. Join AC. This completes the traingle ABC.\n"
      "5. Now take the perpendicular bisector of any two sides, mark their point of intersection as E(centre of circumcircle).\n"
      "6. Taking E as centre and EA=EB=EC as radius draw a circle(circumcircle).\n"
      "7. Take internal angle bisector of AB and BC, let its point of intersection with the circumcircle be D.\n"
      "8. Join AD and CD.")
