def add(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(add(1, 2, 3, 4, 5))