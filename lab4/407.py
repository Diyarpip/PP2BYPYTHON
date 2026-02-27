def reverse_generator(string):
    for i in range(len(string) - 1, -1, -1):
        yield string[i]

# Чтение входных данных
s = input()

# Использование генератора
for char in reverse_generator(s):
    print(char, end='')
print()