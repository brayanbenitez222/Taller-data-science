SELECT 
    cliente.ID AS Cod_Cliente,
    cliente.NOMBRE,
    cliente.APELLIDO,
    ventas.ID_VENTAS AS Num_Factura,
    ventas.VALOR,
    ventas.FECHA
FROM ventas INNER JOIN cliente ON ventas.ID_CLIENTE = cliente.ID;