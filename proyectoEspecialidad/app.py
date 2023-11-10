from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bd_especialidad"
)

cursor = db.cursor()

# Ruta para la página de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario de contacto
@app.route('/enviar-mensaje', methods=['POST'])
def enviar_mensaje():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']

        # Insertar datos en la base de datos
        cursor.execute("INSERT INTO mensajes (nombre, email, mensaje) VALUES (%s, %s, %s)", (nombre, email, mensaje))
        db.commit()

        

    # Redirige a la página de inicio después de enviar el mensaje
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
