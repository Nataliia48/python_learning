# Задача 1
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5}

print("Задача 1:")
print(f"set1: {set1}")
print(f"set2: {set2}")
print(f"set1 == set2: {set1 == set2}")
print(f"set1 is set2: {set1 is set2}")
print()

# Задача 2
print("Задача 2:")
print("Результат порівняння:")
print(f"set1 == set2: {set1 == set2}")
print(f"set1 is set2: {set1 is set2}")

print("\nПояснення:")
print("== порівнює ВМІСТ об'єктів - тому True")
print("is порівнює ІДЕНТИЧНІСТЬ об'єктів в пам'яті - тому False")
print("Це два різні об'єкти з однаковим вмістом")
print()

# Задача 3
print("Задача 3:")
print(f"set1 is set2: {set1 is set2}")

print("\nПояснення результату:")
print("Результат False, тому що:")
print("- Оператор 'is' перевіряє чи це той самий об'єкт в пам'яті")
print("- set1 і set2 - це два різні об'єкти")
print("- Навіть якщо вони мають однаковий вміст, вони знаходяться в різних місцях пам'яті")

set3 = set1
print(f"\nДля порівняння:")
print(f"set3 = set1")
print(f"set1 is set3: {set1 is set3}")
print()

# Задача 4
print("Задача 4:")
my_set = {10, 20, 30, 40, 50}
print(f"Наш набір: {my_set}")

elements_to_check = [10, 25, 30, 100, 50]

print("\nПеревірка елементів оператором 'in':")
for element in elements_to_check:
    if element in my_set:
        print(f"Елемент {element} ЗНАЙДЕНО в наборі")
    else:
        print(f"Елемент {element} НЕ ЗНАЙДЕНО в наборі")

print("\nДодаткові приклади:")
print(f"20 in my_set: {20 in my_set}")
print(f"75 in my_set: {75 in my_set}")
print(f"40 not in my_set: {40 not in my_set}")

print("\n" + "="*50)
print("БОНУС: Робота з різними типами в set")

string_set = {"apple", "banana", "orange"}
print(f"\nSet з рядками: {string_set}")
print(f"'apple' in string_set: {'apple' in string_set}")
print(f"'grape' in string_set: {'grape' in string_set}")

mixed_set = {1, "hello", 3.14, True}
print(f"\nSet зі змішаними типами: {mixed_set}")
print(f"1 in mixed_set: {1 in mixed_set}")
print(f"'hello' in mixed_set: {'hello' in mixed_set}")
print(f"3.14 in mixed_set: {3.14 in mixed_set}")

print(f"\nЦікавий факт: True == 1 в Python: {True == 1}")
print("Тому в set {1, True} буде тільки один елемент!")