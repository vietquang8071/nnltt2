def convert(n):
    bin = []
    while n > 0:
        bin.append(n % 2)
        n //= 2
    return "".join(str(i) for i in bin)[::-1]
    
print(convert(11))