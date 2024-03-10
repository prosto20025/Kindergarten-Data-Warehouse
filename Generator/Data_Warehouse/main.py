from datetime import datetime

from scripts.find_day import *
from scripts.load_data import load_data, export_data
from scripts.new_objects import *
import random

# CONSTANCE'S
TUPLES = 1000  # ilość dzieci
CHILDREN_PER_YEAR = 200
CHILDREN_PER_GROUP = 10
END_DATE = datetime(2023, 11, 1)
NUMBER_OF_FAULTS = 100
FAULT_PER_YEAR = 2
MAX_OF_FAULTS = 3
MAX_TEACHER_AGE = 62
PRICE_PER_MINUTE = 1
MAX_AGE = 10

# TABLES
Wady = []
Dzieci = []
Wady_Dziecka = []
Logopedzi = []
Grupy = []
Dziecko_Grupa = []
Terapie = []
Dni_Terapii = []
Transakcje = []
Opiekunowie = []

# VARIABLES FOR TABLES
months = 1 + int(12 * TUPLES / CHILDREN_PER_YEAR)
start_date = END_DATE - relativedelta(months=months)
now = start_date
active_teachers = int(CHILDREN_PER_YEAR / CHILDREN_PER_GROUP) + 1
childern_per_month = int(CHILDREN_PER_YEAR / 12) + 1

# LOAD DATA
first_names = load_data('data/first-names.txt')
last_names = load_data('data/last-names.txt')
days = load_data('data/days.txt')
payment_method = load_data('data/payment.txt')
status = load_data('data/status.txt')
education = load_data('data/education.txt')
countries = load_data('data/country.txt')

# FAULTS
for i in range(1, NUMBER_OF_FAULTS):
    new_fault(Wady)

# TEACHERS
for i in range(active_teachers):
    Logopedzi.append(new_teacher(now, Logopedzi, first_names, last_names))

# TIMELINE
weeks = 0
while now < END_DATE:
    # OLD CHILDREN
    if now != start_date:
        treatment(now, Dziecko_Grupa, MAX_AGE, Wady_Dziecka)
        chech_and_close_groups(now, Grupy, Dziecko_Grupa)

    # HELP VALUES
    new_children = []
    new_groups = []
    children_per_group = 0
    group_value = 0

    # BEGINNING OF MOTH
    if weeks == 0:
        # TEACHER REMOVAL
        for teacher in Logopedzi:
            if get_age(now, teacher.data_urodzenia) >= MAX_TEACHER_AGE:
                teacher.aktywny = 0
        # NEW FAULTS
        if new_year(now.day, now.month, start_date):
            for i in range(FAULT_PER_YEAR):
                new_fault(Wady)

        # NEW CHILDREN
        for i in range(1, childern_per_month):
            # CHILD
            dziecko = new_child(now, Dzieci, first_names, last_names)
            Dzieci.append(dziecko)
            new_children.append(dziecko)

            # CAREGIVER
            Opiekunowie.append(new_caregiver(Opiekunowie, dziecko, first_names, countries, status, education, now))

            # FAULTS
            number_of_faults = random.randint(1, MAX_OF_FAULTS)
            child_faults = random.sample(Wady, number_of_faults)
            for fault in child_faults:
                Wady_Dziecka.append(WadaDziecka(fault, dziecko, 'Mam na te chorobe plan', 0, None))

        # NEW TEACHER
        now_active_teachers = sum(1 for logopeda in Logopedzi if logopeda.aktywny)
        if active_teachers < now_active_teachers:
            for i in range(active_teachers - now_active_teachers):
                Logopedzi.append(new_teacher(now, Logopedzi, first_names, last_names))

        # GROUPS
        for i in range(int(len(new_children) / CHILDREN_PER_GROUP) + 1):
            group = new_group(now, Grupy, Logopedzi)
            Grupy.append(group)
            new_groups.append(group)

        # NEW CHILDREN TO GROUP
        for child in new_children:
            if children_per_group >= CHILDREN_PER_GROUP:
                children_per_group = 0
                group_value += 1
            Dziecko_Grupa.append(PodzialGrup(new_groups[group_value], child, 1, now, None))
            children_per_group += 1

    # EVERY WEEK
    for grupa in Grupy:
        if grupa.grupa_aktwyna:
            # THERAPY
            number_of_days = random.randint(1, 7)
            Therapy = Terapia(len(Terapie) + 1, now, None, grupa, random.choice([30, 45, 60, 90]), number_of_days)
            Terapie.append(Therapy)

            # DAYS OF THERAPY
            therapy_days = random.sample(days, number_of_days)
            for day in therapy_days:
                Dni_Terapii.append(DniTerapii(len(Dni_Terapii) + 1, Therapy, day))

            # Transaction
            for uczen in Dziecko_Grupa:
                if uczen.id_grupa == grupa and uczen.aktywny:
                    Transakcje.append(Transakcja(
                        len(Transakcje) + 1, Therapy, uczen,
                        Therapy.czestotliwosc * Therapy.dlugosc_zajec * PRICE_PER_MINUTE,
                        'xx-' + str(len(Transakcje) + 1), random.choice(payment_method), now, random.randint(3, 10))
                    )

    now += relativedelta(days=7)
    weeks += 1
    if weeks == 4:
        weeks = 0
        if now.month == 12:
            now = datetime(now.year + 1, 1, 1)
        else:
            now = datetime(now.year, now.month + 1, 1)
    print('Pracuje')
    if now == datetime(2023,5,1):
        export_data(Wady, Dzieci, Wady_Dziecka, Logopedzi, Grupy, Dziecko_Grupa, Terapie, Dni_Terapii, Transakcje,
                Opiekunowie,
                'data/outputT1/')

export_data(Wady, Dzieci, Wady_Dziecka, Logopedzi, Grupy, Dziecko_Grupa, Terapie, Dni_Terapii, Transakcje, Opiekunowie,
            'data/outputT2/')
