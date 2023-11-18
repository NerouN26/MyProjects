print("программа конвектор величин")
print("")
print("Для его использования нужно:")
print("1. Вписать в первую строчку одину из величин выше и через пробел вписать конкретную величину.")
print("Пример: (Какую еденицу нудно сконвертировать?: 1 кг (конкретная величина во множественном числе) - enter")
print("2. Во второй строке нужно вписать само число, которое вы хотите сконвертировать.")
print("Пример: (Введите число: 56) - enter")
print("3. После этих шагов вы увидите результат, если вы хотите сконвертировать еще что-либо, тогда нажмите enter и снова следуйте 2-м первым шагам.")
print("4. Если же вы хотите закрыть конвертер, вы можете нажать на крестик, или же в 1 строке вместо обозначений напишите -конец-.")
print("")
print("1 - вес (мг, г, кг, ц, т)")
print("2 - данные (бит, ба, кб, мб, гб, тб, пб)")
print("3 - расстояние (мм, см, м, км, мегм)")
print("4 - время (мс, с, м, ч, сут, н, м, г)")
print("5 - температура (ц, ф)")
print("")
def ves_kilogramm():
    global chislo, a, b, c, d, f                                                        #a milligramm b gramm c kilogramm d centner f tonna
    a = chislo * 1000 * 1000
    b = chislo * 1000
    c = chislo
    d = chislo / 100
    f = chislo / 1000

def ves_otv():
    print(f"{a} Миллиграмм")
    print(f"{b} Грамм")
    print(f"{c} Килограмм")
    print(f"{d} Центнера")
    print(f"{f} Тонн")

def ves_milligramm():
    global chislo, a, b, c, d, f
    b = chislo / 1000
    c = chislo / 1000 / 1000
    d = chislo / 1000 / 1000 / 100
    f = chislo / 1000 / 1000 / 1000

def ves_gramm():
    global chislo, a, b, c, d, f
    a = chislo * 1000
    b = chislo
    c = chislo / 1000
    d = chislo / 1000 / 100
    f = chislo / 1000 / 1000

def ves_centner():
    global chislo, a, b, c, d, f
    a = chislo * 100 * 1000 * 1000
    b = chislo * 100 * 1000
    c = chislo * 100
    d = chislo
    f = chislo / 10

def ves_tonna():
    global chislo, a, b, c, d, f
    a = chislo * 1000 * 1000 * 1000
    b = chislo * 1000 * 1000
    c = chislo * 1000
    d = chislo * 10
    f = chislo


def dan_bit():
    global chislo, a, b, c, d, f, e, g                                                  #a bit b bite c kilobait d megabite f gigabite e terobite g petobite
    a = chislo
    b = chislo / 8
    c = chislo / 8 / 1024
    d = chislo / 8 / 1024 / 1024
    f = chislo / 8 / 1024 / 1024 / 1024
    g = chislo / 8 / 1024 / 1024 / 1024 / 1024
    e = chislo / 8 / 1024 / 1024 / 1024 / 1024 / 1024

def dan_otv():
    print(f"{a} Бит")
    print(f"{b} Байт")
    print(f"{c} Килобайт")
    print(f"{d} Мегабайт")
    print(f"{f} Гигабайт")
    print(f"{g} Теробайт")
    print(f"{e} Петобайт")

def dan_bait():
    global chislo, a, b, c, d, f, e, g
    a = chislo * 8
    b = chislo
    c = chislo / 1024
    d = chislo / 1024 / 1024
    f = chislo / 1024 / 1024 / 1024
    g = chislo / 1024 / 1024 / 1024 / 1024
    e = chislo / 1024 / 1024 / 1024 / 1024 / 1024

def dan_kilobaite():
    global chislo, a, b, c, d, f, e, g
    a = chislo * 8 * 1024
    b = chislo * 1024
    c = chislo
    d = chislo / 1024
    f = chislo / 1024 / 1024
    g = chislo / 1024 / 1024 / 1024
    e = chislo / 1024 / 1024 / 1024 / 1024

def dan_megabite():
    global chislo, a, b, c, d, f, e, g
    a = chislo * 8 * 1024 * 1024
    b = chislo * 1024 * 1024
    c = chislo * 1024
    d = chislo
    f = chislo / 1024
    g = chislo / 1024 / 1024
    e = chislo / 1024 / 1024 / 1024

def dan_gigabite():
    global chislo, a, b, c, d, f, e, g
    a = chislo * 8 * 1024 * 1024 * 1024
    b = chislo * 1024 * 1024 * 1024
    c = chislo * 1024 * 1024
    d = chislo * 1024
    f = chislo
    g = chislo / 1024
    e = chislo / 1024 / 1024

def dan_terabite():
    global chislo, a, b, c, d, f, e, g
    a = chislo * 8 * 1024 * 1024 * 1024 * 1024
    b = chislo * 1024 * 1024 * 1024 * 1024
    c = chislo * 1024 * 1024 * 1024
    d = chislo * 1024 * 1024
    f = chislo * 1024
    g = chislo
    e = chislo / 1024

def dan_petabite():
    global chislo, a, b, c, d, f, e, g
    a = chislo * 8 * 1024 * 1024 * 1024 * 1024 * 1024
    b = chislo * 1024 * 1024 * 1024 * 1024 * 1024
    c = chislo * 1024 * 1024 * 1024 * 1024
    d = chislo * 1024 * 1024 * 1024
    f = chislo * 1024 * 1024
    g = chislo * 1024
    e = chislo


def dist_milliimetr():
    global chislo, a, b, c, d, f, e                                                            #a millimetr b santimetr c detcimetr d metr f kilometr e megametr
    a = chislo
    b = chislo / 10
    c = chislo / 10 / 10
    d = chislo / 10 / 100
    f = chislo / 10 / 100 / 1000
    e = chislo / 10 / 100 / 1000 / 1000

def dist_otv():
    global chislo, a, b, c, d, f, e
    print(f"{a} Миллиметров")
    print(f"{b} Сантиметров")
    print(f"{c} Дециметров")
    print(f"{d} Метров")
    print(f"{f} Километров")
    print(f"{e} Мегаметров")

def dist_santimetr():
    global chislo, a, b, c, d, f, e
    a = chislo * 10
    b = chislo
    c = chislo / 10
    d = chislo / 100
    f = chislo / 100 / 1000
    e = chislo / 100 / 1000 / 1000

def dist_detcimetr():
    global chislo, a, b, c, d, f, e
    a = chislo * 10 * 10
    b = chislo * 10
    c = chislo
    d = chislo / 10
    f = chislo / 10 / 1000
    e = chislo / 10 / 1000 / 1000

def dist_metr():
    global chislo, a, b, c, d, f, e
    a = chislo * 100 * 10
    b = chislo * 100
    c = chislo * 10
    d = chislo
    f = chislo / 1000
    e = chislo / 1000 / 1000

def dist_kilometr():
    global chislo, a, b, c, d, f, e
    a = chislo * 1000 * 10 * 10 * 10
    b = chislo * 1000 * 10 * 10
    c = chislo * 1000 * 10
    d = chislo * 1000
    f = chislo
    e = chislo / 1000

def dist_megametr():
    global chislo, a, b, c, d, f, e
    a = chislo * 1000 * 1000 * 10 * 10 * 10
    b = chislo * 1000 * 1000 * 10 * 10
    c = chislo * 1000 * 1000 * 10
    d = chislo * 1000 * 1000
    f = chislo * 1000
    e = chislo


def vre_millisekunda():
    global chislo, a, b, c, d, f, e, g, h                                                                        #a millisekunda b sekunda c minuta d chas f sutka e nedelia g god
    a = chislo
    b = chislo / 1000
    c = chislo / 1000 / 60
    d = chislo / 1000 / 60 / 60
    f = chislo / 1000 / 60 / 60 / 24
    h = chislo / 1000 / 60 / 60 / 24 / 30
    e = chislo / 1000 / 60 / 60 / 24 / 7
    g = chislo / 1000 / 60 / 60 / 24 / 365

def vre_otv():
    global chislo, a, b, c, d, f, e, g, h
    print(f"{a} Миллисекунд")
    print(f"{b} Секунд")
    print(f"{c} Минут")
    print(f"{d} Часов")
    print(f"{f} Суток")
    print(f"{e} Недель")
    print(f"{h} Месяцев")
    print(f"{g} Лет")

def vre_sekunda():
    global chislo, a, b, c, d, f, e, g, h
    a = chislo * 1000
    b = chislo
    c = chislo / 60
    d = chislo / 60 / 60
    f = chislo / 60 / 60 / 24
    h = chislo / 60 / 60 / 24 / 30
    e = chislo / 60 / 60 / 24 / 7
    g = chislo / 60 / 60 / 24 / 365

def vre_minuta():
    global chislo, a, b, c, d, f, e, g, h
    a = chislo * 1000 * 60
    b = chislo * 60
    c = chislo
    d = chislo / 60
    f = chislo / 60 / 24
    h = chislo / 60 / 24 / 30
    e = chislo / 60 / 24 / 7
    g = chislo / 60 / 24 / 365

def vre_chas():
    global chislo, a, b, c, d, f, e, g, h
    a = chislo * 1000 * 60 * 60
    b = chislo * 60 * 60
    c = chislo * 60
    d = chislo
    f = chislo / 24
    e = chislo / 24 / 7
    h = chislo / 24 / 7 / 30
    g = chislo / 24 / 365

def vre_sutka():
    global chislo, a, b, c, d, f, e, g, h
    a = chislo * 1000 * 60 * 60 * 24
    b = chislo * 60 * 60 * 24
    c = chislo * 60 * 24
    d = chislo * 24
    f = chislo
    e = chislo / 7
    h = chislo / 30
    g = chislo / 365

def vre_nedelia():
    global chislo, a, b, c, d, f, e, g, h
    a = chislo * 1000 * 60 * 60 * 24 * 7
    b = chislo * 60 * 60 * 24 * 7
    c = chislo * 60 * 24 * 7
    d = chislo * 24 * 7
    f = chislo * 7
    e = chislo
    h = chislo / 5
    g = chislo / 52

def vre_mes():
    global chislo, a, b, c, d, f, e, g, h
    a = chislo * 30 * 24 * 60 * 60 * 1000
    b = chislo * 30 * 24 * 60 * 60
    c = chislo * 30 * 24 * 60
    d = chislo * 30 * 24
    f = chislo * 30
    e = chislo * 5
    h = chislo
    g = chislo / 12

def vre_god():
    global chislo, a, b, c, d, f, e, g, h
    a = chislo * 1000 * 60 * 60 * 24 * 365
    b = chislo * 60 * 60 * 24 * 365
    c = chislo * 60 * 24 * 365
    d = chislo * 365 * 24
    f = chislo * 365
    e = chislo * 52
    h = chislo * 12
    g = chislo


def tem_celsia():
    global chislo, a, b                                                         # a celsia b farengeit
    a = chislo
    b = (chislo * 9/5) +32

def tem_farengeit():
    global chislo, a, b
    a = 5/9 * (chislo - 32)
    b = chislo

def tem_otv():
    global chislo, a, b
    print(f"{a} C")
    print(f"{b} F")


while True:
    ip = str(input("Какую единицу нужно сконвертировать?: "))
    sis = ip.split()
    if sis[0] == "конец":
        break
    if len(sis) != 2:
        print("Введите корректные обозначения!")
        input()
    else:
        chislo = int(input("Введите число: "))
        print(" ")
        if sis[0] == '1' and sis[1] == "кг":
            ves_kilogramm()
            ves_otv()
        if sis[0] == '1' and sis[1] == "мг":
            ves_milligramm()
            ves_otv()
        if sis[0] == '1' and sis[1] == "г":
            ves_gramm()
            ves_otv()
        if sis[0] == '1' and sis[1] == "ц":
            ves_centner()
            ves_otv()
        if sis[0] == '1' and sis[1] == "т":
            ves_tonna()
            ves_otv()
        if sis[0] == '2' and sis[1] == "бит":
            dan_bit()
            dan_otv()
        if sis[0] == '2' and sis[1] == "байт":
            dan_bait()
            dan_otv()
        if sis[0] == '2' and sis[1] == "кб":
            dan_kilobaite()
            dan_otv()
        if sis[0] == '2' and sis[1] == "мб":
            dan_megabite()
            dan_otv()
        if sis[0] == '2' and sis[1] == "гб":
            dan_gigabite()
            dan_otv()
        if sis[0] == '2' and sis[1] == "тб":
            dan_terabite()
            dan_otv()
        if sis[0] == '2' and sis[1] == "пб":
            dan_petabite()
            dan_otv()
        if sis[0] == '3' and sis[1] == "мм":
            dist_milliimetr()
            dist_otv()
        if sis[0] == '3' and sis[1] == "см":
            dist_santimetr()
            dist_otv()
        if sis[0] == '3' and sis[1] == "дм":
            dist_detcimetr()
            dist_otv()
        if sis[0] == '3' and sis[1] == "м":
            dist_metr()
            dist_otv()
        if sis[0] == '3' and sis[1] == "км":
            dist_kilometr()
            dist_otv()
        if sis[0] == '3' and sis[1] == "мегм":
            dist_megametr()
            dist_otv()
        if sis[0] == '4' and sis[1] == "мс":
            vre_millisekunda()
            vre_otv()
        if sis[0] == '4' and sis[1] == "с":
            vre_sekunda()
            vre_otv()
        if sis[0] == '4' and sis[1] == "м":
            vre_minuta()
            vre_otv()
        if sis[0] == '4' and sis[1] == "ч":
            vre_chas()
            vre_otv()
        if sis[0] == '4' and sis[1] == "сут":
            vre_sutka()
            vre_otv()
        if sis[0] == '4' and sis[1] == "н":
            vre_nedelia()
            vre_otv()
        if sis[0] == '4' and sis[1] == "м":
            vre_mes()
            vre_otv()
        if sis[0] == '4' and sis[1] == "г":
            vre_god()
            vre_otv()
        if sis[0] == '5' and sis[1] == "ц":
            tem_celsia()
            tem_otv()
        if sis[0] == '5' and sis[1] == "ф":
            tem_farengeit()
            tem_otv()

        input()