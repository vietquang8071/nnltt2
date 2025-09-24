def sqrt_newton(c):
  EPSILON = 1e-15
  if c == 0:
    return 0
  
  t = c
  if t == c/t:
    return t
  
  while abs(t - c/t) < (EPSILON * t):
    t = (t + c / t) / 2
  return t