# Part 1: Lists and Tuples

# 1
fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# 2
fruits[2] = "pineapple"

# 3
fruits.append("watermelon")

# 4
numbers = (5, 2, 8, 1, 7)

# 5
second_element = numbers[1]

# Displaying the results
print("1: List 'fruits' after modification:", fruits)
print("2: Modified third element in 'fruits':", fruits[2])
print("3: List 'fruits' after adding 'watermelon':", fruits)
print("4: Tuple 'numbers':", numbers)
print("5: Accessing the second element in 'numbers':", second_element)



# Part 2: Sets

# 6
colors = {"red", "blue", "green", "yellow"}

# 7
colors.add("purple")

# 8
colors.remove("green")

# 9
is_orange_present = "orange" in colors

# Displaying the results
print("6: Set 'colors':", colors)
print("7: Set 'colors' after adding 'purple':", colors)
print("8: Set 'colors' after removing 'green':", colors)
print("9: Is 'orange' present in 'colors'?", is_orange_present)



# Part 3: Dictionaries

# 10
student = {"name": "Alice", "age": 20, "course": "Python Programming"}

# 11
student["age"] = 21

# 12
student["grade"] = "A"

# 13
student.pop("course", None)

# Displaying the results
print("Task 10: Dictionary 'student':", student)
print("Task 11: Modified age in 'student':", student["age"])
print("Task 12: Dictionary 'student' after adding 'grade':", student)
print("Task 13: Dictionary 'student' after removing 'course':", student)



# Part 4: Sorting Dictionaries

# 14
population = {"USA": 331002651, "China": 1444216107, "India": 1380004385, "Brazil": 212559417, "Russia": 145912025}

# 15
sorted_population_by_country = dict(sorted(population.items()))

# 16
sorted_population_by_population = dict(sorted(population.items(), key=lambda item: item[1], reverse=True))

# Displaying the results
print("14: Dictionary 'population':", population)
print("15: Sorted dictionary 'population' by country names (ascending):", sorted_population_by_country)
print("16: Sorted dictionary 'population' by population values (descending):", sorted_population_by_population)


#Key Differences:

#Lists:

#Mutable: Can be changed.
#Ordered: Has a specific order.
#Syntax: Square brackets [].
#Example: [1, 2, 3]
#Tuples:

#Immutable: Can't be changed.
#Ordered: Has a specific order.
#Syntax: Parentheses ().
#Example: (1, 2, 3)
#Sets:

#Mutable: Can be changed.
#Unordered: No specific order.
#Syntax: Curly braces {}.
#Example: {1, 2, 3}
#Dictionaries:

#Mutable: Key-value pairs can be changed.
#Unordered: No specific order.
#Syntax: Curly braces {} with key-value pairs.
#Example: {'name': 'Alice', 'age': 25}
#Importance of Sorting Dictionaries:
#Search: Makes searching for specific keys or values faster.
#Display: Presents data in an organized way for readability.
#Algorithms: Some algorithms require sorted dictionaries.
#Consistency: Ensures a consistent order for predictable behavior.
#Sorting dictionaries is useful for efficiency, readability, and meeting specific requirements in different scenarios.

