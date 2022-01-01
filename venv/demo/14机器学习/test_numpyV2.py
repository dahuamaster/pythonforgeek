import numpy as np

arr1 = np.arange(10)
print(arr1[5:8])
arr1[5:8] = 10
print(arr1)

arr_slice =arr1[5:8].copy()
arr_slice[:]=15
print(arr1)
print(arr_slice)

