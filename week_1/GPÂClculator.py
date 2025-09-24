def gpa(subjects):
  total = 0
  credit = 0

  for subject in subjects:
    point = 0
    if subject[1] >= 9.0:
      point = 4.0
    elif subject[1] > 8.5:
      point = 3.7
    elif subject[1] > 8.0:
      point = 3.5
    elif subject[1] > 7.0:
      point = 3.0
    elif subject[1] > 6.5:
      point = 2.5
    elif subject[1] > 5.5:
      point = 2.0
    elif subject[1] > 5.0:
      point = 1.5
    elif subject[1] > 4.0:
      point = 1.0
    else:
      point = 0
    total += subject[0] * point
    credit += subject[0]
  GPA = round((total/credit), 2)

  if GPA >= 3.60:
    return f'{GPA}: Excellent'
  elif GPA >= 3.20:
    return f'{GPA}: Very Good'
  elif GPA >= 2.50:
    return f'{GPA}: Good'
  elif GPA >= 2.00:
    return f'{GPA}: Average'
  else:
    return f'{GPA}: At risk'
  
n = int(input())

arr = []
for _ in range(n):
  credit, point = input().split()
  arr.append((int(credit), float(point)))

gpa(arr)