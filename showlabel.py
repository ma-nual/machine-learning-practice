from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from pylab import*
mpl.rcParams['font.sans-serif'] = ['SimHei']

ax = plt.subplot(111,projection = '3d')
ax.scatter(1,1,2,c='g',label='好瓜')
ax.scatter(2,1,1,c='g')
ax.scatter(1,3,3,c='r',label='坏瓜')
ax.scatter(2,2,1,c='r')
ax.legend()
ax.set_xlim(0,3)
ax.set_ylim(0,3)
ax.set_zlim(0,3)
ax.set_xlabel('色泽')
ax.set_ylabel('根蒂')
ax.set_zlabel('敲声')
plt.show()



