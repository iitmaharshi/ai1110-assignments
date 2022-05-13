import numpy as np

Bags = np.array([0]+[1]+[2])

N = 10000

selecting_Bag = np.random.choice(Bags, size=N)
uniq, count = np.unique(selecting_Bag, return_counts=True)
arr = dict(zip(uniq, count))
ProbB1 = arr[0]
ProbB2 = arr[1]
probB3 = arr[2]

#1 denotes silver and 0 denotes gold
Bag1 = np.array([1]*0 + [0]*2)
Bag2 = np.array([1]*2 + [0]*0)
Bag3 = np.array([1]*1 + [0]*1)

#for first bag
ballcolor1 = np.random.choice(Bag1, size=N)
uniq1, count1 = np.unique(ballcolor1, return_counts=True)
arr1 = dict(zip(uniq1, count1))
ProbB1_gold = arr1[0]

#for second bag
ballcolor2 = np.random.choice(Bag1, size=N)
uniq2, count2 = np.unique(ballcolor2, return_counts=True)
arr2 = dict(zip(uniq2, count2))
ProbB2_gold = arr2[0]

#for third bag
ballcolor3 = np.random.choice(Bag1, size=N)
uniq3, count3 = np.unique(ballcolor3, return_counts=True)
arr3 = dict(zip(uniq3, count3))
ProbB2_gold = arr3[0]

Req_prob = (ProbB1*ProbB1_gold)/(ProbB2*ProbB2_gold+ProbB1*ProbB1_gold)

print("Practical probability is ", Req_prob)