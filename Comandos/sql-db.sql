sqlite>

CREATE TABLE sucursales(idSucursal INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, userSucursal VARCHAR(255) NOT NULL, nombreSucursal VARCHAR(255) NOT NULL, direccionSucursal VARCHAR(255) NOT NULL, telefonoSucursal INT NOT NULL, activoSucursal BOOLEAN NOT NULL, contrasenaSucursal VARCHAR(255) NOT NULL);
INSERT INTO sucursales(nombreSucursal, userSucursal, direccionSucursal, telefonoSucursal, activoSucursal, contrasenaSucursal) VALUES('El Tio Santa Ana', 'tioSantaAna','Av. fray felipe',24737355, 1, 'admin');
INSERT INTO sucursales(nombreSucursal, userSucursal, direccionSucursal, telefonoSucursal, activoSucursal, contrasenaSucursal) VALUES('El Tio San Salvador', 'tioSanSalvador', 'Av. Alcaldia',24737356, 1,'admin');
INSERT INTO sucursales(nombreSucursal, userSucursal, direccionSucursal, telefonoSucursal, activoSucursal, contrasenaSucursal) VALUES('El Tio Metapan', 'tioMetapan', 'Metapan',24760355, 1,'admin');



CREATE TABLE miembros(idMiembro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, idSucursal INTEGER NOT NULL, nombreMiembro VARCHAR(255) NOT NULL, apellidoMiembro VARCHAR(255) NOT NULL, telefonoMiembro INT NOT NULL, activoMiembro BOOLEAN NOT NULL, FOREIGN KEY(idSucursal) REFERENCES sucursales(idSucursal));
INSERT INTO miembros(idSucursal, nombreMiembro, apellidoMiembro, telefonoMiembro, activoMiembro) VALUES(1,'Juan Carlos','Pleitez Cortez', 76876868, 1);
INSERT INTO miembros(idSucursal, nombreMiembro, apellidoMiembro, telefonoMiembro, activoMiembro) VALUES(1,'Diana Melissa','Magaña Batres',61117759, 1);
INSERT INTO miembros(idSucursal, nombreMiembro, apellidoMiembro, telefonoMiembro, activoMiembro) VALUES(2,'Luis Enrique','Dorrat Herrera',10000000, 1);
INSERT INTO miembros(idSucursal, nombreMiembro, apellidoMiembro, telefonoMiembro, activoMiembro) VALUES(2,'Andrea Alejandra','Cuellar Chavez',10000000, 0);


CREATE TABLE empleados(idEmpleado INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, idSucursal INTEGER NOT NULL, nombreEmpleado VARCHAR(255) NOT NULL, apellidoEmpleado VARCHAR(255) NOT NULL, telefonoEmpleado INT NOT NULL, activoEmpleado BOOLEAN NOT NULL, FOREIGN KEY(idSucursal) REFERENCES sucursales(idSucursal));
INSERT INTO empleados(idSucursal, nombreEmpleado, apellidoEmpleado, telefonoEmpleado, activoEmpleado) VALUES(1,'Kevin','Rojas', 11112222, 1);
INSERT INTO empleados(idSucursal, nombreEmpleado, apellidoEmpleado, telefonoEmpleado, activoEmpleado) VALUES(1,'Merling','Pleitez',79648341, 1);
INSERT INTO empleados(idSucursal, nombreEmpleado, apellidoEmpleado, telefonoEmpleado, activoEmpleado) VALUES(2,'Jose','Pleitez',33334444, 1);


CREATE TABLE tipoPago(idTipoPago INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, precioTipoPago DECIMAL(10,2) NOT NULL, nombreTipoPago VARCHAR(255) NOT NULL,descripcionTipoPago VARCHAR(255) NOT NULL);
INSERT INTO tipoPago(precioTipoPago, nombreTipoPago, descripcionTipoPago) VALUES(10.00,'Matricula','La matricula del año');
INSERT INTO tipoPago(precioTipoPago, nombreTipoPago, descripcionTipoPago) VALUES(19.99,'Mensual','Pagos mensuales');




CREATE TABLE pagos(idPago INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, idTipoPago INTEGER NOT NULL, idMiembro INTEGER NOT NULL, idEmpleado INTEGER NOT NULL, idSucursal INTEGER NOT NULL, datePago TEXT NOT NULL, FOREIGN KEY(idTipoPago) REFERENCES tipoPago(idTipoPago), FOREIGN KEY(idMiembro) REFERENCES miembros(idMiembro), FOREIGN KEY(idEmpleado) REFERENCES empleados(idMiembro), FOREIGN KEY(idSucursal) REFERENCES sucursales(idSucursal));
INSERT INTO pagos(idTipoPago, idMiembro, idEmpleado, idSucursal, datePago) VALUES(1,1,1,1,'2017-01-01T06:43:00');
INSERT INTO pagos(idTipoPago, idMiembro, idEmpleado, idSucursal, datePago) VALUES(2,1,2,1,'2017-05-07T07:53:00');
INSERT INTO pagos(idTipoPago, idMiembro, idEmpleado, idSucursal, datePago) VALUES(1,2,3,1,'2017-01-17T04:20:01');
INSERT INTO pagos(idTipoPago, idMiembro, idEmpleado, idSucursal, datePago) VALUES(2,2,1,1,'2017-11-26T09:03:02');
