counter = 0
with open('t1.txt', 'r') as f:
    for row in f:
        check = int(row)
        if check % 2 == 0 and check != 0:
            counter += 1
print(counter)
