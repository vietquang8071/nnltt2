def birthdayParadox(n):
  days = 365
  no_match = 1.0
  for i in range(n):
    no_match *= (days - i) / days
  result = 1 - no_match
  return f'{round(result * 100, 10)} %'
