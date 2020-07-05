import numpy as np
import pandas as pd

dataset = pd.read_csv('作业数据.csv',header=3)
dataset = dataset.iloc[1:14951]
dataset = pd.DataFrame(dataset, columns=['EMG1','EMG2','EMG3','EMG4','EMG5','EMG6','EMG7','EMG8'])
dataset = dataset.T
dataset = pd.DataFrame(data=dataset, dtype=np.float64)
# print(dataset)
mean = dataset.mean(1)
# print(mean)
dataset_mean = dataset.sub(mean,axis=0)
print(dataset_mean)
# dataset_cov = np.cov(dataset_mean)
dataset_cov = np.dot(dataset_mean, dataset_mean.T)
# print(dataset_cov)
dataset_value, dataset_vec = np.linalg.eig(dataset_cov)
dataset_valind = np.argsort(-dataset_value)
# print(dataset_value, dataset_vec)
dataset_sortvalue = dataset_value[dataset_valind]
dataset_vecs = dataset_vec.T
dataset_sortvec = dataset_vecs[dataset_valind]
# print(dataset_sortvalue, dataset_sortvec)
dataset_svec = dataset_sortvec[:7]
# print(dataset_svec)
dataset_pca = np.dot(dataset_svec, dataset_mean)
print(dataset_pca)
'''U, S, V = np.linalg.svd(dataset_cov)
U_reduce = U[:, 0:8].reshape(8, 8)
Z = np.dot(dataset_mean.T, U_reduce)
print(dataset_mean)
dataset_recov = np.dot(U_reduce, Z.T)
print(dataset_recov)'''
dataset_recov = np.dot(dataset_svec.T, dataset_pca)
print(dataset_recov)
dataset_sub = (dataset_recov - dataset_mean)**2
dataset_subl = dataset_sub.sum(1)
dataset_subon = dataset_subl.sum(0)
# print(dataset_subon)
dataset_ori = dataset_mean**2
dataset_oris = dataset_ori.sum(1)
dataset_subund = dataset_oris.sum(0)
dataset_ana = dataset_subon/dataset_subund
print(dataset_ana)
from sklearn.decomposition import PCA
pca_sk = PCA(n_components=7)
dataset_newa = pca_sk.fit_transform(dataset.T)
dataset_new = dataset_newa.T
print(dataset_new)

