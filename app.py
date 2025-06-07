from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Usuário e senha simulados
USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        senha = request.form["senha"]
        if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
            return redirect(url_for("bem_vindo"))
        else:
            return "Usuário ou senha incorretos!"
    return render_template("login.html")

@app.route("/bem-vindo")
def bem_vindo():
    return "<h1>Bem-vindo ao sistema!</h1>"

if __name__ == "__main__":
    app.run(debug=True)
