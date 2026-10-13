# The actual T_m is influenced by the conentration of Mg_2+ and K_+, and 
# T_m=81.5+16.6*(log_10([Nort]))+0.41*(%GC)-600/length

import matplotlib.pyplot as plt
import math
import random

prev=1
def temp(C,G,A,T):
    return 81.5 +16.6 * math.log10(0.05)+0.41*((C+G) /(C+G+A+T)*100)-600/(C+T+A+G)
x=[]
y=[]
for i in range(1,10):
    C=random.randint(prev,15)
    G=random.randint(prev-1,10)
    A=random.randint(1,10)
    T=random.randint(1,10)
    x.append((C+G)/2)
    y.append(temp(C,G,A,T)) 
plt.plot(x,y)
plt.show()

 