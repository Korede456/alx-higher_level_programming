#!/usr/bin/python3
print_sorted_dictionary = (
    __import__('6-print_sorted_dictionary').print_sorted_dictionary
)

a_dictionary = {
    'language': "C", 'Number': 89, 'track': "low level", 'ids': [1, 2, 4]
}
print_sorted_dictionary(a_dictionary)
