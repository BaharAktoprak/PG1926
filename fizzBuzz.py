a = 0
while a<100:
    a = a+1
    if (a % 3 == 0) and (a % 5 == 0):
        print ("FizzBuzz")
    elif (a % 5 == 0):
        print ("Buzz")
    elif (a % 3 == 0):
        print("Fizz")
    else:
        print(a)