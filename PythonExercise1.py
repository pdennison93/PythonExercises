
'''
Question 1: 
 
 Adapt the “HelloWorld” code below to produce a program that defines a variable capable of holding an integer of your choice. The program should add 3 to that number, multiply the result by 2, subtract 4, subtract twice the original number, add 3, then print the result and a new line.
'''
 
def printHelloWorld():
  x = 9  # Replace with any integer of your choice
  print("The original number is " + str(x))
  newVar = x + 3
  newVar *= 2
  newVar -= 4
  newVar -= 2 * x
  newVar += 3
  print("The result is " + str(newVar))


'''
Question 2: 
 
 Complete the function below so that it prints every integer from x to x + 10.  Do not use loops. 
 
 Call this function from the main to test your program.
'''

def printXTenTimes():
  print(str(3))
  print(str(3+1))
  print(str(3+2))
  print(str(3+3))
  print(str(3+4))
  print(str(3+5))
  print(str(3+6))
  print(str(3+7))
  print(str(3+8))
  print(str(3+9))
  print(str(3+10))

'''
Question 3: 
 
 Complete the function below so that it converts the height of a person from centimetres to feet and inches. Use integer division (rounding down is acceptable, which is the default for integer division). 
 
 Hint: 254 cm is exactly 100 inches and 12 inches is exactly 1 foot. 
 
 Call this function from the main to test your program.  For example you could test your program with the follow five values, where "?" replaced with the true value.

 101 cm is 3 feet 3 inches to the nearest inch.
 3 cm is 0 feet 1 inches to the nearest inch.
 15 cm is ? feet ? inches to the nearest inch.
 192 cm is ? feet ? inches to the nearest inch.
 124 cm is ? feet ? inches to the nearest inch.
'''


def convertMetricToImperialHeights():
  x = 192
  ft = int(x/30.54)
  cm = int((x-ft*30.54)/2.54)
  print(str(101) + " is 3 feet 3 inches to the nearest inch.")
  print(str(x) + " cm is " + str(int(ft)) + " feet " + str(int(cm)) + " inches to the nearest inch.")

'''
Question 4: 
 
 Complete the function below so that it uses three variables (current, previous, next) to calculate and print out the first ten numbers of the Fibonacci sequence, each on a new line: i.e. the first four lines should be as follows:

 0 
 1 
 1 
 2
 
'''

def fibonacci():
  previous = 0
  current = 1
  print(str(previous))
  print(str(current))
  for i in range(0,8):
    next = previous + current
    previous = current
    current = next
    print(str(current))

'''
 Question 5: 
 
 Complete the function below so that it uses two variables: height and radius. 
 Use these two variables and print to the screen, the volume of a cylinder. 

 Call this function from the main to test your program.  
 For example, you could test your program with the following values, 

 height 7.0cm and radius 4.0cm
 height 20.0cm and radius 3.0cm
 height 14.7cm and radius 5.2cm
 
 Which prints out, 
 
 the cylinder with height 7.0cm and radius 4.0cm has a volume of 351.86cm^3
'''

def volumeOfACylinder():
  height = (14.7)
  radius = (5.2)
  volume = 3.14159 * (radius * radius) * height
  print("the cylinder with height " + str(height) + "cm and radius " + str(radius) + "cm has a volume of " + str(round(volume, 2)) + "cm^3")
  print("the cylinder with height ", str(height), "cm and radius ", str(radius), "cm has a volume of ", str(round(volume, 2)), "cm^3")
  print(f"the cylinder with height {height}cm and radius {radius}cm has a volume of {round(volume, 2)}cm^3")

print("Question 1\n");
printHelloWorld();

print("\nQuestion 2\n");
printXTenTimes();

print("\nQuestion 3\n");
convertMetricToImperialHeights();

print("\nQuestion 4\n");
fibonacci();

print("\nQuestion 5\n");
volumeOfACylinder();
