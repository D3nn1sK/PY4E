#Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
#Once "done" is entered, print out the total, count, and average of the numbers. 
#If the user enters anything other than a number, 
#detect their mistake using try and except and print an error message and skip to the next number.

total = 0
count = 0
average = 0

while True:
    n = input("Enter a number: ")
    if n == "done":
        break
    
    try:
        number = int(n)
    except:
        print ("bad data")
        continue    
   
    total = total + number
    count = count + 1

average = total/count
#print ("Total: ", total)
#print ("Count: ", count)
#print ("Average: ", average)
print (total, count, average)
