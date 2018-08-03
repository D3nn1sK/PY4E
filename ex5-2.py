#Exercise 2: Write another program that prompts for a list of numbers as above and at 
#the end prints out both the maximum and minimum of the numbers instead of the average.

smallest = None
largest = None

while True:
    n = input("Enter a number: ")
    if n == "done":
        break
   
    try:
        number = int(n)
    except:
        print ("bad data")
        continue    
        
    if smallest is None or smallest > number:
        smallest = number
    if largest is None or largest < number:
        largest = number

    

#print ("Maximum: ", largest)
#print ("Minimum: ", smallest)
print (largest, smallest)