import math
import statistics
import numpy as np
from scipy import stats

x = [8.0, 1, 2.5, 4, 28.0]

print(x)

mean = sum(x) / len(x)  # 8.7
print("Mean calculated using simple method:", mean)

mean = statistics.mean(x)  # 8.7
print("Mean calculated using statistics library:", mean)

y = np.array(x)
mean = np.mean(y)  # 8.7
print("Mean calculated using numpy:", mean)


n = len(x)
if n % 2:  # For ODD number of data items
    median_ = sorted(x)[round(0.5 * (n - 1))]
else:  # For EVEN number of data items
    x_ord = sorted(x)
    index = round(0.5 * n)
    median_ = 0.5 * (x_ord[index - 1] + x_ord[index])
    
print("Median calculated using simple method:", median_)  # 4

median_ = statistics.median(x)  # 4
print("Median calculated using statistics library:", median_)

y = np.array(x)
median_ = np.median(y)  # 4
print("Median calculated using numpy:", median_)


u = [2, 3, 2, 8, 12]  # Lets change the data to this one
print()
print(u)

mode_ = max((u.count(item), item) for item in set(u))[1]
print("Mode calculated using simple method:", mode_)  # 2

mode_ = statistics.mode(u)  # 2
print("Mode calculated using statistics library:", mode_)

w = np.array(u)
mode_ = stats.mode(w).mode  # Use scipy.stats.mode to get the mode
print("Mode calculated usin scipy:", mode_)