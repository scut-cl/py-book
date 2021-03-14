# 数组调整27-arrar_reshape.py
import numpy as np
ar1 = np.arange(1, 25)
# 调整形状
print("np.reshape(ar1,(3,8)):\n", np.reshape(ar1, (3, 8)))
print("ar1.reshape((3,8)):\n", ar1.reshape((3, 8)))
print("ar1.reshape((2,12)):\n", ar1.reshape((2, 12)))
# 折叠为一维数组
ar2 = ar1.reshape((2, 12))
print("ar2:", ar2)
print("ar2_11:", np.ndarray.flatten(ar2))  # 默认order='C',行为主序
print("ar2_12:", ar2.flatten(order='F'))  # 列为主序
print("ar2_13:", ar2.ravel(order='F'))  # 创建视图优先
print("ar2_14:", np.ndarray.ravel(ar2))
# 数组转置
arT = np.array([[1, 2, 3], [4, 7, 9]])
print("arT1:", arT.T)
print("arT2:", np.ndarray.transpose(arT))
ar1 = np.array([1, 2, 3])
print("ar1.T:", ar1.T)  # 一维数组无转置效果
ar1_2 = np.array([[1, 2, 3]])
print("ar1_2.T:", ar1_2.T)
ar1_22 = np.array([1, 2, 3], ndmin=2)
print("ar1_22.T:", ar1_22.T)
