# Напишите функцию min_max_dist, которая принимает на вход неограниченное число векторов через запятую. Гарантируется, что все векторы, которые передаются, одинаковой длины.
# Функция возвращает минимальное и максимальное расстояние между векторами в виде кортежа.

# Пример:

#vec1 = np.array([1,2,3])
#vec2 = np.array([4,5,6])
#vec3 = np.array([7, 8, 9])
 
#min_max_dist(vec1, vec2, vec3)
# (5.196152422706632, 10.392304845413264)

import numpy as np

vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])

def min_max_dist(*vectors):
    
    min_distances = []
    max_distances = []
    
    for v in vectors:
        
        n = 0
        distances = []
        
        while n < len(vectors):
            dist = np.linalg.norm(v - vectors[n])
            if dist:
                distances.append(dist)
            n += 1

        min_distances.append(min(distances))
        max_distances.append(max(distances))
    
    return (min(min_distances), max(max_distances))

print (min_max_dist(vec1, vec2, vec3))

