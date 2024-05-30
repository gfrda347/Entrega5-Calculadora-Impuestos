import sys
sys.path.append ("src")
from flask import Flask, render_template, request
from model import TaxLogic
from controller import ControllerRegistros

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        id = int(request.form['id'])
        total_labor_income_per_year = int(request.form['total_labor_income_per_year'])
        other_taxable_income_per_year = int(request.form['other_taxable_income_per_year'])
        other_non_taxable_income_per_year = int(request.form['other_non_taxable_income_per_year'])
        source_retention_value_per_year = int(request.form['source_retention_value_per_year'])
        mortgage_loan_payment_per_year = int(request.form['mortgage_loan_payment_per_year'])
        donation_value_per_year = int(request.form['donation_value_per_year'])
        educational_expenses_per_year = int(request.form['educational_expenses_per_year'])

        tax_information = TaxLogic.TaxInformation(
            id,
            total_labor_income_per_year,
            other_taxable_income_per_year,
            other_non_taxable_income_per_year,
            source_retention_value_per_year,
            mortgage_loan_payment_per_year,
            donation_value_per_year,
            educational_expenses_per_year
        )

        ControllerRegistros.InsertRecord(tax_information)

        result = TaxLogic.calculateTax(tax_information)

        return render_template('result.html', result=result)

    except ValueError:
        error_message = "Por favor, llene todos los campos con valores numéricos válidos (enteros)."
        return render_template('error.html', error_message=error_message)

    except Exception as e:
        error_message = f"Error: {str(e)}"
        return render_template('error.html', error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
