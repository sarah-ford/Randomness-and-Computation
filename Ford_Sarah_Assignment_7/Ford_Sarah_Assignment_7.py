import random
import math
import numpy


def dist_value():
    r = random.random()

    x = (21**r) - 1

    return x


def ave_value(N):
    total = 0
    for n in range(N):
        total+=dist_value()

    ave = float(total) / N
    return ave



def check(N):
    ex_value = 5.56917
    for n in range(N):
        if abs(ave_value(29106900)-ex_value) > (10**(-3)):
            return False
        else:
            return True



#print dist_value()
N = 10000
#print ave_value(29000000)
print check(100)

