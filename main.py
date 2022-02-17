from matplotlib import pyplot
import graphing
import data_storage
user_menu = """Please choose from the following options:
Enter "c" - to chart a new graph.
Enter "q" - quit.
Your selection:
"""
charting_menu = "Enter the column you would like to chart"

while True:
    user_selection = input(user_menu)
    if user_selection == 'q':
        break
    elif user_selection == 'c':
        graphing.handle_chart()
    else:
        print(f"Sorry {user_selection} is not a valid option")