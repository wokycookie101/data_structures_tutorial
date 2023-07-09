set_3 = {"Carrot", "Tomato", "Spinach", "Celery"}
set_4 = {"Spinach", "Kale", "Carrot", "Pepper"}

# These print the exact same things
print(set_3.difference(set_4))
print(set_3 - set_4)

# If you were to reverse the order, you would get the results minus the other list
print(set_4.difference(set_3))
print(set_4 - set_3)