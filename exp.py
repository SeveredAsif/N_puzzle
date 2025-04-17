# numbers = [1,2,3,4,5,6,7,8,0]
# rows = []
# for i in range(3):
#     rows.append(numbers[i*3:(i+1)*3])

# #print(rows)

import numpy as np # type: ignore
# r = np.array(rows)
# ro = np.hsplit(r,3)

# for x in ro:
#     print(x)

# def ceildiv(a, b):
#     return -(a // -b)

# print(ceildiv(9,3))
array1 = [1,2,3]
array2 = [1,2,3]
print(np.array_equal(array1, array2))
