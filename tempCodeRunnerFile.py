#Tuple2
def count_vowels(characters_tuple):
    vowels = "aeiouAEIOU"
    return sum(1 for char in characters_tuple if char in vowels)
characters_tuple = ('a', 'b', 'c', 'd', 'e', 'A', 'E', 'I', 'O', 'U')
result = count_vowels(characters_tuple)
print(f"The number of vowels in the tuple is: {result}")