def sumNN(num):
  res = 0
  temp = str(num)
  for i in range(4):
    res += int(temp)
    temp += str(num)
    print(temp)
  return res

n = int(input())
print(sumNN(n))