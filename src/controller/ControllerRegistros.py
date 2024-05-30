import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import psycopg2
import SecretConfig

import sys
sys.path.append("src")

from model.TaxLogic import TaxInformation

import psycopg2

class ErrorNotFound( Exception ):
    """ Excepcion que indica que una fila buscada no fue encontrada"""
    pass

def GetCursor():
    """Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones."""

    DATABASE = SecretConfig.PGDATABASE
    USER = SecretConfig.PGUSER
    PASSWORD = SecretConfig.PGPASSWORD
    HOST = SecretConfig.PGHOST
    PORT = SecretConfig.PGPORT

    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)

    return connection.cursor()

def CreateTable():
    """Crea la tabla registros, en caso de que no exista."""

    Sql_CreateTable = f"""CREATE TABLE registros (
            id INT NOT NULL, 
            total_labor_income_per_year INT, 
            other_taxable_income_per_year INT, 
            other_non_taxable_income_per_year INT, 
            source_retention_value_per_year INT, 
            mortgage_loan_payment_per_year INT, 
            donation_value_per_year INT, 
            educational_expenses_per_year INT, 
            CONSTRAINT id_pk PRIMARY KEY (id)
        );"""

    cursor = GetCursor()

    try:
        cursor.execute( Sql_CreateTable )
        cursor.connection.commit()
    except:
        cursor.connection.rollback()

def InsertRecord( record: TaxInformation ):
    """Guardar un registro en la base de datos"""

    Sql_InsertRecord = f"""INSERT INTO registros (
            id,
            total_labor_income_per_year,
            other_taxable_income_per_year,
            other_non_taxable_income_per_year,
            source_retention_value_per_year,
            mortgage_loan_payment_per_year,
            donation_value_per_year,
            educational_expenses_per_year
        )
        VALUES
        (
            {record.id},
            {record.total_labor_income_per_year},
            {record.other_taxable_income_per_year},
            {record.other_non_taxable_income_per_year},
            {record.source_retention_value_per_year},
            {record.mortgage_loan_payment_per_year},
            {record.donation_value_per_year},
            {record.educational_expenses_per_year}
        )"""

    try:
        cursor = GetCursor()
        cursor.execute( Sql_InsertRecord )
        cursor.connection.commit()
    except:
        cursor.connection.rollback() 
        raise Exception("No fue posible insertar el registro: " + str(record.id))

def DeleteRecord( id: int ):
    """Elimina la fila que contiene un registro en la BD"""

    Sql_DeleteRecord = f"""DELETE FROM registros WHERE id = {id}"""

    try:
        cursor = GetCursor()
        cursor.execute( Sql_DeleteRecord )
        cursor.connection.commit()
    except:
        cursor.connection.rollback() 
        raise Exception("No fue posible eliminar el registro: " + str(id))

def SearchRecordByID( id: int ):    
    """Busca un registro por el numero de Cedula"""

    Sql_SearchRecordById = f"""SELECT 
            id,
            total_labor_income_per_year,
            other_taxable_income_per_year,
            other_non_taxable_income_per_year,
            source_retention_value_per_year,
            mortgage_loan_payment_per_year,
            donation_value_per_year,
            educational_expenses_per_year
        FROM
            registros
        WHERE
            id = {id}"""

    # Todas las instrucciones se ejecutan a tavés de un cursor
    cursor = GetCursor()
    cursor.execute( Sql_SearchRecordById )
    fila = cursor.fetchone()

    if fila is None:
        raise ErrorNotFound("El registro buscado, no fue encontrado. Cedula=" + str(id))

    result = TaxInformation(id=fila[0], 
                               total_labor_income_per_year=fila[1], 
                               other_taxable_income_per_year=fila[2], 
                               other_non_taxable_income_per_year=fila[3], 
                               source_retention_value_per_year=fila[4],
                               mortgage_loan_payment_per_year=fila[5],
                               donation_value_per_year=fila[6],
                               educational_expenses_per_year=fila[7]
                               )
    
    return result

def UpdateRecord( record: TaxInformation ):
    """Actualiza los valores de un registro en la base de datos; 
    El atributo cedula nunca se debe cambiar, porque es la clave primaria"""

    Sql_UpdateRecord = f"""UPDATE 
            registros
        SET
            total_labor_income_per_year = {record.total_labor_income_per_year},
            other_taxable_income_per_year = {record.other_taxable_income_per_year},
            other_non_taxable_income_per_year = {record.other_non_taxable_income_per_year},
            source_retention_value_per_year = {record.source_retention_value_per_year},
            mortgage_loan_payment_per_year = {record.mortgage_loan_payment_per_year},
            donation_value_per_year = {record.donation_value_per_year},
            educational_expenses_per_year = {record.educational_expenses_per_year}
        WHERE
            id = {record.id}"""

    try:
        cursor = GetCursor()
        cursor.execute( Sql_UpdateRecord )
        cursor.connection.commit()
    except:
        cursor.connection.rollback() 
        raise Exception("No fue posible actualizar el registro: " + str(id))

def DeleteTable():
    """Borra (DROP) la tabla registros en su totalidad"""  

    Sql_DeleteTable = """DROP TABLE registros"""

    cursor = GetCursor()
    cursor.execute( Sql_DeleteTable )
    cursor.connection.commit()