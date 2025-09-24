# giải phương trình f(x) = 0, tìm nghiệm xấp xỉ c theo phương pháp chia đôi.
def solver(f, a, b, e=0.000001):
    if f(a) * f(b) > 0:
      raise ValueError("f(a) and f(b) must be lower than 0")
    
    c = (a + b)/2

    fc = f(c)

    if fc < e:
       return c
    
    if f(a) * f(c) < 0:
       return solver(f, a, c, e)
    else:
       return solver(f, c, b, e)
