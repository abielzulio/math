def narcissistic(n):
  cacah = len(str(n))
  listnarsis = []
  for i in str(n):
    narsis = int(i) ** cacah
    listnarsis.append(int(narsis))
  narsistik = sum(listnarsis)

  if narsistik == int(n):
    print(n, "termasuk bilangan narcissistic")
  else:
    print(n, "tidak termasuk bilangan narcissistic")
