array = list()
with open('num3.txt', 'r') as f:
    for row in f:
        number = float(row.replace(' ', '').replace(',', '.'))
        if number < 0.5:
            array.append(number)

print(len(array))
