create database Tienda;
drop database Tienda;
use Tienda;
alter table Producto modify precio decimal(4,2);
drop table Producto;
create table Producto (
	idProducto int primary key check(idProducto > 0),
    nombreProducto varchar(50) not null check(nombreProducto regexp '^[a-zA-Z0-9\\s]+$'),
    nombreProveedor varchar(50) not null check(nombreProveedor regexp '^[a-zA-Z0-9\\s]+$'),
    precio decimal(5,2) not null check(precio > 0.0),
    cantidad int not null check(cantidad > -1),
    unidadDeMedida varchar(30) not null check(unidadDeMedida regexp '^[a-zA-Z\\s]+$')
);

drop table cliente;
create table cliente (
	idCliente int not null check(idCliente > 0),
    nombreCliente varchar(50) primary key check(nombreCliente regexp '^[a-zA-Z0-9\\s]+$'),
    numeroCliente varchar(10) not null check(numeroCliente regexp '^[0-9\\s]+$')
);

create table compra(
	idCompra int primary key check(idCompra > 0),
    nombreCliente varchar(50) not null check(nombreCliente regexp '^[a-zA-Z0-9\\s]+$'),
    fecha datetime not null,
    total decimal(4,2) not null check(total > 0),
    
    foreign key(nombreCliente) references cliente(nombreCliente)
);

create table compraDetallada (
	idCompraDetallada int primary key check(idCompraDetallada > 0),
    idCompra int not null check(idCompra > 0),
    idProducto int not null check(idProducto > 0),
    subtotal decimal(4,2) not null check(subtotal > 0),
    
    foreign key(idCompra) references compra(idCompra),
    foreign key(idProducto) references Producto(idProducto)
);


use Tienda;
select * from Producto;
delete from Producto where idProducto = 1;
insert into Producto values(5,"Churrumaiz", "Sabritas", 9, 20, "Empaquetado");