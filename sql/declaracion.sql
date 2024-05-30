CREATE TABLE declaracion (
    id SERIAL PRIMARY KEY,
    id_usuario INTEGER NOT NULL,
    ingresos_laborales NUMERIC(10,2) NOT NULL,
    otros_ingresos_gravables NUMERIC(10,2) DEFAULT 0,
    otros_ingresos_no_gravables NUMERIC(10,2) DEFAULT 0,
    retenciones NUMERIC(10,2) NOT NULL,
    seguridad_social NUMERIC(10,2) NOT NULL,
    aportes_pension NUMERIC(10,2) NOT NULL,
    gastos_creditos_hipotecarios NUMERIC(10,2) NOT NULL,
    donaciones NUMERIC(10,2) DEFAULT 0,
    gastos_educacion NUMERIC(10,2) DEFAULT 0,
    total_ingresos_gravados NUMERIC(10,2) NOT NULL,
    total_ingresos_no_gravados NUMERIC(10,2) NOT NULL,
    total_costos_deducibles NUMERIC(10,2) NOT NULL,
    valor_impuesto NUMERIC(10,2) NOT NULL
);


