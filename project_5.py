import numpy as np 
import math

arrivalrate = float(input('arrival rate is:'))
servicerate = float(input('service rate of server 1 is:'))
servicerate2 = float(input('service rate of server 2 is:'))

lamda = arrivalrate

if servicerate < servicerate2:
    mu1 = servicerate
    mu2 = servicerate2
else:
    mu1 = servicerate2
    mu2 = servicerate

c00 = 1
c01 = (lamda/mu2)*(1-(lamda+mu1+mu2)/(2*lamda+mu1+mu2))
c10 = (1+((lamda+mu2)/mu1))*(lamda/(2*lamda+mu1+mu2))
c11 = ((lamda+mu2)/mu1)*c01
csum = (lamda/(mu1+mu2))*(c11/(1-(lamda/(mu1+mu2))))

p00 = 1/(c00+c01+c10+c11+csum)
p01 = c01*p00
p10 = c10*p00
p11 = c11*p00
px1 = csum*p00

check = p00+p01+p10+p11+px1

print('probability of idle or p00 is:',p00, p01,p10,p11,px1)
print('sum of all probability is: ',check)

E_Ns = 0*p00+1*p01+1*p10+2*p11+2*px1

print('average number of servers working (E_Ns) is:',E_Ns)
print('the server utilization (E_Ns/2) is:',E_Ns/2)