import math
import numpy
from pylab import *

def phi(x):
    return 0.5 + 0.5*math.erf(x/math.sqrt(2))



phi_b = phi((201-float(500)/3)/(math.sqrt(float(50*(29/9)))))

phi_a = phi((149-float(500)/3)/(math.sqrt(float(50*(29/9)))))



def PMF():
    values = [1,2,4,5,6]
    dist = [1.0/6,1.0/3,1.0/6,1.0/6,1.0/6]
    stem(values,dist,linefmt='k-',markerfmt='ko')
    xlabel("Value on Die")
    ylabel("Probability of Occurrence")
    title("PMF of Damaged Die")
    show()


def die_roll():
    
    val = numpy.random.choice([1,2,4,5,6],p=[1.0/6,1.0/3,1.0/6,1.0/6,1.0/6])
    return val


def S_50():
    total = 0
    for x in range(50):
        total+=die_roll()
    return total


def prob_part_g():
    count = 0
    for x in range(1000):
        if S_50() > 149 and S_50() < 201:
            count+=1
    return float(count) / 1000

def roll_hist():
    array = []
    for x in range(1000):
        new_S = (S_50() - (float(500)/3)) / (math.sqrt(float(50)*(29/9)))
        array.append(new_S)
    bins = arange(-500,501,0.5)
    hist(array,bins,color="g")
    xlim(-5,5)
    title("Sum of 50 Rolls Distribution")

    x = arange(-4,4.01,0.2)
    plot(x, exp(-x**2/2)/math.sqrt(2*3.141562))

    show()
    


#print phi_b - phi_a
#print die_roll()
#print S_50()
#print prob_part_g()
roll_hist()
#PMF()
