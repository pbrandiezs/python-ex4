number = input("Enter a number? ")
number = int(number)

for I in (range(2,number)):
    if (number % I) == 0:
        print(str(I) + " is a divisor.")
