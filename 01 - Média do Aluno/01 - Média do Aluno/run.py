from flask import Flask, render_template, request, redirect
                                                                                                                
app= Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/salvar_nota", methods=['POST'])
def validar_aluno():
    nome_aluno = request.form["nome_aluno"]
    nota_1 = float(request.form["nota_1"])
    nota_2 = float(request.form["nota_2"])
    nota_3 = float(request.form["nota_3"])
    
    # Calculando a média e arredondando para 2 casas decimais
    media = round((nota_1 + nota_2 + nota_3) / 3, 1)
    
    status = "Aprovado" if media >= 6 else "Reprovado"
   
    caminho_arquivo = 'models/notas.txt'
    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome_aluno};{nota_1};{nota_2};{nota_3};{media:};{status}\n")

    return redirect("/")

@app.route("/consulta")
def consulta_notas():
    notas = []
    caminho_arquivo = 'models/notas.txt'
    
    with open (caminho_arquivo, 'r') as arquivo:
        for nota in arquivo: 
            item = nota.strip().split(';')
            if len(item) == 6:
                notas.append({
                    'nome_aluno': item[0],
                    'nota_1': item[1],
                    'nota_2': item[2],
                    'nota_3': item[3],
                    'media': item[4],
                    'status': item[5]
                })    
            else:
                print(f"Linha inválida: {nota}")    
    
    return render_template("consulta_aluno.html", aluno=notas)

app.run(host='127.0.0.1', port=80, debug=True)
