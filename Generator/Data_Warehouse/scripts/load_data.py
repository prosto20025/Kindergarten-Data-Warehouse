import csv
def load_data(filename):
    with open(filename, "r") as plik:
        data = plik.readlines()
    data = [linia.strip() for linia in data]
    return data

def export_data(Wady, Dzieci, Wady_Dziecka, Logopedzi, Grupy, Dziecko_Grupa, Terapie, Dni_Terapii, Transakcje, Opiekunowie, path):
    with open(path+'Wada_dziecka.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_wada", "id_dziecko", "opis_leczenia", 'wyleczona', 'data_wyleczenia'])
        for wada in Wady_Dziecka:
            writer.writerow([wada.id_wada.id_wada,wada.id_dziecko.id_dziecko, wada.opis_leczenia, wada.wyleczona, wada.data_wyleczenia])
    with open(path+'Wada.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_wada", "nazwa", "opis", 'sredni_czas_leczenia'])
        for wada in Wady:
            writer.writerow([wada.id_wada, wada.nazwa, wada.opis, wada.sredni_czas_leczenia])
    with open(path+'Dziecko.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_dziecko", "imie", "nazwisko", 'data_urodzenia'])
        for dziecko in Dzieci:
            writer.writerow([dziecko.id_dziecko,dziecko.imie,dziecko.nazwisko, dziecko.data_urodzenia])
    with open(path+'Podzial_grupy.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_grupa", "id_dziecko", "aktywny", 'data_dolaczenia', 'data_odejscia'])
        for grupa in Dziecko_Grupa:
            writer.writerow([grupa.id_grupa.id_grupa,grupa.id_dziecko.id_dziecko, grupa.aktywny, grupa.data_dolaczenia, grupa.data_odjescia])
    with open(path+'Grupa.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_grupa", "id_logopeda", "numer_grupa", 'grupa_aktywna', 'data_utworzenia','data_zamkniecia'])
        for grupa in Grupy:
            writer.writerow([grupa.id_grupa,grupa.id_logopeda.id_logopeda, grupa.numer_grupa, grupa.grupa_aktwyna, grupa.data_utworzenia, grupa.data_zamkniecia])
    with open(path+'Logopeda.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_logopeda", "imie", "nazwisko", 'data_urodzenia', 'telefon', 'mail', 'aktywny'])
        for logopeda in Logopedzi:
            writer.writerow([logopeda.id_logopeda, logopeda.imie, logopeda.nazwisko, logopeda.data_urodzenia, logopeda.telefon, logopeda.mail, logopeda.aktywny])
    with open(path+'Transakcja.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_transakcja", "id_terapia", "id_dziecko", 'kwota', 'numer_transakcji', 'sposob_platnosci', 'ocena_terapii'])
        for transakcja in Transakcje:
            writer.writerow([transakcja.id_transakcja, transakcja.id_terapia.id_terapia, transakcja.id_dziecko.id_dziecko.id_dziecko, transakcja.kwota, transakcja.numer_transakcji, transakcja.sposob_platnosci, transakcja.ocena_terapii])
    with open(path + 'Terapia.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["id_terapia", "data_rozpoczecia", "id_grupa", 'dlugosc_zajec', 'czestotliwosc'])
        for terapia in Terapie:
            writer.writerow([terapia.id_terapia, terapia.data_rozpoczecia, terapia.id_grupa.id_grupa, terapia.dlugosc_zajec, terapia.czestotliwosc])
    with open(path + 'Dni_terapii.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["id_dni_terapii", "id_terapia", "dzien_zajec"])
        for dzien in Dni_Terapii:
            writer.writerow([dzien.id_dni_terapii, dzien.id_terapia.id_terapia, dzien.dzien_zajec])

    with open(path + 'Opiekun.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ['id_opiekuna', 'id_dziecko', 'Imie', 'Nazwisko', 'Plec', 'data_urodzenia', 'adres', 'kod pocztowy', 'status zamieszkania', 'numer telefonu', 'mail', 'wyksztalcenie', 'kraj pochodzenia'])
        for opiekun in Opiekunowie:
            writer.writerow(
                [opiekun.id_opiekuna, opiekun.id_dziecko.id_dziecko, opiekun.imie, opiekun.nazwisko, opiekun.plec, opiekun.data_urodzenia, opiekun.adres, opiekun.kod_pocztowy, opiekun.status_zamieszkania, opiekun.numer_telefonu, opiekun.adres_mail, opiekun.wyksztalcenie, opiekun.kraj_pochodzenia])



