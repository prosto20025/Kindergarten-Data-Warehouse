CREATE TABLE Logopeda (
    id_logopeda INT PRIMARY KEY,
    imie NVARCHAR(30),
    nazwisko NVARCHAR(30),
	data_urodzenia DATE,
    telefon NVARCHAR(9),
    mail NVARCHAR(100),
	aktywny BIT,
);

CREATE TABLE Grupa (
    id_grupa INT PRIMARY KEY,
    dzien_zajec NVARCHAR(12),
    id_logopeda INT,
    numer_grupa INT,
    grupa_aktywna BIT,
    data_utworzenia DATE,
    data_zamkniecia DATE,
    FOREIGN KEY (id_logopeda) REFERENCES Logopeda(id_logopeda)
);

CREATE TABLE Terapia (
    id_terapia INT PRIMARY KEY,
    data_rozpoczecia DATE,
    id_grupa INT,
    dlugosc_zajec INT,
    czestotliwosc INT,
    FOREIGN KEY (id_grupa) REFERENCES Grupa(id_grupa)
);

CREATE TABLE Dziecko (
    id_dziecko INT PRIMARY KEY,
    imie NVARCHAR(30),
    nazwisko NVARCHAR(30),
    data_urodzenia DATE
);

CREATE TABLE Wada (
    id_wada INT PRIMARY KEY,
    nazwa NVARCHAR(30),
    opis NVARCHAR(300),
    sredni_czas_leczenia INT,
);

CREATE TABLE Wada_dziecka (
    id_wada INT,
    id_dziecko INT,
    opis_leczenia NVARCHAR(500),
    wyleczona BIT,
    data_wyleczenia DATE,
    PRIMARY KEY (id_wada, id_dziecko),
    FOREIGN KEY (id_wada) REFERENCES Wada(id_wada),
    FOREIGN KEY (id_dziecko) REFERENCES Dziecko(id_dziecko)
);

CREATE TABLE Transakcja (
    id_transakcja INT PRIMARY KEY,
    id_terapia INT,
    id_dziecko INT,
    kwota DECIMAL(10,2),
    numer_transakcji NVARCHAR(100),
    sposob_platnosci NVARCHAR(20),
    ocena_terapii INT,
    FOREIGN KEY (id_terapia) REFERENCES Terapia(id_terapia),
    FOREIGN KEY (id_dziecko) REFERENCES Dziecko(id_dziecko)
);

CREATE TABLE Podzial_grup (
    id_grupa INT,
    id_dziecko INT,
    aktywny BIT,
    data_dolaczenia DATE,
    data_odejscia DATE,
    PRIMARY KEY (id_grupa, id_dziecko),
    FOREIGN KEY (id_grupa) REFERENCES Grupa(id_grupa),
    FOREIGN KEY (id_dziecko) REFERENCES Dziecko(id_dziecko)
);

CREATE TABLE Dni_terapii (
    id_dni_terapii INT PRIMARY KEY,
    id_terapia INT,
	dzien_zajec NVARCHAR(12),
	FOREIGN KEY (id_terapia) REFERENCES Terapia(id_terapia)
);