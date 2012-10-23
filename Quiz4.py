import numpy as np

for i in np.arange(2,5):
    print i

x = range(2,5)
for j in x:
    print j

for j in x:
    print x

for i in np.arange(10,1,-1):
    print i

sum = 0;
for i in range(1,6):
    sum = sum + i
print "sum=", sum

x = [2, 5, 3]
sum = 0;
for i in range(len(x)):
    sum = sum + x[i]
print "sum=", sum

x = [2, 5, 3]
sum = 0
for i in x:
    sum = sum + i
print "sum=", sum

x = range(1,5)
a = 0
for i in range(len(x)):
    a = a + x[i]
print "a=",a

x = np.arange(3,6)
y = np.arange(-1,2)
for i in range(len(y)):
    y[i] = x[i]**2;
print "y=",y

f = [1, 1]
for i in range(2, 8):
    f.append(f[i-1] + f[i-2])
print "f=", f

f2 = [1, 1]
for i in range(2, 8):
    f2.append(f2[-1] + f2[-2])
print "f2=", f2

for x in range(3):
    print x
    for y in range(3,6):
        print x, y

for x in range(3):
    print 'yes'
    for y in range(3,6):
        print 'no'

n = 3
while n <= 9:
    print n
    n = n + 1


i = 5*4
while i < 10:
    print 'here'
    i = i - 5