# Todas las pruebas unitarias importan la biblioteca unittest
import unittest

# Las pruebas importan los modulos que hacen el trabajo
import sys
sys.path.append("src")

from model.TaxLogic import TaxInformation

from controller import ControllerRegistros

class TaxesTest(unittest.TestCase):

    #Caso Normal Insert
    def testInsert1( self ):

        #Eliminamos la tabla registro y la volvemos a crear
        ControllerRegistros.DeleteTable()
        ControllerRegistros.CreateTable()

        #Insertamos un nuevo usuario a la tabla
        UserTest = TaxInformation(id=1,
                                total_labor_income_per_year=12,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)
        ControllerRegistros.InsertRecord( UserTest )

        #Verifico si lo trajo correctamente
        UserSearch = ControllerRegistros.SearchRecordByID( 1 )

        self.assertEqual( UserTest.id, UserSearch.id)

    
    #Caso Error Insert
    def testInsert2( self ):

        #Eliminamos la tabla registro y la volvemos a crear
        ControllerRegistros.DeleteTable()
        ControllerRegistros.CreateTable()

        #Insertamos un nuevo usuario a la tabla
        UserTest = TaxInformation(id=1,
                                total_labor_income_per_year=12,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)
        ControllerRegistros.InsertRecord( UserTest )

        #valido
        with self.assertRaises(Exception):
            ControllerRegistros.InsertRecord( UserTest )
        
    
    #Caso Normal Delete
    def testDelete1( self ):

        #Eliminamos la tabla registro y la volvemos a crear
        ControllerRegistros.DeleteTable()
        ControllerRegistros.CreateTable()

        #Insertamos un nuevo usuario a la tabla
        UserTest = TaxInformation(id=1,
                                total_labor_income_per_year=12,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)
        ControllerRegistros.InsertRecord( UserTest )

        #Borrar usuario
        Aux = ControllerRegistros.DeleteRecord( 1 )
    
        self.assertNotEqual( UserTest.id, Aux)
    

    #Caso Error Delete
    def testDelete2( self ):

        #Eliminamos la tabla registro y la volvemos a crear
        ControllerRegistros.DeleteTable()
        ControllerRegistros.CreateTable()

        #Insertamos un nuevo usuario a la tabla
        UserTest = TaxInformation(id=1,
                                total_labor_income_per_year=12,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)
        ControllerRegistros.InsertRecord( UserTest )

        #Borrar registro
        ControllerRegistros.DeleteRecord( 1 )

        #valido
        with self.assertRaises(Exception):
            ControllerRegistros.DeleteRecord( 1 )
    

    #Caso Normal Search
    def testSearch1( self ):

        #Eliminamos la tabla registro y la volvemos a crear
        ControllerRegistros.DeleteTable()
        ControllerRegistros.CreateTable()

        #Insertamos un nuevo usuario a la tabla
        UserTest = TaxInformation(id=1,
                                total_labor_income_per_year=12,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)
        ControllerRegistros.InsertRecord( UserTest )

        #Verifico si lo trajo correctamente
        UserSearch = ControllerRegistros.SearchRecordByID( 1 )

        self.assertEqual( UserTest.id, UserSearch.id)
    

    #Caso Error Search
    def testSearch2( self ):

        #Eliminamos la tabla registro y la volvemos a crear
        ControllerRegistros.DeleteTable()
        ControllerRegistros.CreateTable()

        #Validacion
        with self.assertRaises(ControllerRegistros.ErrorNotFound):
            ControllerRegistros.SearchRecordByID( 2 )
    

    #Caso Normal Update
    def testUpdate1( self ):

        #Eliminamos la tabla registro y la volvemos a crear
        ControllerRegistros.DeleteTable()
        ControllerRegistros.CreateTable()

        #Insertamos un nuevo usuario a la tabla
        UserTest = TaxInformation(id=1,
                                total_labor_income_per_year=12,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)
        ControllerRegistros.InsertRecord( UserTest )

        #Creamos usuario actualizado
        UserUpdate = TaxInformation(id=1,
                                total_labor_income_per_year=133,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)
        
        #Actualizamos el usuario que esta en la tabla
        ControllerRegistros.UpdateRecord( UserUpdate )

        #Verifico si lo trajo correctamente
        UserSearch = ControllerRegistros.SearchRecordByID( 1 )

        self.assertEqual( UserUpdate.id, UserSearch.id)
    

    #Caso Error Update
    def testUpdate2( self ):

        #Eliminamos la tabla registro y la volvemos a crear
        ControllerRegistros.DeleteTable()
        ControllerRegistros.CreateTable()

        #Insertamos un nuevo usuario a la tabla
        UserTest = TaxInformation(id=1,
                                total_labor_income_per_year=12,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)
        ControllerRegistros.InsertRecord( UserTest )

        #Creamos usuario actualizado
        UserUpdate = TaxInformation(id=2,
                                total_labor_income_per_year=133,
                                other_taxable_income_per_year=12,
                                other_non_taxable_income_per_year=12,
                                source_retention_value_per_year=12,
                                mortgage_loan_payment_per_year=12,
                                donation_value_per_year=12,
                                educational_expenses_per_year=12)

        #valido
        with self.assertRaises(Exception):
            ControllerRegistros.UpdateRecord( UserUpdate )


if __name__ == '__main__':
    unittest.main()