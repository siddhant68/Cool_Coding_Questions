from random import randint

count = 10000
l = [0] * 6
for i in range(count):
    n = randint(0, 5) 
    l[n] += 1

d = {}
for i in range(len(l)):
    d[i+1] = l[i]/count

print(d)
