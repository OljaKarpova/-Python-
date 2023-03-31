kol_uchastnikov = int(input("Введите количество билетов: "))
summa = 0 #Заводим счетчик стоимости билетов
for i in range(kol_uchastnikov): #Цикл, где для каждого участника будем запрашивать возраст
    if kol_uchastnikov == 1: #Вариант, когда участник один
        vozrast = int(input("Введите возраст участника: ")) #Формулировка запроса отличается от остальных случаев
        if vozrast < 18:
            summa = 0
        elif 18 <= vozrast < 25:
            summa = 990
        else:
            summa = 1390
    elif 1 < kol_uchastnikov < 4: #Вариант, когда участников до 3 включительно, скидка еще не действует
        k = i + 1
        vozrast = int(input("Введите возраст %d-го участника: " % (k)))
        if vozrast < 18:
            summa += 0
        elif 18 <= vozrast < 25:
            summa += 990
        else:
            summa += 1390
    else: #Вариант, когда участников больше 3, действует скидка
        k = i + 1
        vozrast = int(input("Введите возраст %d-го участника: " % (k)))
        if vozrast < 18:
            summa += 0
        elif 18 <= vozrast < 25:
            summa = summa + round(0.9*990)
        else:
            summa = summa + round(0.9*1390)
print("Общая сумма к оплате: ", summa, "руб.")