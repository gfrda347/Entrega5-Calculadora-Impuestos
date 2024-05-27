# Todas las pruebas unitarias importan la biblioteca unittest
import unittest

# Las pruebas importan los modulos que hacen el trabajo
import sys
sys.path.append("src")

from model import TaxLogic

class TaxesTest(unittest.TestCase):


    #PRUEBAS UNITARIAS NORMALES

    def testNormal1(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 1,
            total_labor_income_per_year = 15600000, 
            other_taxable_income_per_year = 9600000, 
            other_non_taxable_income_per_year = 516000, 
            source_retention_value_per_year = 600000, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 0)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 25200000 
        total_untaxed_income = 516000 
        total_deductible_costs = 1248000 
        amount_to_pay_income_taxes = 0 

        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )
    

    def testNormal2(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 2,
            total_labor_income_per_year = 24000000, 
            other_taxable_income_per_year = 13000000, 
            other_non_taxable_income_per_year = 0, 
            source_retention_value_per_year = 1000000, 
            mortgage_loan_payment_per_year = 9600000, 
            donation_value_per_year = 200000, 
            educational_expenses_per_year= 100000)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 37000000
        total_untaxed_income = 0
        total_deductible_costs = 11820000
        amount_to_pay_income_taxes = 0

        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )

    
    def testNormal3(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 3,
            total_labor_income_per_year = 60000000, 
            other_taxable_income_per_year = 30000000, 
            other_non_taxable_income_per_year = 1200000, 
            source_retention_value_per_year = 4000000, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 10000000)


        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 90000000
        total_untaxed_income = 1200000
        total_deductible_costs = 14800000
        amount_to_pay_income_taxes = 17056000

        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )

    
    def testNormal4(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 4,
            total_labor_income_per_year = 96000000, 
            other_taxable_income_per_year = 35500000, 
            other_non_taxable_income_per_year = 3000000, 
            source_retention_value_per_year = 4800000, 
            mortgage_loan_payment_per_year = 12000000, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 1000000)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 131500000
        total_untaxed_income = 3000000
        total_deductible_costs = 20680000
        amount_to_pay_income_taxes = 26229600

        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )

    
    def testNormal5(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 5,
            total_labor_income_per_year = 120000000, 
            other_taxable_income_per_year = 0, 
            other_non_taxable_income_per_year = 5000000, 
            source_retention_value_per_year = 5000000, 
            mortgage_loan_payment_per_year = 1300000, 
            donation_value_per_year = 3000000, 
            educational_expenses_per_year= 7000000)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 120000000
        total_untaxed_income = 5000000
        total_deductible_costs = 20900000
        amount_to_pay_income_taxes = 22748000

        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )

    
    def testNormal6(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 6,
            total_labor_income_per_year = 420000000, 
            other_taxable_income_per_year = 180000000, 
            other_non_taxable_income_per_year = 10000000, 
            source_retention_value_per_year = 120000000, 
            mortgage_loan_payment_per_year = 36000000, 
            donation_value_per_year = 5000000, 
            educational_expenses_per_year= 24000000)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 600000000
        total_untaxed_income = 10000000
        total_deductible_costs = 98600000
        amount_to_pay_income_taxes = 55490000

        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )
    

    #PRUEBAS UNITARIAS EXTRAORDINARIAS
    
    #Ingresos no gravables son mayores
    def testExtraordinary1(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 7,
            total_labor_income_per_year = 15600000, 
            other_taxable_income_per_year = 0, 
            other_non_taxable_income_per_year = 20000000, 
            source_retention_value_per_year = 600000, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 0)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 15600000
        total_untaxed_income = 20000000
        total_deductible_costs = 1248000
        amount_to_pay_income_taxes = 0

        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )

    
    #Ganarse la loteria
    def testExtraordinary2(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 8,
            total_labor_income_per_year = 15600000, 
            other_taxable_income_per_year = 5000000000, 
            other_non_taxable_income_per_year = 0, 
            source_retention_value_per_year = 1000000, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 20000000)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 5015600000
        total_untaxed_income = 0
        total_deductible_costs = 21248000
        amount_to_pay_income_taxes = 1946797280

        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )
    

    #Perdida en otros ingresos gravables
    def testExtraordinary3(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 9,
            total_labor_income_per_year = 70000000, 
            other_taxable_income_per_year = -100000000, 
            other_non_taxable_income_per_year = 0, 
            source_retention_value_per_year = 4800000, 
            mortgage_loan_payment_per_year = 12000000, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 15000000)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = -30000000
        total_untaxed_income = 0
        total_deductible_costs = 32600000
        amount_to_pay_income_taxes = 0


        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )

    
    #Donaciones de alto valor
    def testExtraordinary4(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 10,
            total_labor_income_per_year = 30000000, 
            other_taxable_income_per_year = 15000000, 
            other_non_taxable_income_per_year = 5000000, 
            source_retention_value_per_year = 3000000, 
            mortgage_loan_payment_per_year = 10000000, 
            donation_value_per_year = 50000000, 
            educational_expenses_per_year= 0)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 45000000
        total_untaxed_income = 5000000
        total_deductible_costs = 62400000
        amount_to_pay_income_taxes = 0


        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )

    
    #Herencia
    def testExtraordinary5(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 11,
            total_labor_income_per_year = 24000000, 
            other_taxable_income_per_year = 9600000, 
            other_non_taxable_income_per_year = 350000000, 
            source_retention_value_per_year = 1500000, 
            mortgage_loan_payment_per_year = 500000, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 5000000)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 33600000
        total_untaxed_income = 350000000
        total_deductible_costs = 7420000
        amount_to_pay_income_taxes = 0


        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )

    
    #Gastos extraordinarios en educacion
    def testExtraordinary6(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 12,
            total_labor_income_per_year = 17000000, 
            other_taxable_income_per_year = 5000000, 
            other_non_taxable_income_per_year = 0, 
            source_retention_value_per_year = 1500000, 
            mortgage_loan_payment_per_year = 1000000, 
            donation_value_per_year = 800000, 
            educational_expenses_per_year= 20000000)
        

        #Proceso
        result = TaxLogic.calculateTax(TaxInformation)

        #Datos de salida esperados
        total_taxed_income = 22000000
        total_untaxed_income = 0
        total_deductible_costs = 23160000
        amount_to_pay_income_taxes = 0


        #Validacion de datos
        self.assertEqual( total_taxed_income, result[0] )
        self.assertEqual( total_untaxed_income, result[1] )
        self.assertEqual( total_deductible_costs, result[2] )
        self.assertEqual( amount_to_pay_income_taxes, result[3] )


    
    #PRUEBAS UNITARIAS DE ERROR

    #Retencion en la fuente superior a los ingresos laborales    
    def testError1(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 13,
            total_labor_income_per_year = 15000000, 
            other_taxable_income_per_year = 10000000, 
            other_non_taxable_income_per_year = 1000000, 
            source_retention_value_per_year = 30000000, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 5000000)
        

        #Validacion
        with self.assertRaises(TaxLogic.HigherIncomeRetentionException):
            TaxLogic.calculateTax(TaxInformation)

    
    #Error por ingresar texto
    def testError2(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 14,
            total_labor_income_per_year = "Mil millones", 
            other_taxable_income_per_year = 0, 
            other_non_taxable_income_per_year = 0, 
            source_retention_value_per_year = 0, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 0)
        

        #Validacion
        with self.assertRaises(TaxLogic.InvalidEntryException):
            TaxLogic.calculateTax(TaxInformation)

    
    #Error digitos muy grandes
    def testError3(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 15,
            total_labor_income_per_year = 80000000000, 
            other_taxable_income_per_year = 1000000000, 
            other_non_taxable_income_per_year = 3000000, 
            source_retention_value_per_year = 6000000, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 0)
        

        #Validacion
        with  self.assertRaises(TaxLogic.DigitsVeryLargeError):
            TaxLogic.calculateTax(TaxInformation)

    
    #Error por datos obligatorios no agregados
    def testError4(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 16,
            total_labor_income_per_year = 0, 
            other_taxable_income_per_year = 10000, 
            other_non_taxable_income_per_year = 0, 
            source_retention_value_per_year = 0, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 0)
        

        #Validacion
        with self.assertRaises(TaxLogic.DataNotAggregatedError):
            TaxLogic.calculateTax(TaxInformation)

    
    #Error por deduccibles negativos
    def testError5(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 17,
            total_labor_income_per_year = 15000000, 
            other_taxable_income_per_year = 1000000, 
            other_non_taxable_income_per_year = 1000000, 
            source_retention_value_per_year = 500000, 
            mortgage_loan_payment_per_year = -15000000, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 0)
        

        #Validacion
        with self.assertRaises(TaxLogic.DeductiblesNegativeError):
            TaxLogic.calculateTax(TaxInformation)

    
    #No ingresar los activos
    def testError6(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 18,
            total_labor_income_per_year = 0, 
            other_taxable_income_per_year = 0, 
            other_non_taxable_income_per_year = 0, 
            source_retention_value_per_year = 0, 
            mortgage_loan_payment_per_year = 2000000, 
            donation_value_per_year = 4000000, 
            educational_expenses_per_year= 3000000)
        

        #Validacion
        with self.assertRaises(TaxLogic.AssetsNotEnteredException):
            TaxLogic.calculateTax(TaxInformation)

    
    #Ingresar un valor negativo en los ingresos.
    def testError7(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 19,
            total_labor_income_per_year = -15600000, 
            other_taxable_income_per_year = -1000000, 
            other_non_taxable_income_per_year = -300000, 
            source_retention_value_per_year = 1000000, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 0)
        

        #Validacion
        with self.assertRaises(TaxLogic.NegativeValueEnteredException):
            TaxLogic.calculateTax(TaxInformation)

    
    #Caso de error en caso de ingresar cifras no coherentes
    def testError8(self):

        #Datos de entrada
        TaxInformation = TaxLogic.TaxInformation(
            id = 20,
            total_labor_income_per_year = 0.000525, 
            other_taxable_income_per_year = 250000, 
            other_non_taxable_income_per_year = 50000, 
            source_retention_value_per_year = 0, 
            mortgage_loan_payment_per_year = 0, 
            donation_value_per_year = 0, 
            educational_expenses_per_year= 0)
        

        #Validacion
        with self.assertRaises(TaxLogic.IncoherentFiguresExpection):
            TaxLogic.calculateTax(TaxInformation)


# Este fragmento de codigo permite ejecutar el formato individualmente
if __name__ == '__main__':
    unittest.main()