import numpy as np 
import math


arrivalrate = float(input('arrival rate is:'))
servicerate = float(input('service rate is:'))
K = int(input('maximum capacity of the system is:'))


sum1 = 0

for i in range(K+1):
    sum1 = sum1 + (arrivalrate/(K*servicerate))**i*(math.factorial(K)/math.factorial(K-i))

p_0 = 1/sum1
print('p0 = ',p_0)
p = []

for i in range(K+1):
    
    x = (arrivalrate/(K*servicerate))**i*(math.factorial(K)/math.factorial(K-i))
    p.append(x*p_0)

print(p)
print(sum(p))

utilization = 1-p[0]
E_N = 0

for i in range(K+1):
    E_N = E_N + i*p[i]
print('util = ', utilization)
print('avg packets in the system = ', E_N)