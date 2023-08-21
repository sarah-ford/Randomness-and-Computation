
from pylab import *
from numpy.random import choice
import random

def trans(n):

    Array = [[0 for x in range(n+1)] for y in range(n+1)]

    Array[0][1] = 1

    for x in range(1,n):
        Array[x][1] = (1.0/2)
        for j in range(1,n+1):
            if j == x+1:
                Array[x][j] = (1.0/2)

    Array[n][n] = 1


    return array(Array)


def step_matrix(trans,n):

    return linalg.matrix_power(trans,n)


def prob_result(trans,state,step):

    stepm = step_matrix(trans,step)

    return 1 - stepm[0][state]


def nextstate(m,state):
    return choice(range(len(m)),p=m[state])


def run_sim(n):
    count = 0
    tally = 0
    while count < n:
        x = random.randint(0,1)
        tally+=1
        if x == 1:
            count+=1
        else:
            count = 1
    return tally


def avg_sim(n):
    total = 0
    for x in range(10000):
        total+=run_sim(n)
    return float(total)/10000


def revised_trans(n):
    
    Array = [[0 for x in range(n+1)] for y in range(n+1)]

    Array[0][1] = 1

    for x in range(1,n):
        Array[x][1] = (1.0/2)
        for j in range(1,n+1):
            if j == x+1:
                Array[x][j] = (1.0/2)

    Array[n][1] = 1.0/2
    Array[n][n] = 1.0/2

    return array(Array)


def eig_vals():
    m = revised_trans(n)
    u = eig(transpose(m))
    v = [real(u[1])[j][0] for j in range(n+1)]
    return v/sum(v)


def revised_sim(tosses,state):
    count = 0
    n = 0
    for x in range(tosses):
        x = random.randint(0,1)
        if x == 1:
            if n < state:
                n += 1
            else:
                n += 0
        else:
            n = 1

        if n == state:
            count += 1
            
    return float(count) / tosses


n = 7
#print trans(n)
#print
#print step_matrix(trans(n),200)
#print
#print prob_result(trans(6),6,200)
#print
#print prob_result(trans(7),7,200)
#print
#print avg_sim(n)
#print revised_trans(n)
#print
#print step_matrix(revised_trans(n),50)
#print
#print eig_vals()
#print
print revised_sim(200000,6)
print
print revised_sim(200000,7)
