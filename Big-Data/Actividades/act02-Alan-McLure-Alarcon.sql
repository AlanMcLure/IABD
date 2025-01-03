use jardineria;

-- 1. Devuelve un listado con la ciudad y el teléfono de las oficinas de España

select ciudad, telefono from oficina where pais = 'España';

-- 2. Devuelve un listado con los estados de los pedidos. Los estados no deben repetirse.

select distinct estado from pedido;
select estado from pedido group by estado;

-- 3. Devuelve un listado con el código de cliente de aquellos clientes que realizaron algún pago en 2008. 
-- Tenga en cuenta que deberá eliminar aquellos códigos de cliente que aparezcan repetidos.

select p.codigo_cliente from pago p where year(p.fecha_pago) = 2008 group by p.codigo_cliente;
select distinct p.codigo_cliente from pago p where year(p.fecha_pago) = 2008;

-- 4. Devuelve un listado con todos los clientes que sean de la ciudad de Madrid y cuyo representante de ventas 
-- tenga el código de empleado 11 o 30.

select * from cliente c where ciudad = 'Madrid' and c.codigo_empleado_rep_ventas in (11, 30);

-- 5. Devuelve el listado de clientes indicando el nombre del cliente y cuántos pedidos ha realizado. Tenga en cuenta 
-- que pueden existir clientes que no han realizado ningún pedido.

select c.nombre_cliente, count(p.codigo_pedido) as 'Número de pedidos' from cliente c 
left join pedido p on c.codigo_cliente = p.codigo_cliente group by c.codigo_cliente;

-- 6. Devuelve un listado con los nombres de los clientes y el total pagado por cada uno de ellos. Tenga en cuenta que 
-- pueden existir clientes que no han realizado ningún pago.

select c.nombre_cliente, sum(p.total) as 'Total pagado' from cliente c 
left join pago p on c.codigo_cliente = p.codigo_cliente group by c.nombre_cliente;

-- 7. Devuelve el nombre de los clientes que hayan hecho pedidos en 2008 ordenados alfabéticamente de menor a mayor.

select distinct c.nombre_cliente from cliente c 
join pedido p on c.codigo_cliente = p.codigo_cliente 
where year(p.fecha_pedido) = 2008 order by c.nombre_cliente asc;

-- 8. Devuelve el listado de clientes donde aparezca el nombre del cliente, el nombre y primer apellido de su representante 
-- de ventas y la ciudad donde está su oficina.

select c.nombre_cliente, e.nombre, e.apellido1, o.ciudad from cliente c 
join empleado e on c.codigo_empleado_rep_ventas = e.codigo_empleado 
join oficina o on e.codigo_oficina = o.codigo_oficina;

-- 9. Devuelve un listado indicando todas las ciudades donde hay oficinas y el número de empleados que tiene

select o.ciudad, count(e.codigo_empleado) as 'Número de empleados' from oficina o 
left join empleado e on o.codigo_oficina = e.codigo_oficina group by o.ciudad;