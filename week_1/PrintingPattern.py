def leftHalfPyramid(n):
    for i in range(1, n + 1):
      print("*" * i + ' ' * (n - i))

def rightHalfPyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


def fullPyramid(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i + " " * (n - i))


def invertedFullPyramid(n):
    for i in range(n , 0, - 1):
        print(" " * (n - i) + "*" * (i * 2 - 1) + " " * (n - i))

def hollowPyramid(n):
  for i in range(1, n+1):
      print(" " * (n - i), end="")

      if i == 1:
        print("*")
      elif i == n:
        print("*" * (2 * i - 1))
      else:
         print("*" + " " * (2 * i - 3) + "*")


leftHalfPyramid(5)
rightHalfPyramid(5)
hollowPyramid(5)