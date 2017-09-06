#01
import numpy as np

#02
print(np.__version__)
np.show_config()

#03
z = np.zeros(10)
print(z)

#04
#python3 -c "import numpy; numpy.info(numpy.add)"

#05
x = np.zeros(10)
x[4] = 1
print(x)

#06
vec = np.array(range(10,50))
print(vec)
#or #the same result
vec = np.arange(10,50)
print(vec)

#07
vec = np.arange(1,6)
vec2 = vec[::-1]
print(vec)
print(vec2)

#08
rng = range(0,9)
arr = np.array([rng[:3],rng[3:6],rng[6:]])
print(arr)
#or #the same result
arr = np.arange(9).reshape(3,3)
print(arr)

#09
vec = np.nonzero([1,2,0,0,4,0])
print(vec)

#10
vec = np.eye(3)
print(vec)

#11
arr = np.random.random((3,3,3))
print(arr)

#12
arr = np.random.random((10,10))
print(arr, arr.min(), arr.max())

#13
vec = np.floor(np.random.random((30)) * 50)
print(vec)
print(np.mean(vec))

#14
vec = np.ones((5,5))
vec[1:-1, 1:-1] = 0
print(vec)

#15
"""
nan
false
false
nan
false
"""
