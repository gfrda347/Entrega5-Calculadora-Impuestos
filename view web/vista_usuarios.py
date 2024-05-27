import os
from flask import Flask, render_template, request, redirect, url_for, flash

# Define el directorio base del proyecto
base_dir = os.path.abspath(os.path.dirname(__file__))
# Configura el directorio de plantillas relativo al directorio base
template_dir = os.path.join(base_dir, '../templates')

# Crea la aplicación Flask
app = Flask(__name__, template_folder=template_dir)
app.secret_key = 'your_secret_key'

# Función para conectar a la base de datos (placeholder)
def conectar_db():
    # Aquí iría la conexión a la base de datos
    pass

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

        # Aquí iría la lógica para agregar el usuario a la base de datos

        flash('Usuario agregado exitosamente')
        return redirect(url_for('index'))
    
    return render_template('agregar_usuario.html')

# Ruta para agregar una declaración
@app.route('/agregar_declaracion', methods=['GET', 'POST'])
def agregar_declaracion():
    if request.method == 'POST':
        # Obtener datos del formulario
        id_usuario = request.form['id_usuario']
        ingresos_laborales = request.form['ingresos_laborales']
        otros_ingresos = request.form['otros_ingresos']
        retenciones = request.form['retenciones']
        seguridad_social = request.form['seguridad_social']
        aportes_pension = request.form['aportes_pension']
        gastos_creditos_hipotecarios = request.form['gastos_creditos_hipotecarios']
        donaciones = request.form['donaciones']
        gastos_educacion = request.form['gastos_educacion']

        # Validar los datos (puedes agregar más validaciones según necesites)
        if not all([id_usuario, ingresos_laborales, otros_ingresos, retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion]):
            flash('Todos los campos son obligatorios')
            return redirect(url_for('agregar_declaracion'))

        # Conectar a la base de datos y agregar la declaración
        conn = conectar_db()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO declaraciones (id_usuario, ingresos_laborales, otros_ingresos, retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                (id_usuario, ingresos_laborales, otros_ingresos, retenciones, seguridad_social, aportes_pension, gastos_creditos_hipotecarios, donaciones, gastos_educacion)
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
        
        # Aquí iría la lógica para consultar los datos del usuario en la base de datos
        
        # Suponiendo que el resultado de la consulta se almacene en la variable usuario
    
    return render_template('consultar_usuario.html', usuario=usuario)

# Ruta para eliminar un usuario
@app.route('/eliminar_usuario', methods=['GET', 'POST'])
def eliminar_usuario():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        
        # Aquí iría la lógica para eliminar el usuario de la base de datos
        
        flash('Usuario eliminado exitosamente')
        return redirect(url_for('index'))
    
    return render_template('eliminar_usuario.html')

if __name__ == '__main__':
    app.run(debug=True)
