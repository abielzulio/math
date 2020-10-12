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

def boilaegg(n):
    print("[BOIL A EGG is a program to count how long to boil a eggs with 8 eggs per 5 minutes performance.]", "\n")
    if int(n) == 0:
        print("\n" + "You haven't input any egg yet." + "\n")
    else:
        minute = -(-int(n) // 8) * 5
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
