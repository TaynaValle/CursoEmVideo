##Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome
##"Santo"
nome = str(input('Digite o nome de uma cidade: '))
nome_lista = nome.split()
resultado = 'Santo' in nome_lista
print(resultado)
