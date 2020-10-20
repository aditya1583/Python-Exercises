#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
"""
phonebook = {
    'Andrew Pearson': 9802789,
    'Emely Pearson': 878987,
    'Lewis Lame': 88767,
    'Aditya Uppu': 2176857725 
}
age = {
    'Aditya': 37,
    'Sunitha':35, 
    'Rishika':4, 
    'Pappu':33
}


print(phonebook['Emely Pearson'])
print(age['Aditya'])

fruits = {("apples", 430), ("bananas", 312), ("oranges", 525), ("pears", 217)}
print(fruits)

car = {'Model':"Chevy",'Year':'1990'}
eng2sp = {"one": "uno", "two": "dos", "three": "tres"}

print(car['Model'])
print(eng2sp["one"])

inventory = {"apples": 430, "bananas": 312, "oranges": 525, "pears": 217}
print(inventory)
del (inventory["pears"])
print(inventory)
inventory["pears"] = 0
print(inventory)
inventory["bananas"] += 200
print(inventory)
print(len(inventory))
# for k in inventory:
# if inventory['apples'] == 430:
#     print(inventory,inventory[k])
"""
print([x**2 for x in range(6)])
print([(x,y) for x in (1,2,3) for y in [3,4,5]] if x != y)