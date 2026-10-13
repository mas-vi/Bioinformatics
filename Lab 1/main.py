import matplotlib.pyplot as plt

def compute_freq(sequence):
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

while True:
    S=""
    print("Input sequence:")
    S=input()
    print(compute_freq(S))