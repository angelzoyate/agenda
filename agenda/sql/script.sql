CREATE TABLE contactos(
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
);

INSERT INTO contactos(nombre,primer_apellido,segundo_apellido,email,telefono)
VALUES
('Roberto','Vazquez','Alvarado','robert@email.com','7711412468'),
('Jacob','Gonzales','Curiel','jacob@email.com','7751876929');


SELECT * FROM contactos;