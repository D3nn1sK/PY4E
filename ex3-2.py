try:
    hours = input("Please enter the number of hours: ")
    h = float(hours)
    rate = input("Please enter the rate per hour: ")   
    r = float(rate)

    if h > 40:
        pay = (40 * r) + ((h-40) * r * 1.5)
    else:
        pay = h * r

    print ("Pay:",pay)
except:
    print ("Error, please enter a number")