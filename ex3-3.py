try:
    score = input("Enter Score: ")
    s = float(score)
   
    if s < 0.0:
        print ("Bad Score")
        
    elif s < 0.6:
        print ("Grade: F")

    elif s < 0.7:
        print ("Grade: D")

    elif s < 0.8:
        print ("Grade: C")

    elif s < 0.9:
        print ("Grade: B")

    elif s <=1.0:
        print ("Grade: A")

    elif s > 1.0:
        print ("Bad Score")

except:
    print ("Bad Score")


