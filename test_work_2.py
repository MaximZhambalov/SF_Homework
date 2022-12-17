import numpy as np

# arr = np.array([1,5,2,9,10], dtype=np.int8)

 #nd_arr = np.array([
 #              [12, 45, 78],
 #              [34, 56, 13],
 #              [12, 98, 76]
 #              ], dtype=np.int16)

#arr, step = np.linspace(-6, 21, 60, endpoint=False, retstep=True)
#print (step)

#a = np.float16(np.random.rand(1))
#print (a, a.itemsize)

def get_chess(a):
    temp = np.zeros((a,a))
    b = 1
    while b < a:
        temp[b, ::2] = 1
        temp[::2, b] = 1
        b += 2
    return temp

def get_chess_2(a):
    temp = np.zeros((a,a))
    temp[1::2, ::2] = 1
    #temp[::2, 1::2] = 1
    return temp

print (get_chess_2(10))


