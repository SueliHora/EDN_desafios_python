# -*- coding: utf-8 -*-

# ====================================================================
# Exercício 1: Programa de Saudação
# Crie um programa que imprima a mensagem "Olá, mundo!" na tela.
# ====================================================================
print("--- Exercício 1: Saudação ---")
mensagem = "Olá, mundo!"
print(mensagem)
print("\n" + "="*50 + "\n")


# ====================================================================
# Exercício 2: Calculadora de Soma
# Desenvolva um programa que soma dois números.
# ====================================================================
print("--- Exercício 2: Calculadora de Soma ---")
numero1 = 12
numero2 = 14
soma = numero1 + numero2
print(f"O primeiro número é: {numero1}")
print(f"O segundo número é: {numero2}")
print(f"A soma dos dois números é: {soma}")
print("\n" + "="*50 + "\n")


# ====================================================================
# Exercício 3: Calculadora de Volume
# Crie um programa que calcula o volume de uma caixa retangular.
# ====================================================================
print("--- Exercício 3: Calculadora de Volume ---")
comprimento = 12
largura = 14
altura = 20
volume = comprimento * largura * altura
print(f"Dimensões da caixa: {comprimento}cm x {largura}cm x {altura}cm")
print(f"O volume da caixa é: {volume} cm³")
print("\n" + "="*50 + "\n")


# ====================================================================
# Exercício 4: Calculadora de Preço Total
# Desenvolva um programa que calcula o preço total de uma compra.
# ====================================================================
print("--- Exercício 4: Calculadora de Preço Total ---")
nome_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3
preco_total = preco_unitario * quantidade

print(f"Produto: {nome_produto}")
# O :.2f formata o número para ter sempre duas casas decimais, ideal para moeda.
print(f"Preço Unitário: R$ {preco_unitario:.2f}")
print(f"Quantidade: {quantidade} unidades")
print("-" * 25)
print(f"Valor Total da Compra: R$ {preco_total:.2f}")
print("\n" + "="*50 + "\n")
