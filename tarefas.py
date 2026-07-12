import json
 
 # Funções para carregar e salvar tarefas em um arquivo 
def carregar_tarefas():
     try:
         with open('tarefas.json', 'r') as arquivo:
             tarefas = json.load(arquivo)
     except FileNotFoundError:
         tarefas = []
     return tarefas

# Função para salvar tarefas em um arquivo 
def salvar_tarefas(tarefas):
    with open('tarefas.json', 'w') as arquivo:
        json.dump(tarefas, arquivo, indent=4)

# Função para listar todas as tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("sua lista esta vazia.")
    else:
        for tarefa in tarefas:
            status = " (concluída)" if tarefa['concluida'] else ""
            print(f"- {tarefa['titulo']}: {tarefa['descricao']}{status}")

# Função para adicionar uma nova tarefa
def adicionar_tarefa(titulo, descricao):
    tarefas = carregar_tarefas()
    tarefa = {
        'titulo': titulo,
        'descricao': descricao,
        'concluida': False
    }
    tarefas.append(tarefa)
    salvar_tarefas(tarefas)

# corpo do programa
def main():
    tarefas = carregar_tarefas()

    while True:
        print("\nGerenciador de Tarefas")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tarefas = carregar_tarefas()
            listar_tarefas()
        elif escolha == '2':
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(titulo, descricao)
            print("Tarefa adicionada com sucesso!")
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.") 

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)