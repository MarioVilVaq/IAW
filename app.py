from flask import Flask, render_template

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return render_template("index.html")

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)


import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def repos():
    # Reemplaza 'MarioVilVaq' con tu nombre de usuario de GitHub
    url = 'https://api.github.com/users/MarioVilVaq/repos'

    # Hacemos la petición a la API de GitHub
    response = requests.get(url)

    # Si la respuesta fue exitosa
    if response.status_code == 200:
        repos = response.json()  # Convertimos la respuesta en JSON
    else:
        repos = []  # Si algo falla, devolvemos una lista vacía

    return render_template('index.html', repos=repos)

if __name__ == "__main__":
    app.run(debug=True)
