def read_column(column):
    column_data = []
    with open('iris.csv', 'r') as iris:
        for line in iris.readlines()[1:]:
            data = line.strip().split(',')
            column_data.append(data[column])
    return column_data


