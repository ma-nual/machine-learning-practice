import numpy as np

x1 = np.array([1,2,3,4,5,6,7,8,9,10])
x2 = np.array([0.5,2.6,3.5,6.7,8.9,9.2,11.5,15.8,19.6,20.1])

y = np.array([20.52,27.53,29.84,36.92,38.11,37.21,40.96,46.37,49.78,50.22])

X = np.mat(np.array([x1,x2]))

X1 = np.dot(X.T,X)

w = np.dot(np.log(np.mat(y)),np.dot(X1.I,X.T))

y1 = np.dot(np.mat(w),X)

b = np.sqrt((np.log(y)-np.log(y1))*(np.log(y)-np.log(y1)))/10
