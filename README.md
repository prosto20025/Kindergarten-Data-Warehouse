# Kindergarten-Data-Warehouse
A data warehouse for a kindergarten that conducts sessions with a speech therapist.

Data warehouse for a kindergarten that conducts sessions with a speech threapist. Business goals of the kindergarten is to provide increase number of registered for sessions with a speecht therapist children by 1% to the previous half-year, and a 3% decrease in the number of children interested in continuing speech therapy sessions over a half-year.

## Project contains:
 - [Data Warehouse](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/Generator) and [Source Database](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/RelationalDatabase) design and implementation
 - [MDX queries](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/MDX%20Queries)
 - [KPI queries](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/MDX%20Queries)
 - [BI Dashboards](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/PowerBI/BI%20Dashboard) to represent the data.
 - [ETL process](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/ETL/Populating%20ChildCareMaster/Populating%20ChildCareMaster) using Visual Studio tools
 - [Data generators]([https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/Generator](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/Generator/Data_Warehouse) in Python
 - [Visual Studio project](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/Cube/ChildCareMaster/ChildCareMaster) Cube with hierarchies
 - [Project Documentation](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/Project%20Report) and DW [optimization report](https://github.com/prosto20025/Kindergarten-Data-Warehouse/tree/main/Project%20Report)

## Screenshots

## Data warehouse design
Data Warehouse consists of four fact tables, namely Terapia_FAKT, Sukces_terapii, Zajecia_FAKT, Podzial_grup_FAKT. The Terapia_FAKT contains numerical data for each group therapy frequency. Podzial_grup_FAKT contains numerical data for each child amount of defects and estimated treatment time. The Sukces_terapii contains numerical values representing parent's age for each child. The Zajecia_FAKT contains length of each lesson with therapist. With all this data, we have been able to perform aggregation functions such as calculating the average parent's age, average lesson length, average therapy frequency, average amount of defects and more.
![Screenshot 1](/screens/DataWarehouseScreen.png)

## Database design
![Screenshot 2](/screens/DatabaseScreen.png)

## PowerBI dashboards
![Screenshot 3](/screens/firstDashboard.png)
![Screenshot 4](/screens/secondDashboard.png)
![Screenshot 5](/screens/thirdDashboard.png)
![Screenshot 6](/screens/fourthDashboard.png)
