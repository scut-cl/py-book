#line-programing
import numpy as np
from scipy import optimize
c=np.array([4,3])
a=np.array([[2,1],[1,1]])
b=np.array([10,8])
x_opt=optimize.linprog(c,a,b,bounds=((0,None),(0,7)))