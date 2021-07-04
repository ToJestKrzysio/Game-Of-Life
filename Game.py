import numpy as np
import time

a = np.ones((40000, 40000), dtype=int)

b = np.zeros_like(a)
x, y = 1, 0

start = time.time()
b[:, 1:] += a[:, 0:-1]  # sum for x=+1 and y=0
b[:, 0:-1] += a[:, 1:]  # sum for x=-1 and y=0

b[1:, :] += a[0:-1, :]  # sum for x=0 and y=+1
b[0:-1, :] += a[1:, :]  # sum for x=0 and y=-1

b[1:, 1:] += a[0:-1, 0:-1]  # sum for x=+1 and y=+1
b[1:, 0:-1] += a[0:-1, 1:]  # sum for x=-1 and y=+1
b[0:-1, 1:] += a[1:, 0:-1]  # sum for x=+1 and y=-1
b[0:-1, 0:-1] += a[1:, 1:]  # sum for x=-1 and y=-1
end = time.time()

print(b)
print(f"Execution time {end-start : 0.8f}[s]")


