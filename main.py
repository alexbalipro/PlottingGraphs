from matplotlib import pyplot
import graphing
user_manu = """Please choose from the following options:
Enter "c" - to chart a new graph.
Enter "q" - quit.
Your selection:
"""
x_data = [1, 2, 3, 4, 5]
y_data = [5.5, 6.4, 5.3, 4.4, 7.9]

while True:
    user_selection = input(user_manu)
    if user_selection == 'q':
        break
    elif user_selection == 'c':
        graphing.handle_chart(x_data,y_data)
    else:
        print(f"Sorry {user_selection} is not a valid option")