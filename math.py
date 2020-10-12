import modul arange untuk float
from numpy import arange
import pandas as pd
from math import sqrt

def narcissistic(n):
    print("[NARCISSISTIC CHECKER PROGRAM]", "\n")
    cacah = len(str(n))
    listnarsis = []
    for i in str(n):
        narsis = int(i) ** cacah
        listnarsis.append(int(narsis))
        narsistik = sum(listnarsis)
        if narsistik == int(n):
            print(n, "is a narcissistic number.")
        else:
            print(n, "is not a narcissistic number.")

def boilaegg(n, e, m):
    print("[BOIL A EGG is a program to count how long to boil a eggs with a user-based performance.]", "\n")
    if int(n) == 0:
        print("\n" + "You haven't input any egg yet." + "\n")
    else:
        minute = -(-int(n) // int(e)) * int(m)
        print(n, "eggs for", minute, "minutes." + "\n")

def piprox(n):
    print("[PIPROX is a program to approx a phi number using phi series based on user input orde]", "\n")
    if (int(n) == 0):
        print("Your n orde is", n,)
    else:
        # initial state p
        p = 0
        for i in range(1, n+1):
            # operate approx
            p += (4 / ((2 * i) * ((2 * i)+1) * ((2 * i)+2))) * ((-1) ** int(i+1))
            # sum approx to 3
            phi = 3 + float(p)
            print("Your approximated phi = ", phi, "\n")
piKira2(10)

def probdens(x1, x2, d, r, b):
    e = 2.71828
    p = 3.141594
    for x in arange(x1, x2+d, d):
        # operate exp
        exp = - (1 / 2) * ((float(x) - float(r)) / float(b)) ** 2
        # operate denom
        denom = float(b) * (sqrt(2 * float(p)))
        # operate y
        y = 1 / float(denom) * float(e) ** float(exp)
        ## yield y
        print("%.2f  " % (x), y)
## k2 = probdens(0, sqrt(0.2))
## k3 = probdens(0, sqrt(1))
## k4 = probdens(0, sqrt(5))
## k5 = probdens(0.2, sqrt(0.5))
## table = pd.DataFrame({'x':k1, 'μ=0 & σ2=0.2':k2, 'μ=0 & σ2=1':k3, 'μ=0 & σ2=5':k4, 'μ=0.2 & σ2=0.5':k5})
## print(table)
