import matplotlib.pyplot as plt

# read file here

#best
x = [100,1000,10000,50000,80000,100000]
y1= [0.008077,0.0020055,0.016226,0.19692,0.332246,0.39721] 
y2= [0.000998,0.00100517,0.0068874,0.004068,0.015318,0.02077]
y3= [0.00049018,0.00100064,0.015257,0.166431,0.167348,0.19646]
y4= [0.00100064,0.188725,0.015818,0.080847,0.132927,0.20044]

plt.plot(x, y1, color='red', label='Heap')
plt.plot(x, y2, color='blue',label='Pigeon')
plt.plot(x, y3, color='black',label='Quick. Not continues')
plt.plot(x, y4, color='orange',label='Radix')

plt.show()