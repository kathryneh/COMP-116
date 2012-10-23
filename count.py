import numpy as np
count=np.zeros(100)
A=np.random.random_integers(0,100,10)
def count_ints(A):
	'''return a histogram with the number of times each int occurs in A'''
	#count them
	Amax=A.max()
	Amin=A.min()
	number_of_counters = Amax - Amin + 1
	count=np.zeros(number_of_counters)
	for i in A:
		k=i-Amin
		count[k] = count[k] + 1
	#print them out	
	j=Amin
	for c in count:
		if c !=0:
			print j, c
		j=j+1