import matplotlib.pylab as plt

# 绘制简单的曲线
# plt.plot([1,3,5],[4,8,10])
# plt.show()

import numpy as np
# x = np.linspace(-np.pi, np.pi, 100)
# plt.plot(x, np.sin(x))
# plt.show()

# x = np.linspace(-np.pi*2, np.pi*2, 100)
# plt.figure(1,dpi=50)
# for i in range(1,5):
#     plt.plot(x, np.sin(x/i))
# plt.show()

# plt.figure(1, dpi=50)
# data = [1, 2, 3, 8, 9]
# plt.hist(data)
# plt.show()

x=np.arange(1,10)
y=x
fig=plt.figure()
plt.scatter(x,y,c='r',marker='o')
plt.show()
