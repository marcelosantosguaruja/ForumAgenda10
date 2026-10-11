# ╔══════════════════════════════════════════════╗
# ║ Sistema para checagem de Estoque de Produtos ║░
# ╚══════════════════════════════════════════════╝░
#   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░

# Importação de comando do sistema para limpar a tela.
import os
os.system("CLS") # limpa o terminal

# atribuição da função para verificar o estoque.

def verificar_minimo(nome, estoqueatual):  # atribui os dois campos da função

# verificação do mínimo necessário.   
    if estoqueatual < 5:                   
        print(f"Alerta: O produto {nome} tem somente {estoqueatual} unidades. Precisa urgente de reposição!")
    else:
        print(f"Estoque atual de {nome} está com {estoqueatual} unidades. Isso é um nível seguro.")


# Solicita os dados ao usuário
nome = input("Digite o nome do produto: ")
comprado = int(input("Digite a quantidade de produtos comprados: "))
vendidos = int(input("Digite a quantidade de produtos vendidos: "))
estoqueatual = comprado - vendidos



# Executa a função
verificar_minimo(nome, estoqueatual)