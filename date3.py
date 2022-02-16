from datetime import datetime, timedelta
counter = 0
days_list = []
with open('t6.txt', 'r') as f:
    for row in f:
        day = datetime.strptime(row.replace('\n', ''), '%m-%d-%Y')
        if (
            day.timetuple()[6] == 1 and
            day.timetuple()[1] != (day + timedelta(7)).timetuple()[1]
        ):
            counter += 1
print(counter)
