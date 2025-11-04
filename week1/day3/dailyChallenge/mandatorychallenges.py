# #Challenge 1
# #Instructions 
# #1. User Input:
word = input('Enter a word:')
# #2. Creating the Dictionary:
letter_index = {}
for index, letter in enumerate(word):
    if letter in letter_index:
        letter_index[letter].append(index)
    else:
        letter_index[letter] = [index]
print(letter_index)
# #Challenge 2
items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
wallet = "$300"
wallet = int(wallet.replace("$", "").replace(",", ""))
for item in items_purchase:
    items_purchase[item] = int(items_purchase[item].replace("$", "").replace(",", ""))
basket = []
for item, price in items_purchase.items():
    if price <= wallet:
        basket.append(item)
        wallet -= price  
if not basket:
    print("Nothing")
else:
    print(sorted(basket))
