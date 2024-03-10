# Kindergarten-Data-Warehouse
A data warehouse for a kindergarten that conducts sessions with a speech therapist.

Data warehouse for a kindergarten that conducts sessions with a speech threapist. Business goals of the kindergarten is to provide increase number of registered for sessions with a speecht therapist children by 1% to the previous half-year, and a 3% decrease in the number of children interested in continuing speech therapy sessions over a half-year.

## Project contains:
[Data Warehouse]() and [Source Database]() design and implementation
[MDX queries]()
[KPI queries]()
[BI Dashboards]() to represent the data.
[ETL process]() using Visual Studio tools
[Data generators]() in Python
[Visual Studio project]() Cube with hierarchies
[Project Documentation]() and DW [optimization report]()

## Screenshots

## Data warehouse design
Data Warehouse consists of four fact tables, namely Terapia_FAKT, Sukces_terapii, Zajecia_FAKT, Podzial_grup_FAKT. The Terapia_FAKT contains numerical data for each group therapy frequency. Podzial_grup_FAKT contains numerical data for each child amount of defects and estimated treatment time. The Sukces_terapii contains numerical values representing parent's age for each child. The Zajecia_FAKT contains length of each lesson with therapist. With all this data, we have been able to perform aggregation functions such as calculating the average parent's age, average lesson length, average therapy frequency, average amount of defects and more.
![Screenshot 1](/screens/DataWarehouseScreen.png)

## Database design
![Screenshot 2](/screens/DatabaseScreen.png)

## PowerBI dashboards
![Screenshot 3](/screens/firstDashboard)
![Screenshot 4](/screens/secondDashboard)
![Screenshot 5](/screens/thirdDashboard)
![Screenshot 6](/screens/fourthDashboard)
