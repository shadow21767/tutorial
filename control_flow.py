#Boolean Expessions: check if something is True or False
#Statement One: A car is mammal.
statement_one = "Yes" #If the statement a statement or opinion
#Statement Two: Cars make a best friend
statement_two = "No"

#Relational Operators: Equals (==) and Not Equals (!=)
statement_three = (5 * 2) - 1 == 8 + 1
statement_four = 13 - 6 != (3 * 2) + 1
statement_five = 3 * (2 - 1) == 4 - 1
print(statement_three, statement_four, statement_five)

#Boolean Variables: True and False
if_bool = "true"
print(type(if_bool)) #It is a string not boolean

if_bool_two = True
print(type(if_bool_two)) #It is a boolean

#If Statement
is_raining = True
if is_raining:
    print("Bring an umbrella")

if 3 == 4 -1:
    print("Math rocks")

car = "Porsche 911"
if car == "Nissan GTR":
    print("That's not the car.")
if car == "Porsche 911":
    print("I will get that car in the future.")

#Relational Operators II: greater than (>), greater than or equal to (>=), less than (<), less than or equal to (<=)
x = 19
y = 20
if x == y:
    print("They are the same numbers!")

speed_limit = 120
if speed_limit > 45:
    print("Slow Down!")

#Boolean Operators: and (combines two boolean expression and evaluates as True)
bool_and_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(bool_and_one)
bool_and_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(bool_and_two)

speed = 100
mile = 2
if speed >= 45 and mile <= 10:
    print("You will get to your destination in few minutes!")

#Boolean Operators: or (combines two expressions into a larger expression that is True, if either component is True.)
bool_or_one = (2 - 1 > 3) or (-5 * 2 == -10)
print (bool_or_one)
bool_or_two = (9 + 5 <= 15) or (7 != 4 + 3)
print(bool_or_two)

speed = 100
mile = 12
if speed >= 45 or mile <=10:
    print("You will get there a bit late!")
