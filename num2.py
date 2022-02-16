def primes_to_n(n):
    primes = [2]
    a = list(range(n+1))
    a[1] = 0
    primes = list()
    i = 2
    while i <= n:
        if a[i] != 0:
            primes.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return primes


max = 0
array = list()
with open('t2.txt', 'r') as f:
    for row in f:
        number = int(row)
        if number > max:
            max = number
        array.append(number)
primes = primes_to_n(max)
common_items = set(array) & set(primes)
print(len(common_items))
