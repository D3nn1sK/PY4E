def computepay(h,r):
    if h > 40:
        p = (40 * r) + ((h-40) * r * 1.5)
    else:
        p = h * r 
    return p

try:
    hours = input("Please enter the number of hours: ")
    h = float(hours)
    rate = input("Please enter the rate per hour: ")   
    r = float(rate)

    pay = computepay(h,r)

except:
    print ("Error, please enter a number")

print ("Pay:",pay)
