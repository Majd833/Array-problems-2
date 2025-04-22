a = [1, 5, 3, 67, 3, 5, 64, 23, 8, 2, 2]
smallest = a[0]
largest = a[1]

for i in range(0, len(a)):
  if a[i] > largest:
    largest = a[i]
  elif a[i] == largest:
    largest = a[i]
  else:
    if smallest > a[i]:
      smallest = a[i]
    else:
      pass

sum = largest - smallest
print(sum)