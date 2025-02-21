#import os
fruits = ["apple", "banana"]
# Delete a file
#os.remove('example.txt')
# Delete an element from a list
del fruits[1]
print(fruits)  # Output: ['apple']

# Alternatively, using remove()
fruits.remove("apple")
print(fruits)  # Output: []

# Or using pop()
fruits = ["apple", "banana"]
removed_item = fruits.pop(0)  # Removes 'apple'
print(fruits)  # Output: ['banana']

