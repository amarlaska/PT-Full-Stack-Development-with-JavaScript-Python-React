from decimal import Decimal
import math


# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.
print('Exercise 1')

ex1_list = ['Alba', 'María', 'Pedro', 'Saray']
ex1_tuple = ('Iñigo', 'Jonatan', 'Ibai', 'Israel')
ex1_float = 23.3
ex1_integer = 34
ex1_decimal = Decimal('34.55')
ex1_dictionary = {
    "apertura" : "Marlaska",
    "zaguero" : "Adriana",
    "mediomele" : "Mariana"
}

print(ex1_list)
print(ex1_tuple)
print(ex1_float)
print(ex1_integer)
print(ex1_decimal)
print(ex1_dictionary)
print()

#Exercise 2: Round your float up.
print('Exercise 2')

print(math.ceil(ex1_float))
print()

#Exercise 3: Get the square root of your float.
print('Exercise 3')
square_root_of_ex1_float = math.sqrt(ex1_float)
print(square_root_of_ex1_float)
print()

#Exercise 4: Select the first element from your dictionary.
print('Exercise 4')
first_value = list(ex1_dictionary.values())[0]
print(first_value)
print()

#Exercise 5: Select the second element from your tuple.
print('Exercise 5')
print(ex1_tuple[1])
print()

#Exercise 6: Add an element to the end of your list.
print('Exercise 6')
ex1_list.append('Mikel')
print(ex1_list)
print()

#Exercise 7: Replace the first element in your list.
print('Exercise 7')
ex1_list[0] = 'Mirari'
print(ex1_list)
print()

#Exercise 8: Sort your list alphabetically.
print('Exercise 8')
ex1_list.sort()
print(ex1_list)
print()

#Exercise 9: Use reassignment to add an element to your tuple.
print('Exercise 9')
ex1_tuple = ex1_tuple + ('Vega',)
print(ex1_tuple)