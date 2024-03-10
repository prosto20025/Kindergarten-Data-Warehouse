BULK INSERT Logopeda
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Logopeda.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);


BULK INSERT Grupa
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Grupa.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Terapia
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Terapia.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Dziecko
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Dziecko.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Wada
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Wada.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Wada_dziecka
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Wada_dziecka.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Transakcja
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Transakcja.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Podzial_grup
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Podzial_grupy.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);

BULK INSERT Dni_terapii
FROM 'C:\Users\filip\Desktop\DW_Generator\Data_Warehouse\data\outputT2\Dni_terapii.csv'
WITH (
	FIELDTERMINATOR = ',',
	ROWTERMINATOR = '\n',
	FIRSTROW = 2
);



