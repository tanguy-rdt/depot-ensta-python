import numpy as np
import matplotlib.pyplot as plt

a=[1.0, 1.02, 1.05, 1.07, 1.1, 1.12, 1.15, 1.18, 1.2, 1.23, 1.26, 1.29, 1.32, 1.35, 1.38, 1.42, 1.45, 1.48, 1.52, 1.56, 1.59, 1.63, 1.67, 1.71, 1.75, 1.79,
1.83, 1.87, 1.92, 1.96, 2.01, 2.06, 2.1, 2.15, 2.21, 2.26, 2.31, 2.36, 2.42, 2.48, 2.54, 2.6, 2.66, 2.72, 2.78, 2.85, 2.92, 2.98, 3.05, 3.13, 3.2,
3.27, 3.35, 3.43, 3.51, 3.59, 3.68, 3.76, 3.85, 3.94, 4.04, 4.13, 4.23, 4.33, 4.43, 4.53, 4.64, 4.75, 4.86, 4.98, 5.09, 5.21, 5.34, 5.46, 5.59,
5.72, 5.86, 5.99, 6.14, 6.28, 6.43, 6.58, 6.73, 6.89, 7.05, 7.22, 7.39, 7.56, 7.74, 7.92, 8.11, 8.3, 8.5, 8.7, 8.9, 9.11, 9.33, 9.55, 9.77, 10.0]


b=[2.51, 2.75, 3.71, 2.28, 2.13, 1.92, 4.28, 2.31, 3.31, 1.77, 4.32, 2.25, 5.5, 2.31, 2.83, 3.72, 2.63, 6.28, 6.08, 6.91, 6.89, 3.22, 4.29, 5.87, 4.7,
4.49, 5.24, 6.84, 8.54, 6.83, 8.94, 11.2, 7.66, 12.65, 7.52, 14.32, 13.53, 10.69, 5.93, 15.08, 18.23, 20.04, 12.13, 18.32, 21.33, 15.16, 12.49,
10.88, 22.25, 15.39, 20.57, 14.61, 30.77, 19.6, 33.46, 26.79, 41.86, 53.54, 40.62, 48.61, 64.58, 33.77, 81.54, 62.5, 79.17, 94.5, 133.09,
83.2, 83.37, 182.57, 186.02, 196.24, 123.59, 178.63, 325.9, 213.13, 446.09, 599.6, 363.89, 505.19, 909.76, 596.79, 1063.83, 1335.95,
1521.91, 787.45, 1856.59, 2884.75, 2633.02, 1564.78, 3285.46, 4193.35, 4748.44, 4035.98, 5373.65, 6705.32, 15623.23, 19650.54,
23973.92, 27795.41]

plt.plot(a, b, 'r')
plt.xlabel('année [10^(-3)]')
plt.ylabel('nbr de personne')
plt.title('Evolution de la population')
plt.grid()
plt.show()

fig, subplot = plt.subplots()
subplot.semilogx(a, b, 'r')
fig.suptitle('Evolution de la population')
subplot.set(xlabel=('semi-log'), ylabel=('nbr de personne'))
subplot.grid()
plt.show()

fig, (subplot1, subplot2) = plt.subplots(2, 1)
fig.suptitle('Evolution de la population')
subplot1.plot(a, b, '-r')
subplot1.label_outer()
subplot1.set(xlabel=('année [10^(-3)]'), ylabel=('nbr de personne'))
subplot1.grid()
subplot2.semilogx(a, b, 'tab:orange')
subplot2.set(xlabel=('semi-log'), ylabel=('nbr de personne'))
subplot2.grid()
plt.show()

