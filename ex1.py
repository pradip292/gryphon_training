#List1
def sum_of_even_numbers(numbers):
    return sum(num for num in numbers if num % 2 == 0)
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(numbers_list)
print(f"The sum of even numbers in the list is: {result}")

#List2
def longest_word(words):
    return max(words, key=len, default=None)
word_list = ["Pradip", "akshay", "Vaibhav", "Sanket", "YAsh"]
result = longest_word(word_list)
print(f"The longest word in the list is: {result}")

#List3
def  duplicates(characters):
    return list(dict.fromkeys(characters))
input_characters = ['a', 'b', 'c', 'd', 'a', 'b', 'x']
result = duplicates(input_characters)
print(f"List after removing duplicate characters: {result}")

#List4
def sort_numbers_in_ascending_order(numbers):
    sorted_numbers = sorted(numbers)
    return sorted_numbers
input_numbers = [5, 2, 8, 1, 3]
sorted_result = sort_numbers_in_ascending_order(input_numbers)
print(f"Sorted list in ascending order: {sorted_result}")


#List5
def reverse_words(words):
    reversed_words = list(reversed(words))
    return reversed_words
input_words = ["Pradip", "akshay", "Vaibhav", "Sanket", "YAsh"]
reversed_result = reverse_words(input_words)
print(f"List of words after reversing the order: {reversed_result}")

#Tuple1
def average_of_numbers(numbers_tuple):
    if not numbers_tuple:
        return None 
    return sum(numbers_tuple) / len(numbers_tuple)
numbers_tuple = (10, 20, 30, 40, 50)
result = average_of_numbers(numbers_tuple)
print(f"The average of numbers in the tuple is: {result}")

#Tuple2
def count_vowels(characters_tuple):
    vowels = "aeiouAEIOU"
    return sum(1 for char in characters_tuple if char in vowels)
characters_tuple = ('a', 'b', 'c', 'd', 'e', 'A', 'E', 'I', 'O', 'U')
result = count_vowels(characters_tuple)
print(f"The number of vowels in the tuple is: {result}")

#Tuple3
def find_max_min_values(numbers_tuple):
    if not numbers_tuple:
        return None, None 
    max_value = max(numbers_tuple)
    min_value = min(numbers_tuple)
    return max_value, min_value
numbers_tuple = (10, 5, 8, 20, 15)
max_value, min_value = find_max_min_values(numbers_tuple)
print(f"Maximum value in the tuple: {max_value}")
print(f"Minimum value in the tuple: {min_value}")

#Tuple4
def reverse_words_in_tuple(words_tuple):
    for word in words_tuple:
        reversed_word = ''.join(reversed(word))
        print(f"Reversed order of '{word}': {reversed_word}")
words_tuple = ("apple", "banana", "orange", "kiwi")
reverse_words_in_tuple(words_tuple)

#Set1
def is_palindrome(characters_tuple):
    joined_string = ''.join(characters_tuple)
    reversed_string = joined_string[::-1]
    return joined_string == reversed_string
characters_tuple1 = ('H', 'E', 'L', 'L', 'O')
characters_tuple2 = ('S', 'A', 'N', 'J', 'I','V','A','N','I')
print(f"Is tuple1 a palindrome? {is_palindrome(characters_tuple1)}")
print(f"Is tuple2 a palindrome? {is_palindrome(characters_tuple2)}")

#Set2
def sum_of_numbers_in_set(number_set):
    return sum(number_set)
numbers_set = {1, 2, 3, 4, 5}
result = sum_of_numbers_in_set(numbers_set)
print(f"The sum of numbers in the set is: {result}")

#Set3
def remove_duplicates_set(word_set):
    unique_words_set = set()
    for word in word_set:
        unique_words_set.add(word)
    return unique_words_set
words_set = {"Pradip", "akshay", "Vaibhav", "Sanket", "YAsh"}
unique_words_result = remove_duplicates_set(words_set)
print(f"Set of words after removing duplicates: {unique_words_result}")

#Set4
def find_max_min_values_in_set(number_set):
    if not number_set:
        return None, None  
    max_value = max(number_set)
    min_value = min(number_set)
    return max_value, min_value
numbers_set = {10, 5, 8, 20, 15}
max_value, min_value = find_max_min_values_in_set(numbers_set)
print(f"Maximum value in the set: {max_value}")
print(f"Minimum value in the set: {min_value}")

#Set5
def are_sets_equal(set1, set2):
    return set1 == set2
set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 1, 2}
result = are_sets_equal(set_a, set_b)
print(f"Are set A and set B equal? {result}")

#Dict1
def count_key_value_pairs(dictionary):
    return len(dictionary)
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
result = count_key_value_pairs(my_dict)
print(f"The number of key-value pairs in the dictionary is: {result}")

#Dict2
def print_keys_and_values(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print_keys_and_values(my_dict)

#Dict3
def print_definition(dictionary, word):
    definition = dictionary.get(word)
    if definition is not None:
        print(f"Definition of '{word}': {definition}")
    else:
        print(f"Word '{word}' not found in the dictionary.")
word_definitions = {'apple': 'a round fruit with red or green skin and a whitish interior',
                   'banana': 'a long curved fruit with a yellow skin',
                   'kiwi': 'a small, brown, fuzzy fruit with green flesh'}
given_word = input("Enter a word to get its definition: ")
print_definition(word_definitions, given_word)

#Dict4
def calculate_average_grades(student_grades):
    return {student: sum(grades) / len(grades) for student, grades in student_grades.items()}
student_grades = {'Pradip': [85, 90, 92],
                  'Akshay': [78, 85, 80],
                  'Vaibhav': [90, 92, 88]}
average_grades_result = calculate_average_grades(student_grades)
for student, average_grade in average_grades_result.items():
    print(f"{student}'s average grade is: {average_grade}")

#Dict5
def calculate_average_grades(student_grades):
    return {student: sum(grades) / len(grades) for student, grades in student_grades.items()}
student_grades = {'Pradip': [85, 90, 92],
                  'Akshay': [78, 85, 80],
                  'Vaibhav': [90, 92, 88]}
average_grades_result = calculate_average_grades(student_grades)
for student, average_grade in average_grades_result.items():
    print(f"{student}'s average grade is: {average_grade}")
    
#Sorting Dict1
def sort_dictionary_by_keys(dictionary):
    sorted_dict = dict(sorted(dictionary.items()))
    return sorted_dict
word_definitions = {'apple': 'a round fruit with red or green skin and a whitish interior',
                   'banana': 'a long curved fruit with a yellow skin',
                   'kiwi': 'a small, brown, fuzzy fruit with green flesh'}

sorted_result = sort_dictionary_by_keys(word_definitions)

for word, definition in sorted_result.items():
    print(f"{word}: {definition}")
    
