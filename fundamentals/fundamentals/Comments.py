# déclaration des variables
# Varibale int
num1 = 42
# Varibale float
num2 = 2.3
# Varibale booléene
boolean = True
# Varibale string
string = 'Hello World'
# List
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# Dictionnaire
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# Tuples
fruit = ('blueberry', 'strawberry', 'banana')
# Affichage des éléments de tuples
print(type(fruit))
# affichage de l'élément 2 de la liste 
print(pizza_toppings[1])
# ajout de l'élément Maushrooms à la liste
pizza_toppings.append('Mushrooms')
#  affichage du key name du dictionnaire
print(person['name'])
# affecter la valeur george au key name 
person['name'] = 'George'
#  ajout d'un key/value au dictionnaire
person['eye_color'] = 'blue'
# affichage du 3ème élément du tuple
print(fruit[2])

# Affichage d'un résultat selon une condition
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#  # Affichage d'un résultat selon la longueur de la chaine 
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# affichage d'un nombre entre  0 et 4 
for x in range(5):
    print(x)
# affichage d'un nombre entre  2 et 4 
for x in range(2,5):
    print(x)
# affichage d'un nombre entre  2 et 9  avec un pas 3 
for x in range(2,10,3):
    print(x)
# affichage d'un nombre entre  0 et 4 
x = 0
while(x < 5):
    print(x)
    x += 1
# suppression du dernier élément de la liste
pizza_toppings.pop()
# suppression du deuxième élément de la liste
pizza_toppings.pop(1)
# affichage des élément du dictionnaire 
print(person)
# suppression du key eye color
person.pop('eye_color')
# affichage des élément du dictionnaire 
print(person)

# selon la condition si pepperoni continuer si olive sortir de la boucle
for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
# fonction qui permet d'afficher hello de 10 fois
def print_hello_ten_times():
    for num in range(10):
        print('Hello')
# innoke function
print_hello_ten_times()
# fonction qui permet d'afficher autant de fois hello de x entrée en tant que paramètre
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
# invoke function pour répéter héllo 4 fois
print_hello_x_times(4)
# fonction qui permet d'afficher autant de fois hello de x entrée en tant que paramètre et x doit étre inférieur à 10
def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
# invoke functions
print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
num3=50
print(num3)
# num3 = 72
num3=72
print(num3)
# fruit[0] = 'cranberry'

# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)