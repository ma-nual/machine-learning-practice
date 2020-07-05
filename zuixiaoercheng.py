import numpy as np
import matplotlib.pyplot as plt
import math

def calcAB(x,y):
    n = len(x)
    sumX, sumY, sumXY, sumXX = 0, 0, 0, 0
    for i in range(0, n):
        sumX += x[i]
        sumY += y[i]
        sumXX += x[i] * x[i]
        sumXY += x[i] * y[i]
    a = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX)
    b = (sumXX * sumY - sumX * sumXY) / (n * sumXX - sumX * sumX)
    return a, b

xi = [1,2,3,4,5,6,7,8,9,10]
yi = [20.52,27.53,29.84,36.92,38.11,37.21,40.96,46.37,49.78,50.22]
a,b=calcAB(xi,yi)
print("y = %10.5fx + %10.5f" %(a,b))
x = np.linspace(0,10)
y = a * x + b
plt.plot(x,y)
plt.scatter(xi,yi)
plt.show()

E = 0
for i in range(0,10):
    E = E + (a*xi[i]+b-yi[i]) ** 2
Et = math.sqrt(E)/10
print("Et=%f" %Et)

x1 = [11,12,13]
y1 = [0,0,0]
for j in range(0,3):
    y1[j] = a * x1[j] + b
for j in range(0,3):
    print(y1[j])

E1 = 0
ym = [52.38,55.66,58.31]
for j in range(0,3):
    E1 = E1 + (y1[j]-ym[j]) ** 2
Ep = math.sqrt(E1)/3
print("Ep=%f" %Ep)



