from data_storage import read_column
from matplotlib import pyplot
def handle_chart():
    column = int(input("Enter a column you'd like to chart:"))
    x = read_column(-1)
    y = read_column(column)
    pyplot.scatter(x,y, alpha=0.2)
    pyplot.show()