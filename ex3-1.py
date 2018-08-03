hours = input("Please enter the number of hours: ")
rate = input("Please enter the rate per hour: ")

h = float(hours)
r = float(rate)

if h > 40:
    pay = (40 * r) + ((h-40) * r * 1.5)
else:
    pay = h * r

print ("Pay:",pay)
