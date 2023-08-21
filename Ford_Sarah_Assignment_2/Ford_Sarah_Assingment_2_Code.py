
from pylab import *
import numpy


def simarray():
    simarray = []
    for i in range(500):
        length = numpy.random.choice(arange(2,6),p=[0.25,0.375,0.28125,0.09375])
        simarray.append(length)
    return simarray


def diceroll_stem():
    bins = [1.5,2.5,3.5,4.5,5.5]
    probabilities = [125,187.5,140.625,46.875]
    h = histogram(simarray(),bins)
    print h
    stem(range(2,6),h[0],linefmt='k-',markerfmt='ko')
    stem(arange(2.1,6.1),probabilities,linefmt='b',markerfmt='ko')
    title("500 trials of the dice game")
    xlim(1,6)
    xlabel("Game toss length")
    ylabel("Frequency")
    show()


#diceroll_stem()
print simarray()
