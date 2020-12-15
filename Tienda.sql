create database Tienda;

create table Recargas (
	id int primary key,
    fecha date,
    nombre varchar(50),
    numeroTelefono varchar(10),
    catidad float(0.0),
    pagado boolean
);