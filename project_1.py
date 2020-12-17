import numpy as np
import math



arrivalrate = float(input("arrival rate is:"))
servicerate = float(input('service rate is:'))
p_blocking_required = float(input('the blocking probability is:'))
p_blocking = 1
#error check
#rho must < 1
#input must be only numbers
#end error check
#division by 0

rho = arrivalrate/servicerate


c = 0

while p_blocking>p_blocking_required:
    c = c+1
    summ = 0
    for i in range(c+1):
        #print(i)
        summ = summ+rho**i*(1/math.factorial(i))
    p_0 = 1/summ
    print('p_0 =', p_0)
    p_blocking = rho**c*(1/math.factorial(c))*p_0
    print('p_blocking =', p_blocking)   


print('the # of servers required is: ', c)
print('with blocking probability: ',p_blocking)









