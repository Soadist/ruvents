counter = 0
with open('date1.txt', 'r') as f:
    for row in f:
        if row.split(' ')[0] == 'Tue':
            counter += 1
print(counter)
