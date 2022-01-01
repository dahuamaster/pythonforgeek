import numpy as np

arr1 = np.array([2,3,4])
print(arr1)
print(arr1.dtype)

arr2 = np.array([1.2,2.3,3.4])
print(arr2)
print(arr2.dtype)

print(arr1+arr2)

# 标量
print(arr2*10)

# 矩阵
data =[[1,2,3],[4,5,6]]
arr3 = np.array(data)
print(arr3)
print(arr3.dtype)

print(np.zeros((3,5)))
print(np.ones((4,6)))
print(np.empty((2,3,2)))

