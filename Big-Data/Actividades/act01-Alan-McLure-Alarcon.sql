use actividad1_bd;

-- 1. Selecciona el nombre de todas las piezas (Pieces).

select Name from pieces;

-- 2. Selecciona todos los datos de los proveedores (Providers)

select * from providers;

-- 3. Obtén el precio medio de cada pieza (Muestra solo el código de la pieza y el precio medio)

select pi.Code, avg(pr.Price) as 'Precio medio' from pieces pi join provides pr on pi.Code = pr.Piece group by pi.Code;

-- 4. Obtén los nombres de todos los proveedores que suministran la pieza 1.

select prs.Name from providers prs join provides pr on prs.Code = pr.Provider where pr.Piece = 1;
select pr.Name from providers pr where pr.Code in (select Provider from provides where Piece = 1);

-- 5. Selecciona el nombre de las piezas suministradas por el proveedor con código "HAL".

select pi.Name from pieces pi join provides pr on pi.Code = pr.Piece where pr.Provider = 'HAL';

-- 6. Para cada pieza, busque la oferta más cara de esa pieza e incluye el nombre de la pieza, el nombre del proveedor y 
-- el precio (ten en cuenta que podría haber dos proveedores que suministren la misma pieza al precio más caro).

select pi.Name as 'Pieza' , prs.Name as 'Proveedor', pr.Price from pieces pi 
join provides pr on pi.Code = pr.Piece 
join providers prs on pr.Provider = prs.Code 
where pr.price in (select max(price) from provides as subpr where subpr.Piece = pr.piece);

-- 7. Agregua una entrada a la base de datos para indicar que "Skellington Supplies"
-- (código "TNBC") proporcionará piñones (código "1") por 7 centavos cada uno.

insert into provides (Piece, Provider, Price)
values (1, 'TNBC', 7);

-- 8. Aumenta todos los precios en un centavo.

-- desactivar safe update mode
set SQL_SAFE_UPDATES = 0;

update provides set Price = Price + 1;

-- activar safe update mode
set SQL_SAFE_UPDATES = 1;

-- 9. Actualizae la base de datos para reflejar que "Susan Calvin Corp." (código "RBT")
-- no suministrará pernos (código 4).

delete from provides where Provider = 'RBT' and Piece = 4;

-- 10.Actualiza la base de datos para reflejar que "Susan Calvin Corp." (código "RBT") no
-- proporcionará ninguna pieza (el proveedor aún debe permanecer en la base de datos).

delete from provides where Provider = 'RBT';

select * from provides;
select * from providers;