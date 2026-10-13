# The melting temp is the temp Tm at which half of a particular DNA duplex will dissociate
# and become a single strand of DNA
# Primer length and sequence are of critical importance when designing the parameters
# of a sucessfull amplification
# The melting temperature of a nucleic Acid duplex increases both with its length
# and with increasing CG content
# A simple formula for calculation of T_m is
# T_m=4(G+C)+2(A+T)
# Design a software application that computes the T_m from a given sequence S
import matplotlib.pyplot as plt

def compute_t_m(sequence):
    C=0
    G=0
    T=0
    A=0
    for i in range(len(sequence)):
        match sequence[i]:
            case "C":
                C +=1
            case "G":
                G +=1
            case "A":
                A +=1
            case "T":
                T +=1
                
    x=['C','G','A','T']
    y=[C,G,A,T]

    plt.xlabel("Grupare")
    plt.ylabel("Frecventa")
    plt.bar(x,y)
    plt.show()
    return 4*(C+G)+2*(A+T)



S="TAACGCTA"


while True:
    S=""
    print("Input sequence:")
    S=input()
    print(compute_t_m(S))
   
    
