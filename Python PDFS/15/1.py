# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name

stud_data = {1: 'Samyak', 2: 'Rahul', 3: 'Neha', 4: 'Ridhima', 5: 'Python'}
print(stud_data)


# 1.1. Adding the values in dictionary

stud_data[6] = 'new'


# 1.2. Updating the values in dictionary

stud_data[6] = 'New'
print(stud_data)


# 1.3. Accessing the value in dictionary

print(stud_data[5])  # Python


# 1.4. Create a nested loop dictionary

stud_data_nested = {1: {'first_name': 'Samyak', 'last_name': 'Jain'}, 2: {'first_name': 'Arun', 'last_name': 'Maini'}}


# 1.5. Access the values of nested loop dictionary

print(stud_data_nested[2]['first_name'])  # Arun


# 1.6. Print the keys present in a particular dictionary

print(stud_data.keys())


# 1.7. Delete a value from a dictionary

stud_data.pop(6)
# or can use this:
# del stud_data[6]
print(stud_data)
