import os

def print_file(filepath):
    print('File         :', f"{os.getcwd()}\\{filepath}")
    print('Access time  :', os.path.getatime(filepath))
    print('Modified time:', os.path.getmtime(filepath))
    print('Change time  :', os.path.getctime(filepath))
    print('Size         :', os.path.getsize(filepath), end='\n\n')

def delete_dir(dirname):
    for el in os.listdir(dirname):
        os.remove(f"{dirname}\\{el}")
    os.rmdir(dirname)

if not os.path.isdir("K1"):
    os.mkdir("K1")
if not os.path.isdir("K2"):
    os.mkdir("K2")

with open("K1\\t1.txt", "w", encoding="utf-8") as f:
    f.write("Иванов Иван Иванович, 1965 года рождения, место жительства г. Саратов")
with open("K1\\t2.txt", "w", encoding="utf-8") as f:
    f.write("Петров Сергей Федорович, 1966 года рождения, место жительства г.Энгельс")

with open("K2\\t3.txt", "w", encoding="utf-8") as f:
    f.write("")
with open("K2\\t3.txt", "a", encoding="utf-8") as f:
    with open("k1\\t1.txt", "r", encoding="utf-8") as f1:
        f.write(f1.read())
    with open("k1\\t2.txt", "r", encoding="utf-8") as f2:
        f.write(f2.read())

print_file("K1\\t1.txt")
print_file("K1\\t2.txt")
print_file("K2\\t3.txt")

os.replace("K1\\t2.txt", "K2\\t2.txt")
with open("K2\\t1.txt", "w", encoding="utf-8") as f1:
    with open("K1\\t1.txt", "r", encoding="utf-8") as f2:
        f1.write(f2.read())

input("Нажмите Enter чтобы продолжить.")

if not os.path.isdir("ALL"):
    os.rename("K2", "ALL")
else:
    delete_dir("K2")
delete_dir("K1")

print()
print_file("ALL\\t1.txt")
print_file("ALL\\t2.txt")
print_file("ALL\\t3.txt")