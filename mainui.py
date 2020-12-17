import tkinter as tk
from tkinter import ttk
import math



def buttonrun1Click():
    
    try:
        arrivalrate =  float(input1_1.get())
        servicerate =  float(input1_2.get())
        p_blocking_required = float(input1_3.get())
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


        print('The number of servers required is: ', c)
        print('With blocking probability: ',p_blocking)
        ans = 'The number of servers required is: '+str(c)+ '\nThe blocking probability is: '+'{:.4f}'.format(p_blocking)



    except Exception as E:
        errorstr1.set('Error: '+str(E))
        outputstr1.set('')
    else:
        outputstr1.set(ans)
        errorstr1.set('')

def buttonrun2Click():
    try: 
        arrivalrate = float(input2_1.get())
        servicerate = float(input2_2.get())
        epsilon_req = float(input2_3.get())
        alpha_req = float(input2_4.get())

        #chceck rho < 1
        #epsilon_req <= 1

        c = 0
        epsilon = 1.1
        alpha = 0
        c_alpha = 0
        c_epsilon = 0


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
        
        ans = 'The number of servers required to satisfy constraint a is: '+str(c_epsilon)+'\nThe number of servers required to satisfy constraint b is: '+str(c_alpha)+\
        '\nThe number of servers required to satisfy both constraints is: '+str(c)+'\nThe average number of servers busy is: '+'{:.4f}'.format(E_busyservers)+\
        '\nThe average number of packets in the system is: '+'{:.4f}'.format(E_packets)

    except Exception as E:
        errorstr2.set('Error: '+str(E))
        outputstr2.set('')
    else:
        outputstr2.set(ans)
        print(ans)
        errorstr2.set('')

def buttonrun3Click():
    try:
        N = int(input3_1.get())
        alpha = float(input3_2.get())
        servicerate = float(input3_3.get())
       

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

        #portionwaiting = avgwaittime/avgtime
        portionwaiting = avgtime/(avgtime+alpha)

      
        ans = 'The percentage of time the server is busy is: '+'{:.2f}%'.format(busy*100)+'\nThe throughput of the server is: '+'{:.4f}'.format(throughput)+\
            '\nThe average time spent for each request is: '+'{:.4f}'.format(avgtime)+'\nThe portion of time each client spends waiting is: '+'{:.4f}'.format(portionwaiting)

    except Exception as E:
        errorstr3.set('Error: '+str(E))
        outputstr3.set('')
    else:
        outputstr3.set(ans)
        print(ans)
        errorstr3.set('')

def buttonrun4Click():
    try:

        arrivalrate = float(input4_1.get())
        servicerate = float(input4_2.get())
        K = int(input4_3.get())

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

        ans = 'The server utilization is: '+'{:.4f}'.format(utilization)+'\nThe average number of packets in the system is: '+'{:.4f}'.format(E_N)
    
    except Exception as E:
        errorstr4.set('Error: '+str(E))
        outputstr4.set('')
    else:
        outputstr4.set(ans)
        print(ans)
        errorstr4.set('')

def buttonrun5Click():
    try:
        arrivalrate = float(input5_1.get())
        servicerate = float(input5_2.get())
        servicerate2 = float(input5_3.get())

        lamda = arrivalrate

        if servicerate < servicerate2:
            mu1 = servicerate
            mu2 = servicerate2
        else:
            mu1 = servicerate2
            mu2 = servicerate

        # c00 = 1
        # c01 = (lamda/mu2)*(1-(lamda+mu1+mu2)/(2*lamda+mu1+mu2))
        # c10 = (1+((lamda+mu2)/mu1))*(lamda/(2*lamda+mu1+mu2))
        # c11 = ((lamda+mu2)/mu1)*c01
        # csum = (lamda/(mu1+mu2))*(c11/(1-(lamda/(mu1+mu2))))

        # p00 = 1/(c00+c01+c10+c11+csum)
        # p01 = c01*p00
        # p10 = c10*p00
        # p11 = c11*p00
        # px1 = csum*p00

        # check = p00+p01+p10+p11+px1

        # c00 = 1
        # #c01 = (((lamda+mu1)/mu2)*(lamda*((1+((lamda+mu2)/mu1))/(2*lamda+mu1+mu2)))-(lamda/mu2))*(mu1/(lamda+mu2))
        # c10 = (lamda*(1+((lamda+mu2)/mu1)))/(2*lamda+mu1+mu2)
        # c01 = (lamda*lamda)/(mu2*(2*lamda+mu1+mu2))
        # c11 = ((lamda+mu1)/mu2)*(lamda*((1+((lamda+mu2)/mu1))/(2*lamda+mu1+mu2)))-(lamda/mu2)
        # csum = ((lamda/(mu1+mu2))/(1-(lamda/(mu1+mu2))))*(((lamda+mu1)/mu2)*(lamda*((1+((lamda+mu2)/mu1))/(2*lamda+mu1+mu2)))-(lamda/mu2))
        
        # p00 = 1/(c00+c01+c10+c11+csum)
        # p01 = c01*p00
        # p10 = c10*p00
        # p11 = c11*p00
        # px1 = csum*p00
        # check = p00+p01+p10+p11+px1

        util_new  = lamda/(mu1+mu2)

        c00 = 1
        c10 = (lamda*(1+((lamda+mu2)/mu1)))/(2*lamda+mu1+mu2)
        c01 = (lamda-mu1*c10)/mu2
        c11 = ((lamda+mu2)/mu1)*c01
        csum = (util_new/(1-util_new))*c11
        
        p00 = 1/(c00+c10+c01+c11+csum)
        p01 = c01*p00
        p10 = c10*p00
        p11 = c11*p00
        px1 = csum*p00
        check = p00+p01+p11+px1
  
        print('probability of idle or p00 is:',p00, p01,p10,p11,px1)
        print('sum of all probability is: ',check)

        E_Ns = 0*p00+1*p01+1*p10+2*p11+2*px1
        util1 = 1-p00-p01
        util2 = 1-p00-p10
        util = (util1+util2)/2
        

        print('average number of servers working (E_Ns) is:',E_Ns)
        print('the server utilization (E_Ns/2) is:',E_Ns/2)

        ans = 'The probability that the system is idle is: '+'{:.4f}'.format(p00)+'\nThe system utilization is: '+'{:.4f}'.format(util_new)



    except Exception as E:
        errorstr5.set('Error: '+str(E))
        outputstr5.set('')
    else:
        outputstr5.set(ans)
        print(ans)
        errorstr5.set('')

count=5

window = tk.Tk()
window.geometry('600x400')
window.title("EE555 Mini-Project")

tabcontrol = ttk.Notebook(window)
tab1 = ttk.Frame(tabcontrol)
tab2 = ttk.Frame(tabcontrol)
tab3 = ttk.Frame(tabcontrol)
tab4 = ttk.Frame(tabcontrol)
tab5 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text = 'Problem 1')
tabcontrol.add(tab2, text = 'Problem 2')
tabcontrol.add(tab3, text = 'Problem 3')
tabcontrol.add(tab4, text = 'Problem 4')    
tabcontrol.add(tab5, text = 'Problem 5')

tabcontrol.pack(expand=1, fill='both')


#problem 1
ttk.Label(tab1, text="Lambda = ").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab1, text="Mu = ").grid(column=0, row=1, padx=10, pady=10)
ttk.Label(tab1, text="P_b = ").grid(column=0, row=2, padx=10, pady=10)
input1_1 = ttk.Entry(tab1,width="35")
input1_1.grid(row=0, column=1)
input1_2 = ttk.Entry(tab1,width="35")
input1_2.grid(row=1, column=1)
input1_3 = ttk.Entry(tab1,width="35")
input1_3.grid(row=2, column=1)
output1_1 = ttk.Label(tab1, text="Output:").grid(column=0, row=3, padx=10, pady=10)
outputstr1 = tk.StringVar()
outputstr1.set("")
output1_2 = ttk.Label(tab1, textvariable=outputstr1).grid(column=1, columnspan=3, row=3, pady=10, sticky='W')
errorstr1 = tk.StringVar()
errorstr1.set("")
error1 = ttk.Label(tab1, textvariable=errorstr1, foreground='red').grid(sticky='W', column=0, columnspan=3, row=4, padx=10, pady=10)
buttonrun1 = ttk.Button(tab1, text="Run", command=buttonrun1Click)
buttonrun1.grid(row=4, column=3)


#problem 2
ttk.Label(tab2, text="Lambda = ").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab2, text="Mu = ").grid(column=0, row=1, padx=10, pady=10)
ttk.Label(tab2, text="Epsilon = ").grid(column=0, row=2, padx=10, pady=10)
ttk.Label(tab2, text="Alpha = ").grid(column=0, row=3, padx=10, pady=10)
input2_1 = ttk.Entry(tab2,width="35")
input2_1.grid(row=0, column=1)
input2_2 = ttk.Entry(tab2,width="35")
input2_2.grid(row=1, column=1)
input2_3 = ttk.Entry(tab2,width="35")
input2_3.grid(row=2, column=1)
input2_4 = ttk.Entry(tab2,width="35")
input2_4.grid(row=3, column=1)
output2_1 = ttk.Label(tab2, text="Output:").grid(column=0, row=4, padx=10, pady=10)
outputstr2 = tk.StringVar()
outputstr2.set("")
output2_2 = ttk.Label(tab2, textvariable=outputstr2).grid(column=1, columnspan=3, row=4, pady=10, sticky='W')
errorstr2 = tk.StringVar()
errorstr2.set("")
error2 = ttk.Label(tab2, textvariable=errorstr2, foreground='red').grid(sticky='W', column=0, columnspan=3, row=5, padx=10, pady=10)
buttonrun2 = ttk.Button(tab2, text="Run", command=buttonrun2Click)
buttonrun2.grid(row=5, column=3)


#problem 3
ttk.Label(tab3, text="N = ").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab3, text="Alpha = ").grid(column=0, row=1, padx=10, pady=10)
ttk.Label(tab3, text="Mu = ").grid(column=0, row=2, padx=10, pady=10)
input3_1 = ttk.Entry(tab3,width="35")
input3_1.grid(row=0, column=1)
input3_2 = ttk.Entry(tab3,width="35")
input3_2.grid(row=1, column=1)
input3_3 = ttk.Entry(tab3,width="35")
input3_3.grid(row=2, column=1)
output3_1 = ttk.Label(tab3, text="Output:").grid(column=0, row=3, padx=10, pady=10)
outputstr3 = tk.StringVar()
outputstr3.set("")
output3_2 = ttk.Label(tab3, textvariable=outputstr3).grid(column=1, columnspan=3, row=3, pady=10, sticky='W')
errorstr3 = tk.StringVar()
errorstr3.set("")
error3 = ttk.Label(tab3, textvariable=errorstr3, foreground='red').grid(sticky='W', column=0, columnspan=3, row=4, padx=10, pady=10)
buttonrun3 = ttk.Button(tab3, text="Run", command=buttonrun3Click)
buttonrun3.grid(row=4, column=3)


#problem 4
ttk.Label(tab4, text="Lambda = ").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab4, text="Mu = ").grid(column=0, row=1, padx=10, pady=10)
ttk.Label(tab4, text="K = ").grid(column=0, row=2, padx=10, pady=10)
input4_1 = ttk.Entry(tab4,width="35")
input4_1.grid(row=0, column=1)
input4_2 = ttk.Entry(tab4,width="35")
input4_2.grid(row=1, column=1)
input4_3 = ttk.Entry(tab4,width="35")
input4_3.grid(row=2, column=1)
output4_1 = ttk.Label(tab4, text="Output:").grid(column=0, row=3, padx=10, pady=10)
outputstr4 = tk.StringVar()
outputstr4.set("")
output4_2 = ttk.Label(tab4, textvariable=outputstr4).grid(column=1, columnspan=3, row=3, pady=10, sticky='W')
errorstr4 = tk.StringVar()
errorstr4.set("")
error4 = ttk.Label(tab4, textvariable=errorstr4, foreground='red').grid(sticky='W', column=0, columnspan=3, row=4, padx=10, pady=10)
buttonrun4 = ttk.Button(tab4, text="Run", command=buttonrun4Click)
buttonrun4.grid(row=4, column=3)


#problem5
ttk.Label(tab5, text="Lambda = ").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(tab5, text="Mu 1 = ").grid(column=0, row=1, padx=10, pady=10)
ttk.Label(tab5, text="Mu 2 = ").grid(column=0, row=2, padx=10, pady=10)
input5_1 = ttk.Entry(tab5,width="35")
input5_1.grid(row=0, column=1)
input5_2 = ttk.Entry(tab5,width="35")
input5_2.grid(row=1, column=1)
input5_3 = ttk.Entry(tab5,width="35")
input5_3.grid(row=2, column=1)
output5_1 = ttk.Label(tab5, text="Output:").grid(column=0, row=3, padx=10, pady=10)
outputstr5 = tk.StringVar()
outputstr5.set("")
output5_2 = ttk.Label(tab5, textvariable=outputstr5).grid(column=1, columnspan=3, row=3, pady=10, sticky='W')
errorstr5 = tk.StringVar()
errorstr5.set("")
error5 = ttk.Label(tab5, textvariable=errorstr5, foreground='red').grid(sticky='W', column=0, columnspan=3, row=4, padx=10, pady=10)
buttonrun5 = ttk.Button(tab5, text="Run", command=buttonrun5Click)
buttonrun5.grid(row=4, column=3)





window.mainloop()



