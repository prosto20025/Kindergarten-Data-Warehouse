class Grupa:
    def __init__(self, id_grupa, dzien_zajec, id_logopeda, numer_grupa, grupa_aktwyna, data_utworzenia,
                 data_zamkniecia):
        self.id_grupa = id_grupa
        self.dzien_zajec = dzien_zajec
        self.id_logopeda = id_logopeda
        self.numer_grupa = numer_grupa
        self.grupa_aktwyna = grupa_aktwyna
        self.data_utworzenia = data_utworzenia
        self.data_zamkniecia = data_zamkniecia


class Terapia:
    def __init__(self, id_terapia, data_rozpoczecia, data_zakonczenia, id_grupa, dlugosc_zajec, czestotliwosc):
        self.id_terapia = id_terapia
        self.data_rozpoczecia = data_rozpoczecia
        self.data_zakonczenia = data_zakonczenia
        self.id_grupa = id_grupa
        self.dlugosc_zajec = dlugosc_zajec
        self.czestotliwosc = czestotliwosc


class DniTerapii:
    def __init__(self, id_dni_terapii, id_terapia, dzien_zajec):
        self.id_dni_terapii = id_dni_terapii
        self.id_terapia = id_terapia
        self.dzien_zajec = dzien_zajec


class Transakcja:
    def __init__(self, id_transakcja, id_terapia, id_dziecko, kwota, numer_transakcji, sposob_platnosci,
                 data_zaksiegowania, ocena_terapii):
        self.id_transakcja = id_transakcja
        self.id_terapia = id_terapia
        self.id_dziecko = id_dziecko
        self.kwota = kwota
        self.numer_transakcji = numer_transakcji
        self.sposob_platnosci = sposob_platnosci
        self.data_zaksiegowania = data_zaksiegowania
        self.ocena_terapii = ocena_terapii


class Logopeda:
    def __init__(self, id_logopeda, imie, nazwisko, data_urodzenia, telefon, mail, aktywny):
        self.id_logopeda = id_logopeda
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia
        self.telefon = telefon
        self.mail = mail
        self.aktywny = aktywny


class Dziecko:
    def __init__(self, id_dziecko, imie, nazwisko, data_urodzenia):
        self.id_dziecko = id_dziecko
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia


class Wada:
    def __init__(self, id_wada, nazwa, opis, sredni_czas_leczenia):
        self.id_wada = id_wada
        self.nazwa = nazwa
        self.opis = opis
        self.sredni_czas_leczenia = sredni_czas_leczenia


class WadaDziecka:
    def __init__(self, id_wada, id_dziecko, opis_leczenia, wyleczona, data_wyleczenia):
        self.id_wada = id_wada
        self.id_dziecko = id_dziecko
        self.opis_leczenia = opis_leczenia
        self.wyleczona = wyleczona
        self.data_wyleczenia = data_wyleczenia


class PodzialGrup:
    def __init__(self, id_grupa, id_dziecko, aktywny, data_dolaczenia, data_odjescia):
        self.id_grupa = id_grupa
        self.id_dziecko = id_dziecko
        self.aktywny = aktywny
        self.data_dolaczenia = data_dolaczenia
        self.data_odjescia = data_odjescia

class Opiekun:
    def __init__(self, id_opiekuna, id_dziecko, imie, nazwisko, plec, data_urodzenia, adres, kod_pocztowy, status_zamieszkania, numer_telefonu, adres_mail, wyksztalcenie, kraj_pochodzenia):
        self.id_opiekuna = id_opiekuna
        self.id_dziecko = id_dziecko
        self.imie = imie
        self.nazwisko = nazwisko
        self.plec = plec
        self.data_urodzenia = data_urodzenia
        self.adres = adres
        self.kod_pocztowy = kod_pocztowy
        self.status_zamieszkania = status_zamieszkania
        self.numer_telefonu = numer_telefonu
        self.adres_mail = adres_mail
        self.wyksztalcenie = wyksztalcenie
        self.kraj_pochodzenia = kraj_pochodzenia
