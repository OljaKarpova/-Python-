# Предлагаем пользователю ввести исходные данные. Переводим последовательность в список и число в тип "число". Исключаем ошибки ввода
try:
    array = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
    if len(array) == 1:
        print("Ошибка! Вы ввели только одно число. Пожалуйста, перезапустите код и введите несколько чисел ЧЕРЕЗ ПРОБЕЛ!")
        exit()
except ValueError:
    print("Ошибка! Вы ввели символы, отличные от чисел и пробелов. Пожалуйста, перезапустите код и введите только числа через пробел!")
    exit()
try:
    element = int(input("Введите одно любое число: "))
except ValueError:
    print("Ошибка! Вы ввели символы, отличные от числа. Пожалуйста, перезапустите код и введите на этом шаге ОДНО ЧИСЛО!")
    exit()

# Добавляем число element в последовательность (список) array
array.append(element)

# Функция "быстрой сортировки" списка по возрастанию с применением случайной выборки ведущего элемента
import random
def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
    if j > left:
       qsort_random(array, left, j)
    if right > i:
       qsort_random(array, i, right)
    return array

# Применяем функцию "быстрой сортировки"
array_sorted = qsort_random(array, 0, len(array) - 1)

# Функция "двоичного поиска" индекса элемента, стоящего до элемента element, в отсортированном списке array (+условия задачи)
def binary_search(array_sorted, element, left, right):
    middle = (right + left) // 2
    if array_sorted[middle] == element:
        # исключим вероятность, что поиск нашел не первое вхождение числа element, дойдем до первого вхождения
        while array_sorted[middle] == array_sorted[middle - 1]:
          middle = middle - 1
        # пропишем случай, когда в списке нет чисел меньше искомого числа element
        if middle == 0:
            return f"Элемента, меньшего, чем {element}, во введенной последовательности нет. Задача не имеет решения."
        # пропишем случай, когда большего или равного искомому числу element чисел в списке нет
        elif middle == len(array_sorted) - 1:
            return f"Элемента, большего, чем {element}, во введенной последовательности нет. Задача не имеет решения."
        # пропишем случай, когда число element дублировало самое большое число последовательности, но такое число в начальной последовательности было одно
        elif middle == len(array_sorted) - 2 and array_sorted[len(array_sorted) - 2] == array_sorted[len(array_sorted) - 1]:
            return f"Элемента, большего, чем {element}, во введенной последовательности нет. Задача не имеет решения."
        # и, наконец, когда учли все частные случаи, найдем индекс элемента, идущего до числа element в отсортированной последовательности
        else:
            index = middle - 1
            return f"Ответ: '{index}' - номер позиции элемента, который меньше введенного числа {element}, а следующий за ним элемент больше или равен этому числу."

    elif element < array_sorted[middle]:
        return binary_search(array_sorted, element, left, middle - 1)
    else:
        return binary_search(array_sorted, element, middle + 1, right)

# Применяем функцию "двоичного поиска" и выводим ответ
print(binary_search(array_sorted, element, 0, len(array_sorted) - 1))
