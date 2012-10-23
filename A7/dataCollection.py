# nice hypothesis and excellent graph
# Grade 90/100
# -5 break after 20 or so trials
# -5 analysis of accuracy

import random
import time 
import numpy as np

incorrect=[]
correct=[]
fp=file('incorrectlist.txt','r')
for line in fp:
    incorrect1=line.strip()
    incorrect.append(incorrect1)


fp2=file('correctlist.txt','r')
for line in fp2:
    correct1=line.strip()
    correct.append(correct1)


random.shuffle(correct)
random.shuffle(incorrect)



lencorrect=len(correct)
lenincorrect=len(incorrect)

correct=np.array(correct)
incorrect=np.array(incorrect)
print "Hello, and thank you for participating in Katie Hawthorne's COMP 116 assignment."
time.sleep(1.5)
print "Today, you will be going through a collection of runs of incorrectly and "
print "correctly spelled prompt words; your job is to re-type the prompts exactly, "
print "and as quickly as possible."

time.sleep(2.5)
print "If you misspell a word, do not despair--it won't be saved in the time data."
print " "
print "Ready?"
raw_input ('Please hit enter to continue')
time.sleep(.5)
 
for i in range(1,100):
    if i%2==0:
        entry = correct[random.randint(0,lencorrect-1)]
        t1=time.time()
        print 'Please type the following word exactly and press enter'
        print " "
        input= raw_input(entry + '\n')
        for j in correct:
            if input == j in correct:
                fp=file('correcttime.txt', 'a')
                t2=time.time()
                dp=file('correctwords.txt', 'a')
                print>>fp, t2-t1
                print>>dp, input, t2-t1 
                    
    if i%2==1:
        entry = incorrect[random.randint(0,lenincorrect-1)]
        t1=time.time()
        print 'Please type the following word exactly and press enter'
        input= raw_input(entry + '\n')
        for j in incorrect:
            if input == j in incorrect:
                fp=file('incorrecttime.txt', 'a')
                dp=file('incorrectwords.txt', 'a')
                t2=time.time()
                print>>dp, input, t2-t1
                print>>fp, t2-t1
                
print 'Thank you, please play again!'
