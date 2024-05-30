CREATE TABLE tabla_ingresos (
    id_usuario INT PRIMARY KEY,
    total_ingresos_gravados DECIMAL(10,2),
    total_ingresos_no_gravados DECIMAL(10,2),
    total_costos_deducibles DECIMAL(10,2),
    valor_impuesto DECIMAL(10,2)
);
