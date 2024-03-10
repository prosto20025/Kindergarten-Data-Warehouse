from random import random

from classes import *
from scripts.find_day import find_day_years
import random


def new_child(now, Dzieci, first_names, last_names):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    birth_day = find_day_years(now, 7, 3)
    dziecko = Dziecko(len(Dzieci) + 1, first_name, last_name, birth_day)
    return dziecko


def new_teacher(now, Logopedzi, first_names, last_names):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    birth_day = find_day_years(now, 60, 30)
    return Logopeda(len(Logopedzi) + 1, first_name, last_name, birth_day, 8888910,
                    first_name + '.' + last_name + '@psm.pl', 1)


def new_fault(Wady):
    time = random.randint(30, 120)
    wada = Wada(len(Wady) + 1, 'Wada_' + str(len(Wady) + 1), 'Krótki opis wady', time)
    Wady.append(wada)


def new_group(now, Grupy, Logopedzi):
    Logopeda = random.choice(Logopedzi)
    while not Logopeda.aktywny:
        Logopeda = random.choice(Logopedzi)
    return Grupa(len(Grupy) + 1, None, Logopeda, Logopeda.nazwisko + '_' + str(len(Grupy) + 1), 1, now, None)


def new_caregiver(Opiekunowie, child, first_names, countries, status, education, now):
    rand = random.randint(0, 100)
    if rand == 0:
        country = random.choice(countries)
    else:
        country = 'Poland'
    if rand > 50:
        plec = "M"
    elif rand < 50:
        plec = "K"
    else:
        plec = 'I'
    return Opiekun(len(Opiekunowie) + 1, child, random.choice(first_names), child.nazwisko, plec,
                   find_day_years(now, 70, 20), 'tu mieszkam', '88-100', random.choice(status), '8889', '@mail.com',
                   random.choice(education), country)
