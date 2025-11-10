# #Exercice 1
# #Instruction
# #Write a function called get_full_name() that takes three arguments: 1: first_name, 2: middle_name 3: last_name.
# #middle_name should be optional, if it’s omitted by the user, the name returned should only contain the first and the last name.
def get_full_name(first_name, last_name, middle_name=""):
    if middle_name: 
        full_name = f"{first_name.capitalize()} {middle_name.capitalize()} {last_name.capitalize()}"
    else:
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
    return full_name
print(get_full_name(first_name="john", middle_name="hooker", last_name="lee"))
print(get_full_name(first_name="bruce", last_name="lee"))
# #Exercice 2
# #Instruction
