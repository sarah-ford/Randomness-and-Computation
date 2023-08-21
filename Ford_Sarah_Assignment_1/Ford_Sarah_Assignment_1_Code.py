
from pylab import *


def runlengths(p,n):

    tosslength = 0
    tosssequence = []
    booltosses = []

    for i in range(n):
        booltosses.append(rand(n/n)<p)

    tosses = [[int(u) for u in v] for v in booltosses]

    flattosses = []

    for i in range(len(tosses)):
        for j in range(len(tosses[0])):
            flattosses.append(tosses[i][j])

    for x in range(len(flattosses)):
        if x == 0:
            tosslength = 1

        elif (flattosses[x] == 1 and flattosses[x-1] == 0) or (flattosses[x] == 0 and flattosses[x-1] == 1):
            tosssequence.append(tosslength)
            tosslength = 1
        elif flattosses[x] == 1 and flattosses[x-1] == 1:
            tosslength += 1
        elif flattosses[x] == 0 and flattosses[x-1] == 0:
            tosslength += 1
            
    tosssequence.append(tosslength)
    return tosssequence



def maxrunlength(p,n):
    return max(runlengths(p,n))

def numruns(p,n):
    if n == 0:
        return 0
    else:
        return len(runlengths(p,n))




def histmaxruns(p,n,numtrials,cum = False):
    maxlengtharray=[]

    for i in range(numtrials):
        maxlengtharray.append(maxrunlength(p,n))

    
    bins = arange(-0.5,n+1.5,1)
    title(str(numtrials) + " trials of " + str(n) + """
coin tosses with success probability """ + str(p))
    xlim(-1, 30)
    xlabel("Maximum Run Length")
    ylabel("Number of Occurrences")
    hist(maxlengtharray,bins,color="g",cumulative=cum,edgecolor='k')
    show()
    return


def histnumruns(p,n,numtrials,cum = False):

    numrunarray=[]

    for i in range(numtrials):
        numrunarray.append(numruns(p,n))

    bins = arange(-0.5,n+1.5,1)
    title(str(numtrials) + " trials of " + str(n) + """
coin tosses with success probability """ + str(p))
    xlim(-1, n+1)
    xlabel("Number of Runs")
    ylabel("Number of Occurrences")
    hist(numrunarray,bins,color="r",cumulative=cum,edgecolor='k')
    show()
    return



def averunarray(p):
    averunarray = []
    average = 0
    for i in range(0,200):
        array = []
        for j in range(1000):
            array.append(numruns(p,i))
        average = (sum(array)/len(array))
        averunarray.append(average)

    return averunarray


    
def plotnumruns():

    j = 0.3
    while j < 0.6:
        averuns = averunarray(j)
        plot(range(100),averuns, label = "prob="+str(j))
        j += 0.1
    
    axhline(y=0,xmin=0,xmax=n, color='k')
    title("""Average number of runs in 100 tosses of
a coin with heads probability 0.3 - 0.5""")
    xlabel("Number of Tosses")
    ylabel("Average # of Runs")
    legend(loc = "upper left")
    show()
        

def plotconstant():
    constantarray = []
    jarray = []
    j = 0.05
    while j < 1.05:
        jarray.append(j)
        averuns = averunarray(j)
        constant = 200/averuns[199]
        constantarray.append(constant)
        j+=0.05
        
    scatter(constantarray,jarray,s=5)
    xlim((0,max(constantarray)))
    yticks(arange(0,1.0,0.05))
    title("Distribution of constants in 200 tosses of a fair coin with probabilities 0.05 - 1.0")
    show()


n = int(raw_input("Please input the number of tosses: "))
p = float(raw_input("Please input the probability of landing on heads: "))
numtrials = int(raw_input("Please input the number of trials: "))

print runlengths(p,n)
print
print histmaxruns(p,n,numtrials,cum = False)
print histnumruns(p,n,numtrials,cum = False)
print averunarray(p)
print plotnumruns()
print numruns(0.5,0)
print plotconstant()
