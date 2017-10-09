#1 . 1D->2D, other case, just use T, transpose.

arr.reshape(ar.shape[0], -1)
#array([ 0.80203158,  0.25762844,  0.67039516,  0.31021513,  0.80701097])
#to 
#array([[ 0.80203158],
#       [ 0.25762844],
#       [ 0.67039516],
#       [ 0.31021513],
#       [ 0.80701097]])

#2. argmax, argmax_top_N

import numpy as np
aa = [1,2,3,2,2,2,6,8,29,20,23,5]
np.argmax(aa)
#>> 8

aa2 = np.argsort(aa)
#aa2.artsort()[-N:][::-1]
aa2.artsort()[-3:][::-1]
#>> [8, 10, 9]
