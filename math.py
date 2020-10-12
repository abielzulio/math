import numpy as np
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

##################################

def boilaegg(n, e, m):
    print("[BOIL A EGG is a program to count how long to boil a eggs with a customized pan capacity and performance]", "\n")
    if int(n) == 0:
        print("\n" + "You haven't input any egg yet." + "\n")
    else:
        minute = -(-int(n) // int(e)) * int(m)
        print(n, "eggs for", minute, "minutes." + "\n")

##################################

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

##################################

## -> for table
def probdens(x1, x2, d, r, b):
    print("[PROBDENS is a program to calculate probability density]", "\n")
    e = 2.71828
    p = 3.141594
    for x in np.arange(x1, x2+d, d):
        # calculate exp
        exp = - (1 / 2) * ((float(x) - float(r)) / float(b)) ** 2
        # calculate denom
        denom = float(b) * (sqrt(2 * float(p)))
        # calculate y
        y = 1 / float(denom) * float(e) ** float(exp)
        ## yield y
        print("%.2f  " % (x), y)
## k2 = probdens(0, sqrt(0.2))
## k3 = probdens(0, sqrt(1))
## k4 = probdens(0, sqrt(5))
## k5 = probdens(0.2, sqrt(0.5))
## table = pd.DataFrame({'x':k1, 'μ=0 & σ2=0.2':k2, 'μ=0 & σ2=1':k3, 'μ=0 & σ2=5':k4, 'μ=0.2 & σ2=0.5':k5})
## print(table)

##################################

def matrix(n):
    print("[MATRIX is a program to create a matrix automatically based on n input]", "\n")
    r = c = sqrt(n)
    if r*r != n:
        print("It's not matrix-able")
    else:
        x =  np.arange(1, n+1).reshape(int(r), int(c))
        print("Here's your %dX%d matrix: \n" % (sqrt(n), sqrt(n)))
        print(x)

##################################

def stats(n):
    print("[STAT is a program to calculate mean, varian, standar deviation while user input customized n data]", "\n")
    print("Your desired n data = ", n, "\n")
    x = []
    while len(x) < int(n):
        xi = input("Input your X%d = " % (int(len(x)) + 1))
        x.append(int(xi))
        mean = sum(x) / len(x)
        sig = 0
        for b in x:
            sigma = (float(b) - float(mean))**2
            sig += float(sigma)
            var = 1 / (float(n)-1) * float(sig)
        print("\n\n", "Your current data is", len(x), "\n\n", x, "\n\n", "Mean = ", mean, "\n", "Squared mean = ", float(mean)**2, "\n", "Varians = ", var, "\n", "standar deviation = ", var**0.5, "\n\n")

stats(5)

##################################

def fibonacci(n):
    print("[FIBONACCI is a program to show fibonacci sequence based n orde]", "\n")
    if n <= 1:
        fib = n
    else:
        fib = fibonacci(n-1) + fibonacci(n-2)
    return fib

n = int(input("Input your fibonacci orde = "))
print("\n")
print("Your fibonacci sequence:")
[fibonacci(i) for i in range(1, n+1)]

##################################

def logistic(x, k, n):
  print("[LOGISTIC is a program to compute logistic equation]", "\n")
  if x <= 0 or x >= 1:
      print("Your x value is not between 0 - 1.0", "\n")
  else:
      for i in range(1, n+1):
          x = k * x * (1 - x)
          print("%d  " % (i), x)

logistic()
