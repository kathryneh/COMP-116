import numpy as np
import pylab
import time
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
print ' '
print 'Hypothesis:' 
print ' My hypothesis is that it will take longer to type incorrectly spelled' 
print 'words than it will take to type correctly spelled words' 
print ' '
print '  '
time.sleep(2)
print ' Experimental Procedure:' 
print 'My experimental procedure is that I have compiled a list of 54 correctly ' 
print 'spelled words, and 54 incorrectly spelled versions of the same words '
print 'used for the correctly spelled list. '
print'I then created a for loop that will run for 100 rounds and it will' 
print 'randomly select either a correctly or incorrectly spelled word to print for the' 
print 'user to type. If the user types the word correctly, the time will be saved. If ' 
print 'the user types the word incorrectly, it will not be saved.'

print 'I then analyzed it by creating a histogram, and I plotted the resulting normal' 
print 'distribution expected from the mean and standard deviation of the times for ' 
print 'both the correct and incorrect data sets.' 
print ' '

time.sleep(5)
print 'Results:'
print 'As shown by the resulting histogram, the correctly spelled words do have a much' 
print 'narrower distribution than the incorrectly spelled words, and the concentration' 
print 'of data points for the correctly spelled words is thus much lower in time than ' 
print 'the incorrectly spelled words, which have a larger distribution and a higher'
print 'mean time than the correctly spelled words. From this data, I would assume '
print 'that my hypothesis is supported. ' 

correctTime = []
incorrectTime = []
for line in file('correcttime.txt', 'r'):
    correctTime.append(float(line[0:9]))
correct=np.array(correctTime)
for line in file('incorrecttime.txt', 'r'):
    incorrectTime.append(float(line[0:9]))
incorrect=np.array(incorrectTime)
    
import matplotlib.pyplot as plt

cMean=np.mean(correctTime)
iMean=np.mean(incorrectTime)
cSTD=np.std(correctTime)
iSTD=np.std(incorrectTime)

muC, sigmaC = cMean, cSTD
muI, sigmaI = iMean, iSTD

# the histogram of the data
n1, bins1, patches1 = plt.hist(correctTime, 50, normed=1, facecolor='green', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins1, muC, sigmaC)
l = plt.plot(bins1, y, 'green', linewidth=2)

plt.xlabel('Time (seconds)')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
plt.grid(True)

# the histogram of the data
n2, bins2, patches2 = plt.hist(incorrectTime, 50, normed=1, facecolor='blue', alpha=0.75)

# add a 'best fit' line
y = mlab.normpdf( bins2, muI, sigmaI)
l = plt.plot(bins2, y, 'blue', linewidth=2)


plt.title(r'Histogram of Typing Data: Incorrect/Correctly Spelled words vs Time')
plt.axis([0, 7, 0, 1.5])
plt.grid(True)
plt.legend( ('Correct', ('Incorrect') ))
plt.show()

