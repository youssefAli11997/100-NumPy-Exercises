#01
import numpy as np

#02
print(np.__version__)
np.show_config()

#03
z = np.zeros(10)
print(z)

#04
python3 -c "import numpy; numpy.info(numpy.add)"

#05
x = np.zeros(10)
x[4] = 1
print(x)

#06
vec = np.array(range(10,50))
print(vec)
#or # the same
vec = np.arange(10,50)
print(vec)

#07
vec = np.arange(1,6)
vec2 = vec[::-1]
print(vec)
print(vec2)
