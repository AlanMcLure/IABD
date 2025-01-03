Calculo del Trimestre
------------------------
SELECT 
    Id_Actividad,
    Actividad AS Descripcion,
    CASE 
        WHEN CAST(SUBSTRING(Fecha_Fin FROM 4 FOR 2) AS INTEGER) IN (1, 2, 3) THEN 1
        WHEN CAST(SUBSTRING(Fecha_Fin FROM 4 FOR 2) AS INTEGER) IN (4, 5, 6) THEN 2
        WHEN CAST(SUBSTRING(Fecha_Fin FROM 4 FOR 2) AS INTEGER) IN (7, 8, 9) THEN 3
        WHEN CAST(SUBSTRING(Fecha_Fin FROM 4 FOR 2) AS INTEGER) IN (10, 11, 12) THEN 4
    END AS Trimestre,
    Fecha_Fin,
    Peso
FROM FLOWFILE

Separación de apellidos
----------------------
SELECT 
    Id_Usuario, 
    Nombre, 
    CASE 
        WHEN POSITION(' ' IN Apellidos) > 0 
        THEN TRIM(SUBSTRING(Apellidos, 1, POSITION(' ' IN Apellidos) - 1))
        ELSE Apellidos 
    END AS Apellido1,
    CASE 
        WHEN POSITION(' ' IN Apellidos) > 0 
        THEN TRIM(SUBSTRING(Apellidos, POSITION(' ' IN Apellidos) + 1))
        ELSE '' 
    END AS Apellido2,
    Grupo, 
    Email
FROM FLOWFILE