# #Exercise 1
# #Instructions 
# #You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
my_dict = {} 
for key, value in zip(keys, values):
    my_dict[key] = value  
print(my_dict)
# #Exercise 2
# #Instructions
# #Write a program that calculates the total cost of movie tickets for a family based on their ages.
# #Family members’ ages are stored in a dictionary.
# #The ticket pricing rules are as follows:
# #Under 3 years old: Free
# #3 to 12 years old: $10
# #Over 12 years old: $15
family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
price = 0
total = 0
for name, age in family.items():
    if age < 3:
        price = 0
        print(f"{name}:     ${price}")
        total += price
    elif age>3 and age<12:
        price = 10
        print(f"{name}:     ${price}")
        total += price
    else :
        price = 15
        print(f"{name}:     ${price}")
        total += price
print(f"The total price : ${total}")    
# #Exercise 3
# #Instructions
# #Create and manipulate a dictionary that contains information about the Zara brand.
brand = {"name": "Zara",
         "creation_date": 1975,
         "creator_name": "Amancio Ortega Gaona",
         "type_of_clothes":["men", "women", "children", "home"],
         "international_competitors": ["Gap", "H&M", "Benetton"],
         "number_stores": 7000,
         "major_color": {"France": "blue", 
                         "Spain": "red", 
                         "US":["pink", "green"]
                        }
}
# #Change the value of number_stores to 2.
brand["number_stores"]=2   
print(brand["number_stores"])
# #Print a sentence describing Zara’s clients using the type_of_clothes key.
print(f"Zara is for all of {brand['type_of_clothes'][0]}, {brand['type_of_clothes'][1]} and also {brand['type_of_clothes'][2]}.")
# #Add a new key country_creation with the value Spain.
brand ['country_creation'] = "Spain"
print(brand['country_creation'])
# #Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
else:
    print("This category does not exist!")

print(brand["international_competitors"])
# #Delete the creation_date key.
del brand['creation_date']
# #Print the last item in international_competitors.
print(f"The last item in international competitors is : {brand['international_competitors'][-1]}")
# #Print the major colors in the US.
print(f"the major colors in the US are : {brand['major_color']['US']}")
# #Print the number of keys in the dictionary
number_keys = []
number_keys=brand.keys()
print(f"the number of keys in the dictionary is :{len(number_keys)}")
# #Print all keys of the dictionary.
print(f"The keys of the dictionary : {number_keys}")
# #Bonus:
# #Create another dictionary called more_on_zara with creation_date and number_stores. Merge this dictionary with the original brand dictionary and print the result.
more_on_zara= {
                 "creation_date":"Amancio Ortega Gaona",
                 "number_stores": 7000,
}
brand.update(more_on_zara)
print(brand)
# #Exercise 4
# #Instructions
# #You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
# #1. Create a dictionary that maps characters to their indices:
disney_users_A = {}
for index, name in enumerate(users):
    disney_users_A[name] = index
print(disney_users_A)
# #2. Create a dictionary that maps indices to characters:
disney_users_B = {}
for index, name in enumerate(users):
    disney_users_B[index] = name
print(disney_users_B)
# #3. Create a dictionary where characters are sorted alphabetically and mapped to their indices:
disney_users_C = {}
for index, name in enumerate(sorted(users)):
    disney_users_C[name] = index
print(disney_users_C)
