
from pylab import *
import numpy


###################################### GENERAL FUNCTION

def combination(n,k):
    f = math.factorial
    nfact = f(n)
    kfact = f(k)
    n_k = f(n-k)

    combination = (nfact) / (kfact * n_k)

    return combination

###################################### PART I CODE

def Part1_prob(k):
    prob = float((combination(15,k) * combination(85,7-k))) / float((combination(100,7)))
    return prob
    

def PMF_array():
    temp = 0
    array = []
    for x in range(8):
        temp = Part1_prob(x)
        array.append(temp)
    return array

def PMF_stem_X():
    bins = arange(1.5,8.5)
    probabilities = PMF_array()
    print probabilities
    h = histogram(probabilities,bins)
    print h
    stem(range(0,8),probabilities,linefmt='k-',markerfmt='ko')
    title("PMF of X")
    xlabel("Number Draw")
    ylabel("Probability of Occurrence")
    xlim(-1,8)
    ylim(0,0.5)
    show()

def distribution_X():
    return numpy.random.choice(arange(0,8),p=PMF_array())


def ave_min_expected():
    total = 0
    for x in range(1000):
        total+=distribution_X()
    average = float(total)/float(1000)
    print "Average value is: ",average
    expected = 7 * (float(15)/100)
    print "Expected value is: ",expected
    return average - expected

###################################### PART II CODE

def Part2_Y():
    total = 0
    array = []
    for i in range(1000):
        val = numpy.random.choice([0,1],p=[0.9973,0.0027])
        total+=val
        array.append(val)
    return total


def Part2_prob(k):
    prob = float((combination(1000,k)) * (0.0027**k) * (0.9973 ** (1000-k)))
    return prob


def Part2_approx(k):
    f=math.factorial
    approx = (float(2.7**k) / f(k)) * float(exp((-2.7)))
    return approx

def prob_Y_array():
    temp = 0
    array = []
    for x in range(11):
        temp = Part2_prob(x)
        array.append(temp)
    return array


def approx_Y_array():
    temp = 0
    array = []
    for x in range(11):
        temp = Part2_approx(x)
        array.append(temp)
    return array


def sim_Y_array():
    temp = 0
    array = []
    for i in range(1000):
        temp = Part2_Y()
        array.append(temp)
    return array

def PMF_stem_Y():
    bins = arange(-0.5,11.5)
    h = histogram(sim_Y_array(),bins)
    print h
    array = []
    for i in h[0]:
        array.append(float(i)/1000)
    print array
    stem(arange(0,11),prob_Y_array(),linefmt='b',markerfmt='ko', label = "exact probability")
    stem(arange(0.1,11.1),approx_Y_array(),linefmt='k-',markerfmt='ko', label = "approximate probability")
    stem(arange(0.2,11.2),array,linefmt='red',markerfmt='ko', label = "simulation probability")
    xlim(-1,11)
    title('Stem Plot of Y Probability, Y Approximation, and Y Simulation')
    xlabel('Number of Points')
    ylabel('Probability')
    legend(loc="upper right")
    show()


###################################### MAIN SECTION    


#print combination(1000,1)
#print PMF_array()
#PMF_stem_X()
#print distribution_X()
#print ave_min_expected()
#print Part2_Y()
#print Part2_prob(9)
#print Part2_approx(0)
#print prob_Y_array()
#print approx_Y_array()
#print sim_Y_array()
#print PMF_stem_Y()
