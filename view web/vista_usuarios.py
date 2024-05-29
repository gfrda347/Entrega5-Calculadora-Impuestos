import sys
sys.path.append (".")
import os
from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2
import SecretConfig
# Define el directorio base del proyecto
base_dir = os.path.abspath(os.path.dirname(__file__))
# Configura el directorio de plantillas relativo al directorio base
template_dir = os.path.join(base_dir, '../templates')

# Crea la aplicación Flask
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key'

# Función para conectar a la base de datos (placeholder)
def conectar_db():
    conn_string = f"host={SecretConfig.PGHOST} dbname={SecretConfig.PGDATABASE} user={SecretConfig.PGUSER} password={SecretConfig.PGPASSWORD}"
    conn = psycopg2.connect(conn_string)
    return conn

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para agregar un usuario
@app.route('/agregar_usuario', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        # Obtener datos del formulario
        id_usuario = request.form['id_usuario']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        documento_identidad = request.form['documento_identidad']
        correo_electronico = request.form['correo_electronico']
        telefono = request.form['telefono']
        salario = request.form['salario']

        # Conectar a la base de datos
        conn = conectar_db()
        cursor = conn.cursor()

        try:
            # Insertar el nuevo usuario en la base de datos
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

# Ruta para agregar una declaración
@app.route('/agregar_declaracion', methods=['GET', 'POST'])
def agregar_declaracion():
    if request.method == 'POST':
        # Obtener datos del formulario
        id_usuario = request.form['id_usuario']
        ingresos_laborales = request.form['ingresos_laborales']
        otros_ingresos_gravables = request.form.get('otros_ingresos_gravables', 0)
        otros_ingresos_no_gravables = request.form.get('otros_ingresos_no_gravables', 0)
        retenciones = request.form['retenciones']
        seguridad_social = request.form['seguridad_social']
        aportes_pension = request.form['aportes_pension']
        gastos_creditos_hipotecarios = request.form['gastos_creditos_hipotecarios']
        donaciones = request.form.get('donaciones', 0)
        gastos_educacion = request.form.get('gastos_educacion', 0)

        # Validar los datos (puedes agregar más validaciones según necesites)
        if not all([id_usuario, ingresos_laborales, otros_ingresos_gravables, otros_ingresos_no_gravables ,retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion]):
            flash('Todos los campos son obligatorios')
            return redirect(url_for('agregar_declaracion'))

        # Conectar a la base de datos y agregar la declaración
        conn = conectar_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO retencion (id_usuario, ingresos_laborales, otros_ingresos, retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (id_usuario, ingresos_laborales, otros_ingresos_gravables,otros_ingresos_no_gravables, retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion)
            )
            conn.commit()
            flash('Declaración agregada exitosamente')
        except Exception as e:
            conn.rollback()
            flash('Error al agregar la declaración: ' + str(e))
        finally:
            conn.close()
        
        return redirect(url_for('index'))
    
    return render_template('agregar_declaracion.html')

# Ruta para consultar un usuario
@app.route('/consultar_usuario', methods=['GET', 'POST'])
def consultar_usuario():
    usuario = None
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']

        # Conectar a la base de datos
        conn = conectar_db()
        cursor = conn.cursor()

        try:
            # Consultar los datos del usuario en la base de datos
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (id_usuario,))
            usuario = cursor.fetchone()
        except (Exception, psycopg2.Error) as e:
            flash('Error al consultar el usuario: ' + str(e))
        finally:
            cursor.close()
            conn.close()

    return render_template('consultar_usuario.html', usuario=usuario)
# Ruta para eliminar un usuario
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
