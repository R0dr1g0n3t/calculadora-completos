from flask import Flask, render_template, request
from calculadora import calcular_ingredientes

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def inicio():
    if request.method == "POST":
        personas = int(request.form["personas"])
        completos_por_persona = int(request.form["completos_por_persona"])
        tipo = request.form["tipo"]

        resultado = calcular_ingredientes(personas, completos_por_persona, tipo)

        return render_template("index.html", resultado=resultado)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
