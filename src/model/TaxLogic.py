#Aplicacion realizada por Luis Pablo Goez Y Valentina Carmona

# EXCEPCIONES

#Mayor retencion de ingresos 
class HigherIncomeRetentionException( Exception ):
    def __str__(self):
        return "La retencion en la fuente no puede ser mayor al valor total de ingresos."

#Ingreso invalido
class InvalidEntryException( Exception ):
    def __str__(self):
        return "Ingresaste un valor invalido."

#Digitos muy grandes 
class DigitsVeryLargeError( Exception ):
    def __str__(self):
        return "Numeros ingresados muy grandes, exceden el valor normal a calcular."

#Datos no agregados 
class DataNotAggregatedError( Exception ):
    def __str__(self):
        return "El total de ingresos laborales al año no puede ser cero."
    
#Duducibles negativos  
class DeductiblesNegativeError( Exception ):
    def __str__(self):
        return "Algo anda mal, el total de tus deducibles es menor que cero(0)."

# Activos no ingresados
class AssetsNotEnteredException( Exception ):
    def __str__(self):
        return "Ingresos gravables y no gravables en cero, para proseguir con el calculo\n                                          almenos uno debe tener un valor."

# Valor negativo ingresos
class NegativeValueEnteredException( Exception ):
    def __str__(self):
        return "No puedes ingresar valor negativos en el total de ingresos\n            laborales al año y en otros ingresos gravables al año ."

#Cifras incoherentes
class IncoherentFiguresExpection( Exception ):
    def __str__(self):
        return "Ingresaste un valor incoherente, verifique y cambie"


#Clase con la informacion
class TaxInformation:
    def __init__(self, id: int, total_labor_income_per_year: int, other_taxable_income_per_year: int, other_non_taxable_income_per_year: int, source_retention_value_per_year: int, mortgage_loan_payment_per_year: int, donation_value_per_year: int, educational_expenses_per_year: int ):    
        self.id = id
        self.total_labor_income_per_year = total_labor_income_per_year
        self.other_taxable_income_per_year = other_taxable_income_per_year
        self.other_non_taxable_income_per_year = other_non_taxable_income_per_year
        self.source_retention_value_per_year = source_retention_value_per_year
        self.mortgage_loan_payment_per_year = mortgage_loan_payment_per_year
        self.donation_value_per_year = donation_value_per_year
        self.educational_expenses_per_year = educational_expenses_per_year

#Calcular el valor del impuesto a pagar
def calculateTax(objectTaxInfo):
    
    """
    id: Cedula
    total_labor_income_per_year: Total ingresos laborales al año
    other_taxable_income_per_year: Otros ingresos gravables al año
    other_non_taxable_income_per_year: Otros ingresos no gravables al año
    source_retention_value_per_year: Valor retencion en la fuente al año
    mortgage_loan_payment_per_year: Pago credito Hipotecario al año
    donation_value_per_year: Valor donaciones al año
    educational_expenses_per_year: Gastos en educacion al año
    social_security_payment_in_the_year: Valor a la seguridad social al año
    pension_contributions_in_the_year: Aporte a la pension al año
    """

    #CONSTANTES

    #Porcentaje seguridad social
    SOCIALSECURITYPERCENTAGE = 4

    #Porcentaje aporte a la pension
    PENSIONCONTRIBUTIONPERCENTAGE = 4

    #Maximo de digitos
    MAXDIGITS = 10

    #Limite de cifras
    NUMBERLIMIT = 6

    # Definir los rangos y tasas impositivas como una lista de tuplas
    TAX_RATES = [
        (float('-inf'), 1090, 0),
        (1090, 1700, 0.19),
        (1700, 4100, 0.28),
        (4100, 8670, 0.33),
        (8670, 18970, 0.35),
        (18970, 31000, 0.37),
        (31000, float('inf'), 0.39)
    ]

    #Valor unidad tributaria
    TAXUNITVALUE = 46076


    #CONTROL DE ERROR

    #Verificar ingreso de valores invalidos
    def checkInvalidValue(objectTaxInfo):
        if (type(objectTaxInfo.total_labor_income_per_year) == str or 
            type(objectTaxInfo.other_taxable_income_per_year) == str or 
            type(objectTaxInfo.other_non_taxable_income_per_year) == str or 
            type(objectTaxInfo.source_retention_value_per_year) == str or 
            type(objectTaxInfo.mortgage_loan_payment_per_year) == str or 
            type(objectTaxInfo.donation_value_per_year) == str or 
            type(objectTaxInfo.educational_expenses_per_year) == str):
            raise InvalidEntryException()
    
    #Verificar ingreso de valores negativos
    def checkNegativeValues(objectTaxInfo):
        if ((objectTaxInfo.total_labor_income_per_year < 0 or 
            objectTaxInfo.other_non_taxable_income_per_year < 0) and 
            objectTaxInfo.other_taxable_income_per_year < 0):
            raise NegativeValueEnteredException()
    
    #Verificar retencion en la fuenta mayor al valor total de ingresos
    def verifyWithholdingAtSourceGreaterThanTotalIncome(objectTaxInfo):
        if objectTaxInfo.source_retention_value_per_year > objectTaxInfo.total_labor_income_per_year:
            raise HigherIncomeRetentionException()

    #Verificar numeros ingresados muy grandes
    def verifyVeryLargeIncome(objectTaxInfo, MAXDIGITS):
        if (len(str(objectTaxInfo.total_labor_income_per_year)) > MAXDIGITS or 
            len(str(objectTaxInfo.other_taxable_income_per_year)) > MAXDIGITS or 
            len(str(objectTaxInfo.other_non_taxable_income_per_year)) > MAXDIGITS or 
            len(str(objectTaxInfo.source_retention_value_per_year)) > MAXDIGITS or 
            len(str(objectTaxInfo.mortgage_loan_payment_per_year)) > MAXDIGITS or 
            len(str(objectTaxInfo.donation_value_per_year)) > MAXDIGITS or 
            len(str(objectTaxInfo.educational_expenses_per_year)) > MAXDIGITS):
            raise DigitsVeryLargeError()
    
    #Verificar activos no agregados
    def checkNonAggregatedAssets(objectTaxInfo):
        if (objectTaxInfo.other_taxable_income_per_year == 0 and 
            objectTaxInfo.other_non_taxable_income_per_year == 0):
            raise AssetsNotEnteredException()

    #Verificar datos obligatorios no agregados
    def checkMandatoryNonAggregatedData(objectTaxInfo):
        if objectTaxInfo.total_labor_income_per_year == 0:
            raise DataNotAggregatedError()

    #Verificar valores incoherentes
    def checkInconsistentValues(objectTaxInfo, NUMBERLIMIT):
        if (objectTaxInfo.total_labor_income_per_year > 0 and 
            objectTaxInfo.total_labor_income_per_year < 1):
            num_str = str(objectTaxInfo.total_labor_income_per_year)
            if '.' in num_str:
                decimal_part = num_str.split('.')[1]
                if len(decimal_part) == NUMBERLIMIT:
                    raise IncoherentFiguresExpection()
    
    #Verificar deducibles menores que cero
    def verifyDeductiblesLessThanZero(total_deductible_costs):
        if total_deductible_costs < 0:
            raise DeductiblesNegativeError()
    

    #VALIDACIONES
    checkInvalidValue(objectTaxInfo)
    checkNegativeValues(objectTaxInfo)
    verifyWithholdingAtSourceGreaterThanTotalIncome(objectTaxInfo)
    verifyVeryLargeIncome(objectTaxInfo, MAXDIGITS)
    checkNonAggregatedAssets(objectTaxInfo)
    checkMandatoryNonAggregatedData(objectTaxInfo)
    checkInconsistentValues(objectTaxInfo, NUMBERLIMIT)
    

    #Calcular el valor a la seguridad social en el año y el aporte a la pension en el año
    social_security_payment_in_the_year = ( objectTaxInfo.total_labor_income_per_year * SOCIALSECURITYPERCENTAGE ) / 100
    pension_contributions_in_the_year = ( objectTaxInfo.total_labor_income_per_year * PENSIONCONTRIBUTIONPERCENTAGE ) / 100

    #Calcular Total de Ingresos NO Gravables
    total_untaxed_income = objectTaxInfo.other_non_taxable_income_per_year

    #Calcular el Total de Ingresos Gravados
    total_taxed_income =  ( objectTaxInfo.total_labor_income_per_year + objectTaxInfo.other_taxable_income_per_year + objectTaxInfo.other_non_taxable_income_per_year) - total_untaxed_income

    #Calcular Total Costos Deducibles
    total_deductible_costs = social_security_payment_in_the_year + pension_contributions_in_the_year + objectTaxInfo.mortgage_loan_payment_per_year + objectTaxInfo.donation_value_per_year + objectTaxInfo.educational_expenses_per_year


    #Validacion deducibles no sean menores que cero
    verifyDeductiblesLessThanZero(total_deductible_costs)
    

    #Calcular las unidades de valor tributario
    tax_value_units = total_taxed_income / TAXUNITVALUE

    # Iterar sobre las tuplas de rangos y tasas impositivas para encontrar la tasa impositiva adecuada
    for lower_limit, upper_limit, rate in TAX_RATES:
        if lower_limit < tax_value_units <= upper_limit:
            tax_rate = rate
            break

    
    #Calcular el valor a pagar por impuestos de rentas
    if tax_rate == 0:
        amount_to_pay_income_taxes = 0
    else:
        amount_to_pay_income_taxes = (( total_taxed_income - total_deductible_costs ) * tax_rate ) - objectTaxInfo.source_retention_value_per_year

    #Lista de resultados
    results = []
    results.append(total_taxed_income)
    results.append(total_untaxed_income)
    results.append(round(total_deductible_costs))
    results.append(round(amount_to_pay_income_taxes))

    return results