requeseted_topping = 'mushrooms'

if requeseted_topping != 'anchovies':
    print("Hold the anchovies!")

requeseted_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requeseted_toppings)
print('pepperoni' in requeseted_toppings)
requeseted_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requeseted_topping in requeseted_toppings:
    if requeseted_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print("Adding " + requeseted_topping + ".")
print("\nFinished marking your pizza!")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requeseted_toppings = ['mushrooms', 'french peppers', 'extra cheese']
for requeseted_topping in requeseted_toppings:
    if requeseted_topping in available_toppings:
        print("Adding " + requeseted_topping + ".")
    else:
        print("Sorry, we don't have " + requeseted_topping + ".")
print("\nFinished making your pizza!")





