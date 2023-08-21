from pylab import *

#return a list of the sequence of run lengths in
#n tosses of a coin with heads probability p.
#The verbose variable is just an option put in to
#check if this is correct.
def runlengths(p,n,verbose=False):
	results=[]
	for j in range(n):
		results.append(int(random()<p))
	if verbose:
		print results
	runlengths=[]
	current_symbol=results[0]
	current_length=1
	for j in range(1,n):
		if results[j]!=current_symbol:
			runlengths.append(current_length)
			current_length=1
			current_symbol=1-current_symbol
		else:
			current_length+=1
	#and one more entry for the final run
	runlengths.append(current_length)
	return runlengths

def maxrunlength(p,n):
    return max(runlengths(p,n))

def numruns(p,n):
    return len(runlengths(p,n))

def histmaxruns(p,n,numtrials,cum=False):
    result=[maxrunlength(p,n) for j in range(numtrials)]
    minbar=min(result)
    maxbar=max(result)
    bins=arange(minbar-1.5,maxbar+2.5,1)
    hist(result,bins,cumulative=cum)
    #chart title and legend, here and in remaining problems?
    xlabel("Run length")
    ylabel("Number of occurrences")
    title("""Maximum run length in """+str(n)+""" tosses of a coin
          with heads probability """+str(p)+""" based on """+str(numtrials)+""" trials""")
    show()

def histnumruns(p,n,numtrials,cum=False):
    result=[numruns(p,n) for j in range(numtrials)]
    minbar=min(result)
    maxbar=max(result)
    bins=arange(minbar-1.5,maxbar+2.5,1)
    hist(result,bins,cumulative=cum)
    xlabel("Number of runs")
    ylabel("Number of occurrences")
    title("""Number of runs in """+str(n)+""" tosses of a coin
          with heads probability """+str(p)+""" based on """+str(numtrials)+""" trials""")
    show()

def plotnumruns():
    base = range(0,405,10)
    for p in [0.3,0.4,0.5]:
        results=[0]
        for numtosses in base[1:]:
            results.append(sum([numruns(p,numtosses) for j in range(1000)])/1000)
        plot(base,results,label="heads probability="+str(p))
        xlabel('Number of tosses')
        ylabel('Number of runs/number of tosses')
        title("""Number of runs versus number of tosses of a coin
          with different heads probabilities based on 1000 trials""")
        legend(loc='upper left')
    show()

def plotavgnumruns():
    base=arange(0,1.01,0.01)
    results=[]
    for p in base:
        results.append(sum([numruns(p,200)/200.0 for j in range(1000)])/1000)
    plot(base,results)
    xlabel('heads probability')
    ylabel('number of runs')
    title("""Estimate of ratio of number of runs to number of tosses
at different heads probabilites, based on 1000 trials""")
    show()
    
        

plotnumruns()    
    
