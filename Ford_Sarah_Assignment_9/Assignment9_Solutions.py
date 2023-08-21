#Solutions for Assignment 9.

#We'll give the solutions in the form of a Python file.
#The function do_it() calls the other functions to
#display the answers, along with comments about what the
#answers mean.

#Generate the transition matrix for runs of length n.  This will be
#an (n+1)X(n+1) matrix.  There is a second paramenter to determine whether
#we mean the absorbing or the regular version of the problem.

from pylab import *
from numpy.random import choice

def matrix_gen(n,absorbing=True):
    matrix=[]
    rowzero=[0,1]+[0]*(n-1)
    matrix.append(rowzero)
    for j in range(1,n):
        newrow=[]
        for k in range(n+1):
            if k==1:
                newrow.append(0.5)
            elif k==min(j+1,n):
                newrow.append(0.5)
            else:
                newrow.append(0)
        matrix.append(newrow)
    if absorbing:
        lastrow=[0]*n+[1]
    else:
        lastrow=[0,0.5]+[0]*(n-2)+[0.5]
    matrix.append(lastrow)
    return array(matrix)

#Simulate Markov chain:
#Given transition matrix and current state, return next state.
#Note states are numbered 0,1,...,n-1 instead of 1,..,n to conform
#with Python indexing of arrays.

def nextstate(m,state):
    return choice(range(len(m)),p=m[state])



def do_it():
    print """1. The matrices of the absorbing chain
for n=2,3,4.  These were computed using the function
for Problem 2."""
    for j in range(2,5):
        print matrix_gen(j)
        print
    raw_input("Press return to continue.")
    print """3: To find the probability that the chain
is in the absorbing state after 200 tosses,
compute the 200th power and look at the
upper-right entry.  The answer looked for
here is the complementary probability, so
subtract this from 1.

Probability of no run of length 6 in 200 tosses:"""
    m6=matrix_gen(6)
    n=matrix_power(m6,200)
    print 1-n[0][6]
    print
    print """Probability of no run of length 7 in 200 tosses:"""
    m7=matrix_gen(7)
    n=matrix_power(m7,200)
    print 1-n[0][7]
    print
    print """So 80% of the time we will get a run of length 7
in a string of 200 tosses.  Contrast this with the in-
class experiment, where the fake-coin tossers NEVER produced
a run this long."""
    print
    raw_input("Press return to continue.")
    print """4:  To calculate the expected time to absorption,
we extract the nXn submatrix Q of the transient states, find
the inverse of I-Q, and then form sum of the first row.  Below
we print out the inverse of I-Q and the row sum for the case
where n=6 and n=7."""
    q6=array([m6[i][0:6] for i in range(6)])
    i6=inv(eye(6)-q6)
    print i6
    print
    print sum(i6[0])
    print
    q7=array([m7[i][0:7] for i in range(7)])
    i7=inv(eye(7)-q7)
    print i7
    print
    print sum(i7[0])
    print
    
    
    raw_input("Press return to continue.")
    print """5. Now for ten thousand times we will simulate the chains
for 6 and 7 and note the average time to absorption. (Be
patient; it takes a couple of minutes.)"""
    sum6=0
    sum7=0
    for trial in range(10000):
        count6=0
        count7=0
        state6=0
        state7=0
        while state6 != 6:
            state6=nextstate(m6,state6)
            count6+=1
        while state7!= 7:
            state7=nextstate(m7,state7)
            count7 += 1
        sum6+=count6
        sum7+=count7
    print
    print "Average time for run of length 6:\t"+str(sum6/10000.0)
    print
    print "Average time for run of length 7:\t"+str(sum7/10000.0)
    print
    print "The agreement is very good!!"
    raw_input("Press return to continue.")
    print """6. Here are the matrices for the regular chain version
of the problem, for n=6,7."""
    m6=matrix_gen(6,False)
    m7=matrix_gen(7,False)
    print m6
    print
    print m7
    print
    raw_input("Press return to continue.")
    print """7. Instead of using fancy algebra to find the stationary
distribution, let's just compute a high power (here the 200th) and
see if the columns stabilize.  They do (and at nice fractions). Here
are the 200th powers for 6 and 7.  Any row of these gives the stationary
distribution."""
    print matrix_power(m6,200)
    print
    print matrix_power(m7,200)
    print
    print """The run of length 7 occurs 1/64 of the time, and the run
of length 6 1/32 of the time."""
    raw_input("Press return to continue.")
    print """8. Finally, let's do the simulation.  We will run each
chain for 100,000 steps and count the number of times we are in state
6 (for the first chain) and in state 7 (for the second). We'll print
out the proportion of times we are in these states, and compare to the
theoretical values 0.03125 amd 0.015625."""
    count6=0
    count7=0
    state6=0
    state7=0
    for j in range(100000):
        state6=nextstate(m6,state6)
        if state6==6:
            count6+=1
        state7=nextstate(m7,state7)
        if state7==7:
            count7+=1
    print count6/100000.,count7/100000.
    
    
    

        
print do_it()






    
