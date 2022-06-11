import numpy as np

aryA = np.array([1, 2, 3, 4, 5])
aryB = np.array([6, 7, 8, 9, 10])

print(aryA + aryB)
print(aryA - aryB)
print(aryA * aryB)
print(aryA / aryB)

import matplotlib.pyplot as plt

plt.plot([2, 4, 6, 8], [8, 10, 3, 6])
plt.show()

import turtle as t

colors = ['red', 'orange', 'blue', 'green', 'yellow', 'purple']
t.setup(500, 400)
t.bgcolor('black')
t.speed(100)

for i in range(180):
    t.pencolor(colors[i % len(colors)])
    t.width(i / 100 + 1)
    t.forward(i)
    t.left(59)

