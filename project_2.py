import numpy as np 
import math


arrivalrate = float(input('arrival rate is:'))
servicerate = float(input('service rate is:'))
epsilon_req = float(input('probability that a packet must wait will not exceed(epsilon): '))
alpha_req = float(input('average waiting time IF a packet must wait will not exceed(alpha): '))

#chceck rho < 1
#epsilon_req <= 1

c = 0
epsilon = 1.1
alpha = 0




while epsilon>epsilon_req or alpha>alpha_req:
    c = c+1
    rho = arrivalrate/(c*servicerate)    
    if rho < 1:
        sum1 = 0
        for i in range(c):
            sum1 = sum1 + (arrivalrate/servicerate)**i*(1/math.factorial(i))
        sum1 = sum1 + (arrivalrate/servicerate)**c*(1/math.factorial(c))*(1/(1-rho))
        p_0 = 1/sum1
        p_c = (arrivalrate/servicerate)**c*(1/math.factorial(c))*p_0
        epsilon = p_c/(1-rho)
        E_Nw = p_c*rho*(1/(1-rho)**2)
        E_W = E_Nw/arrivalrate
        alpha = E_W/epsilon
        print('for c = ',c,' epsilon = ', epsilon,' alpha = ',alpha)
        if epsilon>epsilon_req:
            c_epsilon = c
        if alpha>alpha_req:
            c_alpha = c
E_busyservers = arrivalrate/servicerate
E_packets = E_busyservers + E_Nw
c_epsilon += 1
c_alpha += 1
print('The number of servers required is: ', c)
print('average number of servers busy is: {:.4f}'.format(E_busyservers))
print('average number of packets in the system is: {:.4f}' .format(E_packets))
print('The number of servers required for epsilon is', c_epsilon)
print('The number of servers required for alpha is', c_alpha)