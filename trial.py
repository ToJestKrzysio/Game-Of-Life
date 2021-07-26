# import numpy as np
# import time
#
# a = np.ones((40000, 40000), dtype=int)
#
# b = np.zeros_like(a)
# x, y = 1, 0
#
# start = time.time()
# b[:, 1:] += a[:, 0:-1]  # sum for x=+1 and y=0
# b[:, 0:-1] += a[:, 1:]  # sum for x=-1 and y=0
#
# b[1:, :] += a[0:-1, :]  # sum for x=0 and y=+1
# b[0:-1, :] += a[1:, :]  # sum for x=0 and y=-1
#
# b[1:, 1:] += a[0:-1, 0:-1]  # sum for x=+1 and y=+1
# b[1:, 0:-1] += a[0:-1, 1:]  # sum for x=-1 and y=+1
# b[0:-1, 1:] += a[1:, 0:-1]  # sum for x=+1 and y=-1
# b[0:-1, 0:-1] += a[1:, 1:]  # sum for x=-1 and y=-1
# end = time.time()
#
# print(b)
# print(f"Execution time {end-start : 0.8f}[s]")

from pydantic import validate_arguments
from typing import Union, List
import numpy as np
if __name__ == "__main__":

    @validate_arguments
    def foo(value: Union[str, int], type: List[str]):
        print(f"{value} {type}")

    foo(1, ["name"])
    foo("123", ["some", "some", "some"])
    foo(1, [[1111], "aaaa"])
