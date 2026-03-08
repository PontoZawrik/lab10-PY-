"""
# Это всё было зря...
def task01():
    f.write("1) ")
    a = rand_double(1, 20)
    b = rand_double(20, 40)
    h = rand_double(1, 5)
    while a < b:
        f.write(f"{round(a, 4)} ")
        a += h
    read_line(f, lambda x, el: not x % 2 == 0)

# номер 2
def task02():
    f.write("2) ")
    for i in range(rand.randint(6, 10)):
        f.write(f"{3 ** i} ")
    read_line(f, lambda x, el: x % 2 == 0)

def task04():
    f.write("4) ")
    num1 = 0
    num2 = 1
    for i in range(rand.randint(10, 15)):
        f.write(f"{num1} ")
        num1 += num2
        num2 = num1 - num2
        num1 -= num2
        num2 += num1
    read_line(f, lambda x, el: not x % 3 == 0)

def task05():
    f.write("5) ")
    nums = [rand.randint(20, 100) for _ in range(rand.randint(10, 15))]
    for num in nums:
        if num % 2 == 0:
            f.write(f"{num} ")
    read_line(f, lambda x, el: True)

def task06():
    f.write("6) ")
    nums = [rand.randint(-100, 100) for _ in range(rand.randint(10, 15))]
    for num in nums:
        if num < 0:
            f.write(f"{num} ")
    read_line(f, lambda x, el: True)

def task07():
    f.write("7) ")
    nums = [rand.randint(-100, 100) for _ in range(rand.randint(10, 15))]
    a = rand.randint(-100, 100)
    b = rand.randint(-100, 100)

    if a > b:
        a += b
        b = a - b
        a -= b

    print(f"Интервал: {a} - {b}")
    for num in nums:
        if a < num < b:
            f.write(f"{num} ")
    read_line(f, lambda x, el: True)

def task08():
    f.write("8) ")
    nums = [rand.randint(-100, 100) for _ in range(rand.randint(10, 15))]
    a = rand.randint(2, 5)
    print(f"Число: {a}")
    for num in nums:
        if not num % a == 0:
            f.write(f"{num} ")
    read_line(f, lambda x, el: True)

def task09():
    f.write("9) ")
    nums = [round(rand_double(-50, 50), 4) for _ in range(rand.randint(10, 15))]
    a = rand.randint(-50, 50)
    b = rand.randint(-50, 50)

    if a > b:
        a += b
        b = a - b
        a -= b

    print(f"Интервал: {a} - {b}")
    for num in nums:
        f.write(f"{num} ")
    read_line(f, lambda x, el: a < float(el) < b)

def task10():
    f.write("10) ")
    nums = [round(rand_double(-100, 100), 4) for _ in range(rand.randint(10, 15))]
    a = rand.randint(-100, 100)
    print(f"Заданное число: {a}")
    for num in nums:
        f.write(f"{num} ")
    read_line(f, lambda x, el: not x % 2 == 0 and float(el) > a)

def task11():
    f.write("11) ")
    nums = [round(rand_double(-100, 100), 4) for _ in range(rand.randint(10, 15))]
    a = rand.randint(-100, 100)
    print(f"Заданное число: {a}")
    for num in nums:
        f.write(f"{num} ")
    read_line(f, lambda x, el: x % 2 == 0 and float(el) < a)

def task12():
    f.write("12) ")
    nums = [round(rand_double(-100, 100), 4) for _ in range(rand.randint(10, 15))]
    for num in nums:
        f.write(f"{num} ")
    read_line(f, lambda x, el: float(el) > 0)

def task13():
    f.write("13) ")
    nums = [round(rand_double(-100, 100), 4) for _ in range(rand.randint(10, 15))]
    for num in nums:
        f.write(f"{num} ")
    f.seek(0)
    line = f.readline().split()[1:]
    avg = count = 0
    for i in range(len(line)):
        if i % 2 == 0:
            count += 1
            avg += float(line[i])
    print(f"Среднее арифметическое: {avg / count}")

def task14():
    f.write("14) ")
    nums = [round(rand_double(-100, 100), 4) for _ in range(rand.randint(10, 15))]
    for num in nums:
        f.write(f"{num} ")
    f.seek(0)
    line = f.readline().split()[1:]
    max = float(line[0])
    for i in range(len(line)):
        if max < float(line[i]) and not i % 2 == 0:
            max = float(line[i])
    print(f"Максимальное число: {max}")
"""

import random as rand

def read_line(file, input_func):
    file.seek(0)
    line = file.readline().split()[1:]
    for i in range(len(line)):
        if input_func(i, line[i]):
            print(line[i], end=" ")

def rand_double(min, max):
    return  min + rand.random() * (max - min)

def task03():
    f.write("3) ")
    for i in range(1, rand.randint(6, 10)):
        f.write(f"{round(1 / i, 4)} ")
    read_line(f, lambda x, el: x % 3 == 0)

with open("file01.txt", "w+") as f:
    f.write("3) ")
    for i in range(1, rand.randint(6, 10)):
        f.write(f"{round(1 / i, 4)} ")
    read_line(f, lambda x, el: x % 3 == 0)