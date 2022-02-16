from matplotlib import pyplot

def handle_chart(x,y):
    column = input("Enter a column you'd like to chart:")
    pyplot.scatter(x,y)
    pyplot.show()