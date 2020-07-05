import numpy as np
from  scipy.stats import ttest_rel
import pandas as pd
from scipy.stats import f_oneway

A1 = [0.9856,0.6244,0.7888,0.9231,0.9617,0.5687]
B1 = [0.8257,0.8665,0.7234,0.9621,0.7695,0.8423]
#求均值
A1_mean = np.mean(A1)
B1_mean = np.mean(B1)
#求标准差
A1_std = np.std(A1,ddof=1)
B1_std = np.std(B1,ddof=1)
print("A算法准确率的平均值为：%f" % A1_mean)
print("B算法准确率的平均值为：%f" % B1_mean)
print("A算法的标准差为:%f" % A1_std)
print("B算法的标准差为:%f" % B1_std)
#配对样本t检验
print(ttest_rel(A1, B1))
#anova分析
f,p = f_oneway(A1,B1)
print("f=%f" %f)
print("p=%f" %p)

