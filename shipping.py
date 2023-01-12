weight = 41.5

#Ground Shipping
if weight <= 2:
  print(20 + weight * 1.5)
elif weight <= 6:
  print(20 + weight * 3)
elif weight <= 10:
  print(20 + weight * 4)
elif weight > 10:
  print(20 + weight * 4.75)

premium = 125.00
print(premium)

#Drone shipping
if weight <= 2:
  print(weight * 4.5)
elif weight <= 6:
  print(weight * 9)
elif weight <= 10:
  print(weight * 12)
elif weight > 10:
  print(weight * 14.25)