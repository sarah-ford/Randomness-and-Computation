import math
import random



def In_Short_Cone(x,y,z):
    equation_1 = ((x)**2)+((y)**2)
    equation_2 = 0
    equation_3 = 1 - math.sqrt((x)**2+(y)**2)
    return (equation_1 <= 1) and (equation_2 <= z) and (z <= equation_3)


def In_Skinny_Cone(x,y,z):
    equation_1 = (z - (0.5))**2 + (y)**2
    equation_2 = -2
    equation_3 = (2 - (8 * math.sqrt(((y)**2) + ((z-(0.5))**2))))
    return (equation_1 <= (0.25)) and (equation_2 <= x) and (x <= equation_3)



def intersect_volume():
    both_count = 0
    for x in range(2000000):
        x = random.uniform(-2,2)
        y = random.uniform(-1,1)
        z = random.uniform(0,1)
        if (In_Short_Cone(x,y,z) == True) and (In_Skinny_Cone(x,y,z) == True):
            both_count+=1
    return both_count


x = random.uniform(-2,2)
y = random.uniform(-1,1)
z = random.uniform(0,1)


#print x, y, z
#print In_Short_Cone(x,y,z)
#print In_Skinny_Cone(x,y,z)
print intersect_volume()

print (float(intersect_volume())/2000000)*8
