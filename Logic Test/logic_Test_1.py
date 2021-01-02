from datetime import datetime import csv
import os
#----------------------------------------------------------------------------- # Função para cadastro de novos clientes
def cadastrar_cliente():
print('\n------ CADASTRO DE CLIENTES ------\n') cadastro = {}
nome = input("Nome.......: ")
cpf = input("CPF........: ")
rg = input("RG.........: ")
cadastro[cpf] = [nome, rg] # Salva os dados em um dicionário

listaClientes = [nome, sobrenome, CPF, RG]
type(listaClientes)
print(listaClientes)

# armazendo informações dos clientes em um dicionário
dicionarioClientes = {}
dicionarioClientes[CPF] = [CPF, nome, sobrenome, RG]
# conferindo a criação do dicionário com dados de cliente e CPF como chave 
dicionarioClientes

# criando arquivo clientes.csv com dados do cliente 
import csv
with open('clientes.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['CPF', 'RG', 'nome', 'sobrenome'])

with open('clientes.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:


    print(', '.join(row))

# função de cadastro com os dados de filmes
nomeFilme = input("Por favor digite o nome do filme: ")
anoFilme = input("Por favor digite o ano de lançamento do filme: ")
tipoReproducao = input("Trata-se de um DVD ou Fita? ")
codigoFilme = input("Por favor digite o código do filme ")

dicionarioFilmes = {}
# chave: código do filme
dicionarioFilmes[codigoFilme] = [codigoFilme, nomeFilme, anoFilme, tipoReproducao]
print(dicionarioFilmes)

#gerando arquivo filme.csv
import csv
with open('filmes.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['codigoFilme', 'tipoReproducao', 'nomeFilme', 'anoFilme'])

with open('filmes.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:


    print('; '.join(row))


nomeFilme = nomeFilme
anoFilme = anoFilme
tipoReproducao = tipoReproducao
codigoFilme = codigoFilme 

from datetime import datetime

date_entry = input('Coloque a data da locação no formato AAAA/MM/DD')
year, month, day = map(int, date_entry.split('/'))
dataLocacao = datetime(year, month, day)



dicionarioLocacao = {}
# chave: código do filme
dicionarioLocacao[codigoFilme] = [codigoFilme, nomeFilme, dataLocacao]
print(dicionarioLocacao)

#gerando arquivo emprestimos.csv
import csv
with open('emprestimos.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['codigoFilme', ' nomeFilme', 'dataLocacao'])

with open('emprestimos.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  for row in spamreader:


    print('; '.join(row))
