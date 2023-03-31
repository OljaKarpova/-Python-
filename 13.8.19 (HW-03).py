kol_uchastnikov = int(input("Введите количество билетов: "))
summa = 0
for i in range(kol_uchastnikov):
    if kol_uchastnikov == 1:
        vozrast = int(input("Введите возраст участника: "))
        if vozrast < 18:
            summa = 0
        elif 18 <= vozrast < 25:
            summa = 990
        else:
            summa = 1390
    elif 1 <  kol_uchastnikov < 4:
        k = i + 1
        vozrast = int(input("Введите возраст %d-го участника: " % (k)))
        if vozrast < 18:
            summa += 0
        elif 18 <= vozrast < 25:
            summa += 990
        else:
            summa += 1390
    else:
        k = i + 1
        vozrast = int(input("Введите возраст %d-го участника: " % (k)))
        if vozrast < 18:
            summa += 0
        elif 18 <= vozrast < 25:
            summa = summa + round(0.9*990)
        else:
            summa = summa + round(0.9*1390)
print("Общая сумма к оплате: ", summa, "руб.")