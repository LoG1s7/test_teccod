# Задание 2
# Написать функцию, которая принимает на вход два целых числа
# (минимум и максимум) и возвращает список всех простых чисел
# в заданном диапазоне.

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


def prime_numbers(min_num, max_num):
    primes = [2] if min_num <= 2 else []
    for num in range(max(3, min_num), max_num + 1, 2):
        if is_prime(num):
            primes.append(num)
    return primes


# Пример использования
print(prime_numbers(1, 20))  # Вывод: [2, 3, 5, 7, 11, 13, 17, 19]
