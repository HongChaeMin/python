import math
clst = list(map(math.ceil, [1.1, 2.2, 3.3, 4.4, 5.5, 6.6]))
print(f'map(math.ceil, list) : {clst}')

lst = [1.1, 2.2, 3.3, 4.4, 5.5]
mlst = list(map(int, lst))
print(f'map(int, list) : {mlst}')

lst = [1, 2, 3, 4, 5]
plst = list(map(lambda  x, y: x * y, lst, lst))
print(f'map(lambda, list) : {plst}')

