# coding: utf-8


import time


a = []
t0 = time.perf_counter()
for i in range(1, 20000):
    a.append(i)
print(time.perf_counter() - t0, "seconds process time")

t0 = time.perf_counter()
b = [i for i in range(1, 20000)]
print(time.perf_counter() - t0, "seconds process time")

c = [i**2 for i in range(1, 10)]
d = [j+1 for j in range(1, 10)]
e = [n for n in range(1, 10) if n % 2 == 0]
f = [letter.lower() for letter in 'ABCDEFGHIJKLMN']

g = {i: i+1 for i in range(4)}
h = {i: j for i, j in zip(range(1, 6), 'abcde')}
i = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}

k = [letter for letter in 'abcdefg']
for num, letter in enumerate(k):
    print(letter, 'is', num + 1)
