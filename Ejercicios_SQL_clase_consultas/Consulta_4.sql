INSERT INTO usuarios (ID_USUARIO, USERNAME, CONTRASENA, ROL) VALUES 
('U001', 'carlos_admin', 'hash_password_segura_1', 'Administrador'),
('U002', 'maria_ventas', 'hash_password_segura_2', 'Vendedor');
INSERT INTO cliente (ID_CLIENTE, NOMBRE, APELLIDO, EMAIL, CITY) VALUES 
('C001', 'Ana María', 'Pérez Gómez', 'ana.perez@email.com', 'Madrid'),
('C002', 'Luis', 'Gómez', 'luis.gomez@email.com', 'Barcelona'),
('C003', 'Carlos', 'Villamizar', 'carlos.villa@email.com', NULL);
INSERT INTO ventas (ID_VENTAS, VALOR, FECHA, ID_CLIENTE, ID_USUARIO) VALUES 
('V001', 150.50, '2026-06-25', 'C001', 'U002'),
('V002', 4200.00, '2026-06-25', 'C002', 'U002'),
('V003', 85.25, '2026-06-25', 'C001', 'U001');