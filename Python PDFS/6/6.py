# 6. Matching a String Against a Regular Expression With matches().


from re import match


string = 'Samyak Jain'
print(match(pattern='^Sam', string=string))  # match a str starting with 'Sam'
