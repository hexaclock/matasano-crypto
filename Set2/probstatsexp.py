import sys
sys.path.append('../Set1/')
from mycrypto import *



def randmult(numbers):
	randa = numbers[getrandnum(0,len(numbers)-1)]
	j = randa
	numbers.remove(randa)
	
	randb = numbers[getrandnum(0,len(numbers)-1)]
	j *= randb
	numbers.remove(randb)
	
	randc = numbers[getrandnum(0,len(numbers)-1)]
	j *= randc
	numbers.remove(randc)
	
	randd = numbers[getrandnum(0,len(numbers)-1)]
	j *= randd
	
	if (j>0):
		return True;
	else:
		return False;
		
def exper():
	numtests = 10000
	amtpos = 0
	numbers = [-10,-5,-7,-8,-3,-9,-1,-6,2,3,4,5,6,7]
	#numbers = [-10,-5,-7,-8,3,9,1,6,2,3,4,5,6,7]
	for i in xrange(numtests):
		if (randmult(numbers[:])):
			amtpos += 1
	return ((float(amtpos)/float(numtests))*100)
	
def avgexper():
	j = 0
	runs = 5
	for i in xrange(runs):
		j += exper()
	return float(j)/float(runs)

print str(avgexper())+'%'