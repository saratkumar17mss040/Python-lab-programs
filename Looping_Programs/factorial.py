print("Enter number")
number = int(input())
fac = 1
if number == 0:
  print(1)
else:
  while number >= 1:
    fac = fac*number
    number = number-1
  print(fac)
