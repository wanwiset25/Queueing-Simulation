import numpy as np 
import math



alpha = float(input('average client request preparation time is:'))
servicerate = float(input('service rate is:'))
N = int(input('maximum number of clients is:'))

sum1 = 0

for i in range(N+1):
    sum1 = sum1 + (math.factorial(N)/math.factorial(N-i))*(1/(alpha*servicerate)**i)

P = [0]
P[0] = 1/sum1

for i in range(N):
    j=i+1
    temp = (P[0]/(alpha*servicerate)**j)*(math.factorial(N)/math.factorial(N-j))
    P.append(temp)

busy = 1-P[0]
throughput = servicerate*busy

avgpacket = 0
for i in range(N+1):
    avgpacket = avgpacket + i*P[i]

avgtime = (avgpacket*alpha)/(N-avgpacket)

avgpacketinservice = busy

avgpacketwaiting = avgpacket - avgpacketinservice

lamda = N/(alpha+avgtime)

avgwaittime = avgpacketwaiting/lamda

portionwaiting = avgwaittime/avgtime

print('The portion of time the server is busy is: ', busy )
print('The throughput of the server is: {:.2f}'.format(throughput))
print('average time spent for a packet is: {:.2f}' .format(avgtime))
print('The portion of time a packet spent waiting is: {:.2f}' .format(portionwaiting))
print('pdf is', P)