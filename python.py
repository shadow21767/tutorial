# Comments: are used to ignore a part of a program, provide context why something is written the way it is.

#print(): tell a computer to talk
print("Hello World")

#Strings: blocks of text surrounded by double quotes or single quotes
print("Gh0st141")
print('Gh0st141')

#Variables: method of storing data for reuse
planet_name = "Mars"
print(planet_name)
        #Variable: numbers don't need quotes
planet_number = 4
print(planet_number)

#Integer (int) is a whole number. No decimal point and contains all counting numbers, even negative numbers
#Floating-point number (float) is a decimal number. Used to represent fractional quantities as well as precise measurements
an_int = 2
a_float = 2.1
print(an_int + 3)

#Calculations: the arithmetic operations of addition (+), subtraction (-), multiplication (*), and division (/)
print(141 + 141)
print(141 - 23)
print(141 / 12)
print(141 * 90)
print(573 - 70 + 1 * 90)

#Changing numbers
banana_price = 1.50
number_of_bananas = 100
print(banana_price * number_of_bananas)

banana_price = 5.00
print(banana_price * number_of_bananas)

number_of_bananas = 50
print(banana_price * number_of_bananas)

#Exponents: just exponents (**)
print(10 ** 10)
print(10 ** -5)
print(60 ** 0.5)

#Modulo: Gives the remainder of a division calculation. If divisible, then the result is 0.
print(30 % 5)
print(36 % 10)

#Concatenation: combining two strings (string concatenation)
ghost_quote_1 = "Let's"
ghost_quote_2 = " do this!" #needs a space
print(ghost_quote_1 + ghost_quote_2)

ghost_quote_1 = "Let's"
ghost_quote_2 = "do this!" #space is applied to the concatenation
ghost_quote_combined = ghost_quote_1 + " " + ghost_quote_2
print(ghost_quote_combined)

soap_quote_1 = "I got"
soap_kill_streak = 20
soap_quote_2 = "kills."
soap1 = soap_quote_1 + " " + str(soap_kill_streak) + " " +soap_quote_2 
print(soap1)
print(soap_quote_1, soap_kill_streak, soap_quote_2)

#Plus Equals: add to the current valus of the variable (+=)
number_of_miles_hiked = 12
number_of_miles_hiked += 2
print(number_of_miles_hiked)

car_caption = "Smokey Nagata's V12 Supra, looks fantastic!"
car_caption += " #V12"
car_caption += " #ToyotaSupra"
car_caption += " #Smokey"
print(car_caption)

#Multi-line strings: using three quotemarks (""" or ''')
ghost_quote = """
We have a nuclear missile launch! 
Missile in the air! 
Missile in the air!
Code Black!
Code Black!
"""
print(ghost_quote)

#User Input
favorite_car = input("What is your favorite car? ") #Don't forget to leave a space.
print("My favorite car is " + favorite_car + ".")
