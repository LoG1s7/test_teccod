# Задание 4
# Написать программу, которая сортирует список строк по длине,
# сначала по возрастанию, а затем по убыванию


def sort_strings_by_length(strings):
    return sorted(strings, key=len) + sorted(strings, key=len, reverse=True)


# Пример использования
print(sort_strings_by_length(["apple", "banana", "cherry",
                              "date"]))
# Вывод:
# ['date', 'apple', 'banana', 'cherry', 'banana', 'cherry', 'apple', 'date']
