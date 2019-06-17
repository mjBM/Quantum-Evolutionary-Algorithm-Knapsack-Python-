import timeit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import string
import math
from Knapsack_quantum import Knapsack_quantum



start = timeit.default_timer()
run = 2                                                         # number of runs
colors = 'red'
iteration=100                                                  #generation or iteration
mean_fitness = [[0 for x in range(iteration)]for j in range(run)]
mean_fitness = np.matrix(mean_fitness)

csv_address1 = "C:\\Users\\majid.mohtasham.MED-EHRU1780SS1\\Google Drive\\QEA_Python\\100.txt"    # office path
# csv_address1 = "C:\\Users\\Majid\\Google Drive\\QEA_Python\\100.txt"                            # laptop parh

temp = np.loadtxt(str(csv_address1) ,dtype=int, delimiter=(" "), unpack=True)                      #read from csv file
capacity = temp[0][0]                                           # assigning the capacity from the text file
temp = temp.transpose()                                         # transpose due to we need 2 columns
temp = np.delete(temp, (0), axis=0)                              # picking up the capacity from the begining the data
knapsack_input=temp
profits=knapsack_input[:,0]
profits = np.matrix(profits)
weights=knapsack_input[:,1]
weights = np.matrix(weights)
repair_type=2      #type=1 random . type=2 greedy . type=3 none
penalty_type=3     #type=1 linear . type=2 logarithm . type=3 none
x=np.arange(1,iteration+1,1)
teta=0.01*np.pi       #Q gate
H_gate=0.01        #epsilon
agent_number=25

for i in range(run):
    mean_fitness[i,:] = Knapsack_quantum(agent_number,profits,weights,capacity,H_gate,repair_type,penalty_type,iteration,teta)
    print('End of Run',i+1,'th')


y = mean_fitness.mean(0)
y = np.asarray(y)
print('The best answer= ',y[0,-1])
x = np.arange(0,iteration,1)
plt.plot(x,y[0,:],'b')
plt.show()
# xlabel('All Iterations') ;                plot configurations
# ylabel('Fitness Mean') ;
# title('All Quantum Genetic Algorithm') ;
# disp('Allruntime=')









stop = timeit.default_timer()
print('run Time : ',stop - start)
