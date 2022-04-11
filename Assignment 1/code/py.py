import matplotlib.pyplot as plt
import mpmath as mp
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

c = 6.5
a = 5
theta = np.pi/3
alpha = mp.acot(11*3**0.5/13)
e1 = np.array(([1,0]))
l = 6.5*3**0.5/(2*mp.sin(alpha))

A = np.array(([0,0]))
B = c*e1
C = np.array(([6.5+a*mp.cos(theta),a*mp.sin(theta)]),dtype = 'float64')
E,r = ccircle(A,B,C)
D = l*np.array((mp.cos(2*np.pi/3 - alpha),mp.sin(2*np.pi/3 - alpha)),dtype = 'float64')


x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_circ = circ_gen(E,r)
x_AD = line_gen(A,D)
x_CD = line_gen(C,D)


plt.plot(x_AB[0,:], x_AB[1,:], 'k')
plt.plot(x_BC[0,:], x_BC[1,:], 'k')
plt.plot(x_CA[0,:], x_CA[1,:], 'k')
plt.plot(x_circ[0,:],x_circ[1,:],'k')
plt.plot(x_AD[0,:], x_AD[1,:], 'k')
plt.plot(x_CD[0,:], x_CD[1,:], 'k')

tri_coords = np.vstack((A,B,C,E,D)).T
plt.scatter(tri_coords[0,:], tri_coords[1,:])
vert_labels = ['A','B','C','E','D']
for i, txt in enumerate(vert_labels):
    plt.annotate(txt, # this is the text
                 (tri_coords[0,i], tri_coords[1,i]), # this is the point to label
                 textcoords="offset points", # how to position the text
                 xytext=(0,5), # distance from text to points (x,y)
                 ha='left') # horizontal alignment can be left, right or center

plt.show()

print("1.The point A is taken as origin and a line segment AB = 6.5 cm is drawn along positive x-axis.\n"
     "2. Draw a line segment emerging from B at angle 120 in anticlockwise direction from BA of length 5 cm.\n"
     "3. Name the other endpoint of the line segment as C.\n"
     "4. Join AC. This completes the triangle ABC.\n"
     "5. Now take the perpendicular bisector of any two sides, mark their point of intersection as E(centre of circumcircle).\n"
     "6. Taking E as centre and EA=EB=EC as radius draw a circle(circumcircle).\n"
     "7. Take internal angle bisector of AB and BC, let its point of intersection with the circumcircle be D.\n"
     "8. Join AD and CD.")


