import sys
sys.path.append (".")
import os
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import SecretConfig
""" Define el directorio base del proyecto"""
base_dir = os.path.abspath(os.path.dirname(__file__))
"""Configura el directorio de plantillas relativo al directorio base"""
template_dir = os.path.join(base_dir, '../templates')

"""Crea la aplicación Flask"""
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key'

"""Función para conectar a la base de datos"""
def conectar_db():
    conn_string =SecretConfig.PGCODE
    conn = psycopg2.connect(conn_string)
    return conn

"""Ruta para la página de inicio"""
@app.route('/')
def index():
    return render_template('index.html')

"""Ruta para agregar un usuario"""
@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        """ Obtener datos del formulario"""
        id_usuario = request.form['id_usuario']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        documento_identidad = request.form['documento_identidad']
        correo_electronico = request.form['correo_electronico']
        telefono = request.form['telefono']
        salario = request.form['salario']

        """ Conectar a la base de datos"""
        conn = conectar_db()
        cursor = conn.cursor()

        try:
            """ Insertar el nuevo usuario en la base de datos"""
            cursor.execute(
                "INSERT INTO usuarios (id_usuario, nombre, apellido, documento_identidad, correo_electronico, telefono, salario) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (id_usuario, nombre, apellido, documento_identidad, correo_electronico, telefono, salario)
            )
            conn.commit()
            flash('Usuario agregado exitosamente')
        except (Exception, psycopg2.Error) as e:
            flash('Error al agregar el usuario: ' + str(e))
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('index'))

    return render_template('agregar_usuario.html')

@app.route('/agregar_declaracion', methods=['GET', 'POST'])
def agregar_declaracion():
    if request.method == 'POST':
        """ Obtener datos del formulario"""
        id_usuario = request.form.get('id_usuario')
        ingresos_laborales = request.form.get('ingresos_laborales')
        otros_ingresos_gravables = request.form.get('otros_ingresos_gravables', 0)
        otros_ingresos_no_gravables = request.form.get('otros_ingresos_no_gravables', 0)
        retenciones = request.form.get('retenciones')
        seguridad_social = request.form.get('seguridad_social')
        aportes_pension = request.form.get('aportes_pension')
        gastos_creditos_hipotecarios = request.form.get('gastos_creditos_hipotecarios')
        donaciones = request.form.get('donaciones', 0)
        gastos_educacion = request.form.get('gastos_educacion', 0)

        """ Calcular valores adicionales"""
        total_ingresos_gravados = float(ingresos_laborales) + float(otros_ingresos_gravables)
        total_ingresos_no_gravados = float(otros_ingresos_no_gravables)
        total_costos_deducibles = float(seguridad_social) + float(aportes_pension) + float(gastos_creditos_hipotecarios) + float(donaciones) + float(gastos_educacion)

        """ Validar los datos"""
        if not all([id_usuario, ingresos_laborales, retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios]):
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('agregar_declaracion'))

        # Proporcionar un valor por defecto para valor_impuesto
        valor_impuesto = 0  # O cualquier otro valor por defecto

        # Conectar a la base de datos y agregar la declaración
        conn = conectar_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO declaracion (id_usuario, ingresos_laborales, otros_ingresos_gravables, otros_ingresos_no_gravables, retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles, valor_impuesto) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
                (id_usuario, ingresos_laborales, otros_ingresos_gravables, otros_ingresos_no_gravables, retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion, total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles, valor_impuesto)
            )
            conn.commit()
            flash('Declaración agregada exitosamente', 'success')
            # Redirigir a la parte de resultados
            return render_template('agregar_declaracion.html', id_usuario=id_usuario, total_ingresos_gravados=total_ingresos_gravados, total_ingresos_no_gravados=total_ingresos_no_gravados, total_costos_deducibles=total_costos_deducibles, valor_impuesto=valor_impuesto)
        except Exception as e:
            conn.rollback()
            flash('Error al agregar la declaración: ' + str(e), 'error')
        finally:
            cursor.close()
            conn.close()

    return render_template('agregar_declaracion.html')

@app.route('/registrar_resultados', methods=['POST'])
def registrar_resultados():
    id_usuario = request.form['id_usuario']
    total_ingresos_gravados = request.form['total_ingresos_gravados']
    total_ingresos_no_gravados = request.form['total_ingresos_no_gravados']
    total_costos_deducibles = request.form['total_costos_deducibles']
    valor_impuesto = request.form['valor_impuesto']

    conn = conectar_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO ingresos (total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles, valor_impuesto, id_usuario) VALUES (%s, %s, %s, %s, %s)',
            (total_ingresos_gravados, total_ingresos_no_gravados, total_costos_deducibles, valor_impuesto, id_usuario)
        )

        conn.commit()
        flash('Resultados de la declaración registrados exitosamente')
    except Exception as e:
        conn.rollback()
        flash('Error al registrar los resultados: ' + str(e))
    finally:
        cursor.close()
        conn.close()

    return redirect(url_for('index'))

""" Ruta para consultar un usuario"""
@app.route('/consultar_usuario', methods=['GET', 'POST'])
def consultar_usuario():
    usuario = None
    declaraciones = None
    ingresos = None
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']

        conn = conectar_db()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            usuario = cursor.fetchone()
            
            cursor.execute("SELECT * FROM declaracion WHERE id_usuario = %s", (id_usuario,))
            declaraciones = cursor.fetchall()

            cursor.execute("SELECT * FROM ingresos WHERE id_usuario = %s", (id_usuario,))
            ingresos = cursor.fetchall()

        except (Exception, psycopg2.Error) as e:
            flash('Error al consultar el usuario: ' + str(e))
        finally:
            cursor.close()
            conn.close()

    return render_template('consultar_usuario.html', usuario=usuario, declaraciones=declaraciones, ingresos=ingresos)



""" Ruta para eliminar un usuario"""
@app.route('/eliminar_usuario', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']

        # Conectar a la base de datos
        conn = conectar_db()
        cursor = conn.cursor()

        try:
            # Eliminar el usuario de la base de datos
            cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            conn.commit()
            flash('Usuario eliminado exitosamente')
        except (Exception, psycopg2.Error) as e:
            flash('Error al eliminar el usuario: ' + str(e))
            conn.rollback()
        finally:
            cursor.close()
            conn.close()

        return redirect(url_for('index'))

    return render_template('eliminar_usuario.html')

if __name__ == '__main__':
    app.run(debug=True)

