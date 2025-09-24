def parse(n):
  primes = []

  for i in range(2, int(n ** 2)):
    while(n % i == 0):
      primes.append(i)
      n //=i
  print(*primes, sep=" x ")

parse(598000)