'''Assignment 4 Water Data'''

# Author: Kathryne Hawthorne 
# Collaborators: Sean Curtis, Emily

# this script will run as is but, of course, it doesn't yet produce
# the desired results. Your mission is to modify it to get the outputs
# requested.

import numpy as np
import pylab

# read the data

# depth: a 276 by 2 array with depth of Jordan and Falls lakes
# for each month from Jan 1985 to Dec 2007, which is 23 years.
# Data that is not available is NaN. 
depth = np.loadtxt('depth.txt')
Jordan=depth[:,0]
Falls=depth[:,1]
# rain: a 276x2 array with total rainfall in inches for each month
rain = np.loadtxt('rain.txt')

# hawgage: a 365x4 array of daily average river or lake height (ft) at
# Haw River, Bynum, and above & below the Jordan Lake Dam by Moncure.
# (These sites are listed upstream to downstream, but the gauges are
# not in that order.)
hawgage = np.loadtxt('hawgage.txt')

# hawrain: a 365x2 array of daily rainfall (in) measured at two
# rain gauges from 29 Aug 07 - 28 Aug 08.
hawrain = np.loadtxt('hawrain.txt')

# 1. Plot a line graph of depths for both lakes.  (Is there an obvious yearly cycle?)
pylab.plot(depth)
pylab.show()
# put the appropriate call here to plot the depths

# these show how to label the figure
pylab.title('Depth of Jordan and Falls lakes')
pylab.ylabel('Depth (feet)')
pylab.xlabel('Months starting with Jan 1985')
pylab.savefig('Fig1.png')

# -2 Image not saved.

# close that figure so we can start another
pylab.close()

# 2. The targets for Jordan and Falls lakes are 216ft and 251.5ft, respectively.  For how many months was each lake over its target?

# include the code here to compute and print the answer.
JordanTarget=216
FallsTarget=251.5
JordanOverTarget =  np.sum(Jordan>JordanTarget) # replace this with some expression
print 'Months Jordan lake was over its target =', JordanOverTarget

FallsOverTarget =  np.sum(Falls>FallsTarget) # replace this with some expression
print 'Months Falls lake was over its target =', FallsOverTarget

# 3. Plot the rain in August as a line graph over years for both lakes.
Aug=7
AugustRain=rain[Aug::12]
pylab.plot(AugustRain)
pylab.show()

# include code to plot the figure with some nice labels as above

pylab.title('Rain in August for Jordan and Falls lakes')
pylab.savefig('Fig2.png')
pylab.close()

# 4. Compute the average height that Falls Lake is above its target
# for each month over the 23 years from 1985-2007, and display as bar
# chart with a bar for each month.  Plot the line for 2007 in red on
# top of this bar chart.

# put code here to compute FallsByMonth
FallsHeightOverTarget=(Falls-FallsTarget)
FHOT=FallsHeightOverTarget.reshape(23,12)
FHOTmean=FHOT.mean(axis=0)

# then you can create a bar chart of it like this:
pylab.bar(np.arange(1,13), FHOTmean, 1, align='center') 
# pylab.bar(np.arange(1,13), FallsByMonth, align='center')
#pylab.plot(np.arange(1,13),-'r')
# then plot a line in red on top of that with a call to plot like this:
print "FallsHeightOverTarget SIZE:", FallsHeightOverTarget.shape

pylab.plot(np.arange(1,13),FHOT[22,:], 'r')

pylab.title('Average Falls lake depth 85-07, and line for 2007')
pylab.ylabel('Height above target(ft)')
pylab.xlabel('Month')
pylab.savefig('Fig3.png')
pylab.close()

# 5. Determine how many days had more than 1 in of precipitation at
# the two sites in hawrain, and how many days had less than 1/4 in.

#this is based on the assumption that both sites have to have more 
#than one inch of rain, or both sites have less than .25inches of
#rain. 

A=hawrain[:,0]
B=hawrain[:,1]

Over= hawrain >1
Over=np.logical_and(Over[:,0],Over[:,1])
Under= hawrain<.25
Under=np.logical_and(Under[:,0], Under[:,1])
DaysOver=np.sum(Over)
DaysUnder=np.sum(Under)

# your code goes here

print 'Days with more than 1 inch of rain=', DaysOver
print 'Days with less than .25 inches of rain=', DaysUnder



# 6. Plot line graphs showing the cumulative amount of rain over the
# past year at both sites.  Which of the two locations (1 or 2)
# received the most rain?


# You'll find the numpy function "cumsum" useful for this one
# put your code here

A2= np.sum(A)
B2= np.sum(B)

print 'Cumulative Rainfall at Point A', A2
print 'Cumulative Rainfall at Point B', B2
#may need to fix this later!
print 'Location 2 has a higher Cumulative Rainfall'
#think about np.argmax
pylab.plot (np.cumsum(hawrain, 0))
pylab.title('Cumulative Rainfall')
pylab.xlabel('Days since 28Aug07')
pylab.ylabel('Cumulative rainfall (in)')
pylab.savefig('Fig4.png')
pylab.close()


# 7. Determine the lowest height for each gauge, and create an array
# of adjusted heights by subtracting the corresponding lowest heights.
# Plot these adjust heights as a line graph.

# compute the adjusted heights
GaugeLow=np.min(hawgage, 0)
AdjustedGauge=hawgage-GaugeLow
pylab.plot(AdjustedGauge)
# and then plot them using commands similar to above
pylab.title('Adjusted gauge heights')
pylab.xlabel('Days since 28Aug07')
pylab.ylabel('Height above min (ft)')
pylab.savefig('Fig5.png')
pylab.close()

# 8. Determine the maximum increase and maximum decrease in height
# from one day to the next for each of the four gauges in hawgage.
GaugeNextDay=hawgage[1:]
GaugePrevDay=hawgage[:-1]
DGauge=GaugeNextDay-GaugePrevDay
MaxDGauge=np.max(DGauge,0)
MinDGauge=np.min(DGauge,0)
# your code goes here


print 'Maximum one-day change in height for the four gauges respectively=', MaxDGauge
print 'Minimum one-day change in height for the four gauges respectively=', MinDGauge
#print the array of four 
