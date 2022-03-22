from weather import *
from user import *
from engine import *

import numpy as np
A=np.array([[2,2,3],[1,0,4],[6,9,7]])
B=np.array([[1,5,2],[6,6,4],[1,10,7],[5,8,2],[3,0,6]])
def csm(A,B):
    num=np.dot(A,B.T)
    p1=np.sqrt(np.sum(A**2,axis=1))[:,np.newaxis]
    p2=np.sqrt(np.sum(B**2,axis=1))[np.newaxis,:]
    return num/(p1*p2)
print(csm(A,B))
