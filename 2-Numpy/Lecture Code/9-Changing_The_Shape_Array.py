import numpy as np
a = np.floor(10*np.random.random((3,4)))
print(a)
print(a.shape)
print(a.ravel())
a.shape = (6, 2)
print(a.T)
print(a.resize((2,6)))
print(a.reshape(3,-1))
a= print('#',50*"-")