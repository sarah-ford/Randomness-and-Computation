
from pylab import*
import numpy.random as npr

def birthsperday_2000():
    f = open('usbirths2000-2003.csv','r')

    s = f.readline()

    birtharray = []

    for i in range(366):
        s=f.readline()
        if s =='':
            break
        fields = s[:-1].split(',')
        birtharray.append(fields[4])

    return birtharray


def total_births_2000():
    f=open('usbirths2000-2003.csv','r')
    s=f.readline()
    totalbirths=0
    for i in range(366):
        s=f.readline()
        if s=='':
            break
        fields=s[:-1].split(',')
        totalbirths+=int(fields[4])
    return totalbirths

def total_births_all():
    f=open('usbirths2000-2003.csv','r')
    s=f.readline()
    totalbirths=0
    while (True):
        s=f.readline()
        if s=='':
            break
        fields=s[:-1].split(',')
        totalbirths+=int(fields[4])
    return totalbirths
    

def birthsperday_2000_2001():
    count = 0
    birtharray = birthsperday_2000()
    allarray1 = []
    allarray2 = []
    allarray3 = []
    
    f=open('usbirths2000-2003.csv','r')
    s=f.readline()
    while (True):
        s=f.readline()
        if s =='':
            break
        fields=s[:-1].split(',')

        if (count - 366 >= 0) and (count - 366) < 365:

            if count - 366 <= 58:
                num = int(birtharray[count - 366]) + int(fields[4])

            else:
                num = int(birtharray[count - 365]) + int(fields[4])

            allarray1.append(num)
            
        count+=1
    return allarray1


def birthsperday_2000_2002():
    count = 0
    allarray1 = birthsperday_2000_2001()
    allarray2 = []
    f=open('usbirths2000-2003.csv','r')
    s=f.readline()
    while (True):
        s=f.readline()
        if s =='':
            break
        fields=s[:-1].split(',')
        
        if (count - 731) >= 0 and (count - 731) < 365:

            num = int(allarray1[count - 731]) + int(fields[4])

            allarray2.append(num)

        count+=1
    return allarray2


def birthsperday_2000_2003():
    count = 0
    allarray2 = birthsperday_2000_2002()
    allarray3 = []
    f=open('usbirths2000-2003.csv','r')
    s=f.readline()
    while (True):
        s=f.readline()
        if s == '':
            break
        fields=s[:-1].split(',')

        if (count - 1096) >= 0 and (count - 1096) < 365:

            num = int(allarray2[count - 1096]) + int(fields[4])

            allarray3.append(num)

        count+=1
    return allarray3


def final_array():
       array = birthsperday_2000()
       x = array[59]
       finalarray = birthsperday_2000_2003()
       finalarray.insert(59,int(x))
       return finalarray
        


def birthhist_stem_2000():
    bins=arange(-0.5,367.5,1)
    temparray = (birthsperday_2000())
    birtharray = []
    for i in range(366):
        proportion = (float(temparray[i]) / total_births_2000())
        birtharray.append(proportion)
    stem(range(366),birtharray,linefmt='ko',markerfmt='ko')
    title("Birth Distribution in the Year 2000")
    xlim(-1,367)
    xlabel("Day of the Year (1 - 366)")
    ylabel("Proportion of All Births")
    show()


def birthhist_stem_final():
    bins=arange(-0.5,367.5,1)
    temparray=(final_array())
    birtharray = []
    for i in range(366):
        proportion = (float(temparray[i]) / total_births_all())
        birtharray.append(proportion)
    stem(range(366),birtharray,linefmt='ko',markerfmt='ko')
    title("Birth Distribution From 2000 - 2003")
    xlim(-1,367)
    xlabel("Day of the Year (1 - 366)")
    ylabel("Proportion of All Births")
    show()
          

def birthday_generation(k):
    birtharray = []
    temparray=(final_array())
    for i in range(366):
        proportion = (float(temparray[i]) / total_births_all())
        birtharray.append(proportion)
    gen = npr.choice(arange(1,367),k,p=birtharray)
    #print gen
    for j in range(len(gen)):
        for k in range(j+1,len(gen)):
            if gen[j] == gen[k]:
                return True
    return False


def prob_coincidence():
    array = []
    for k in range(66):
        true_count = 0
        for i in range(1000):
            if birthday_generation(k) == True:
                true_count+=1
        true_proportion = float(true_count)/1000
        array.append(true_proportion)
    return array


def birthday():
    comp_prob=[1]
    for j in range(65):
        comp_prob.append(comp_prob[j]*(365.0-j-1)/365)
    x=range(1,67)
    axhline(y=0.5,color='black')
    axhline(y=0.9,color='black')
    axhline(y=0.99,color='black')
    plot(x,1-array(comp_prob), label = 'theoretical')
    plot(x,prob_coincidence(), label = 'real distribution')
    #text(23,0.45,'(22.8,0.5)')
    ylist = concatenate((arange(0,0.95,0.1),array([0.95,1])))
    yticks(ylist)
    xlabel('Number of People')
    ylabel('Probability of Coincidental Birthday')
    legend(loc='lower right')
    show()

#birthsscatter()
#birthhist_stem_2000()
#birthhist_stem_final()

    
#array = birthsperday_2000()
#x = array[59]
#finalarray = birthsperday_2000_2003()
#finalarray.insert(59,int(x))
#print final_array()

#print birthday_generation(20)
#print prob_coincidence()

birthday()
