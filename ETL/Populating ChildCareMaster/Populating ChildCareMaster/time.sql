DECLARE @currentDate DATE = '1959-02-10'
DECLARE @endDate DATE = '2023-11-01'

DECLARE @monthNo INT

WHILE @currentDate <= @endDate
BEGIN
    SET @monthNo = MONTH(@currentDate)

    INSERT INTO Data_WYMIAR (rok, miesiac, miesiac_no, dzien, dzien_tygodnia, polrocze, polrocze_no, pelna_data)
    VALUES (
        YEAR(@currentDate),
        FORMAT(@currentDate, 'MMMM', 'pl-PL'),
        @monthNo,
        DAY(@currentDate),
        DATENAME(WEEKDAY, @currentDate),
        CASE WHEN @monthNo BETWEEN 1 AND 6 THEN 'pierwsze' ELSE 'drugie' END,
        CASE WHEN @monthNo BETWEEN 1 AND 6 THEN 1 ELSE 2 END,
        @currentDate
    )

    SET @currentDate = DATEADD(DAY, 1, @currentDate)
END