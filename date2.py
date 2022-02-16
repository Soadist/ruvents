from datetime import datetime
counter = 0
with open('t5.txt', 'r') as f:
    for row in f:
        day = datetime.strptime(row.split(' ')[0], '%Y-%m-%d')
        if day.timetuple()[6] == 1:
            counter += 1
print(counter)
