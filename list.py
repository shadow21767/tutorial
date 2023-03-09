#A list is one of the many built-in data structures that allows us to work with a collection of data in sequential order.
heights = [70, 67, 61, 2]
print(heights)

#A list can store, name, multiple data types, string, integers, boolean, and float(decimals)
animals = ["Tiger", "Lion", "Eagle", "Owl"]
print(animals)
#multiple data types
students_grade = [["Lisa",50],["Jessica", 80], ["Harvey", 100], ["Mike", 100], ["Louis", 95]]
print(students_grade)

mixed_list_common = ["Rachel", 29, True, 0.9]
print(mixed_list_common)

#Empty Lists: planning on filling it up later based on some other input.
empty_list = []

#List Methods: built-in functionality that we can use to create, manipulate, and even delete our data.
append_example = [98, 50, 100, 30]

append_example.append(400)
print(append_example)

append_example.remove(30)
print(append_example)

#Growing a List: Append
cars = []
cars.append("Ferrari")
cars.append("Lambo")
print(cars)

#Growing a List: Plus (+) - add multiple items to a list, we can use + to combine two lists (this is also known as concatenation)
lamborghini = ["Huracan", "Urus"]
print(lamborghini)
lamborghini_new = ["Aventador", "Sian"]
print(lamborghini_new)
lamborghini_models = lamborghini + lamborghini_new
print(lamborghini_models)

#Accessing List Elements: Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1
print(lamborghini_models[0])
print(lamborghini_models[2])

#Accessing List Elements: Negative Index - We can use the index -1 to select the last item of a list, even when we don't know how many elements are in a list
print(lamborghini_models[-1])
print(lamborghini_models[-4])

#Modifying List Elements: To change a value in a list, reassign the value using the specific index
toyota = ["Tacoma", "Toyota", "Carolla", "Prius"]
print(toyota)
toyota[2] = "Camry"
print(toyota)
toyota[-1] = "Crown"
print(toyota)

#Shrinking a List: Remove - remove elements in a list
movies_2023 = ["John Wick 4", "Varisu", "Leo", "Creed 3", "Fast and Furious 10"]
print(movies_2023)
movies_2023.remove("Leo")
print(movies_2023)

#Two-Dimensional (2D) Lists - List containing another list
transformers_movie_release_years = [["Transformers", 2007], ["Transformers: ROTF", 2009], ["Transformers: DOTM", 2011], ["Transformers: AOE", 2014], ["Transformers: Last Knight", 2017]]
print(transformers_movie_release_years)

#Accessing 2D Lists: 2D lists can be accessed similar to their one-dimensional counterpart. Providing a single pair of brackets [] we will use an additional set for each dimension past the first
rotf_transformers = transformers_movie_release_years[1][1]
print(rotf_transformers)

#Modifying 2D Lists: access 2D lists, modifying the elements should come naturally
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
print(class_name_hobbies)
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)
class_name_hobbies[-1][-1] = "Football"
print(class_name_hobbies)