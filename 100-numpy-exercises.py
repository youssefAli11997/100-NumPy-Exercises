#001
import numpy as np

#002
print(np.__version__)
np.show_config()

#003
z = np.zeros(10)
print(z)

#004
z = np.array([1,2,3,4,5])
print("%d bytes" %(z.size * z.itemsize))

#005
#python3 -c "import numpy; numpy.info(numpy.add)"

#006
x = np.zeros(10)
x[4] = 1
print(x)

#007
vec = np.array(range(10,50))
print(vec)
#or #the same result
vec = np.arange(10,50)
print(vec)

#008
vec = np.arange(1,6)
vec2 = vec[::-1]
print(vec)
print(vec2)

#009
rng = range(0,9)
arr = np.array([rng[:3],rng[3:6],rng[6:]])
print(arr)
#or #the same result
arr = np.arange(9).reshape(3,3)
print(arr)

#010
vec = np.nonzero([1,2,0,0,4,0])
print(vec)

#011
vec = np.eye(3)
print(vec)

#012
arr = np.random.random((3,3,3))
print(arr)

#013
arr = np.random.random((10,10))
print(arr, arr.min(), arr.max())

#014
vec = np.floor(np.random.random((30)) * 50)
print(vec)
print(np.mean(vec))

#015
vec = np.ones((5,5))
vec[1:-1, 1:-1] = 0
print(vec)

#016
vec = np.floor(np.random.random((5,5)) * 50 + 1)
vec = np.pad(vec, pad_width=1, mode="constant", constant_values=0)
print(vec)

#017
"""
nan
false
false
nan
false
"""

#018
vec = np.diag(np.arange(1,5), k=-1)
print(vec)

