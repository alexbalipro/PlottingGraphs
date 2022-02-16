user_menu = """Please choose from the following 
- Enter 'c' to chart a new graph.
- Enter 'q' to quit.
Your selection:
"""
charting_menu = "Enter the column you'd like to chart: "
def handle_chart():
    column = int(input(charting_menu))

while True:
    user_selection =