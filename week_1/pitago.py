import math
def pitago(limit):
  res = []
  m = 2

  while 1:
    if m * m > limit:
      return res
    for n in range(1, m):
      if (m - n) % 2 == 1 and math.gcd(m, n) == 1:
        a = m**2 - n**2
        b = 2 * n * m
        c = m**2 + n**2
        if c  > limit:
          break
        res.append((a, b, c))
        k = 2
        while k * c <= limit:
          res.append((k * a, k * b, k * c))
          k+=1
    m+=1
  return res

res = pitago(25)
print(res)

      