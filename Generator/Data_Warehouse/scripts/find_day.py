from datetime import date, timedelta
import random

from dateutil.relativedelta import relativedelta


def find_day_years(now, left, right):
    left_date = now - relativedelta(years=left)
    right_date = now - relativedelta(years=right)
    diff = right_date - left_date
    random_days = random.randint(0, diff.days)
    day = left_date + timedelta(days=random_days)
    return day


def find_day_months(now, left, right):
    left_date = now - relativedelta(days=left)
    right_date = now - relativedelta(days=right)
    diff = right_date - left_date
    random_days = random.randint(0, diff.days)
    day = left_date + timedelta(days=random_days)
    return day


def new_year(day, month, start_date):
    if day == start_date.day and month == start_date.month:
        return 1
    else:
        return 0


def get_age(now, birthday):
    age = now.year - birthday.year
    if (now.month, now.day) < (birthday.month, birthday.day):
        age -= 1
    return age


def get_days(now, then):
    diff = now - then
    return diff.days


def get_treatment_result(now, child, fault):
    time_of_tretement = get_days(now, child.data_dolaczenia)
    avg_time_od_treatment = fault.id_wada.sredni_czas_leczenia
    if time_of_tretement > 2 * avg_time_od_treatment:
        fault.data_wyleczenia = now
        fault.wyleczona = 1
    elif time_of_tretement >= avg_time_od_treatment:
        rand = random.randint(1, 10)
        if rand > 1:
            fault.data_wyleczenia = now
            fault.wyleczona = 1
    elif time_of_tretement >= 0.75 * avg_time_od_treatment:
        rand = random.randint(1, 10)
        if rand > 3:
            fault.data_wyleczenia = now
            fault.wyleczona = 1
    elif time_of_tretement >= 0.5 * avg_time_od_treatment:
        rand = random.randint(1, 10)
        if rand > 6:
            fault.data_wyleczenia = now
            fault.wyleczona = 1
    return fault.wyleczona

def treatment(now, Dziecko_Grupa, MAX_AGE, Wady_Dziecka):
    for child in Dziecko_Grupa:
        number_of_child_faults = 0
        heald_now_or_before = 0
        if get_age(now, child.id_dziecko.data_urodzenia) >= MAX_AGE:
            child.aktywny = 0
            child.data_odjescia = now
        else:
            for fault in Wady_Dziecka:
                if fault.id_dziecko == child.id_dziecko:
                    number_of_child_faults += 1
                    if not fault.wyleczona:
                        if get_treatment_result(now, child, fault):
                            heald_now_or_before += 1
                    else:
                        heald_now_or_before += 1
            if number_of_child_faults == heald_now_or_before:
                child.aktywny = 0
                child.data_odjescia = now

def chech_and_close_groups(now, Grupy, Dziecko_Grupa):
    for group in Grupy:
        number_of_chilren = 0
        number_of_heald_children = 0
        if group.grupa_aktwyna:
            for child_to_group in Dziecko_Grupa:
                if child_to_group.id_grupa == group:
                    number_of_chilren += 1
                    if child_to_group.aktywny == 0:
                        number_of_heald_children += 1
        if number_of_heald_children == number_of_chilren:
            group.grupa_aktwyna = 0
            group.data_zamkniecia = now
