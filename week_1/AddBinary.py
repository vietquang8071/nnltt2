def add(a, b):
    a = a.strip()
    b = b.strip()
    if len(a) > len(b):
        b = b.zfill(len(a))
    elif len(b) > len(a):
        a = a.zfill(len(b))
    a = a[::-1]
    b = b[::-1]
    res = []
    carry = 0
    for i in range(len(a) - 1):
        ai = int(a[i])
        bi = int(b[i])
        digit = ai + bi + carry
        if digit == 0:
            res.append('0')
            carry = 0
        elif digit == 1:
            res.append('1')
            carry = 0
        elif digit == 2:
            res.append('0')
            carry = 1   
        elif digit == 3:
            res.append('1')
            carry = 1
    if carry == 1:
        res.append('1')
    return ''.join(res[::-1])
