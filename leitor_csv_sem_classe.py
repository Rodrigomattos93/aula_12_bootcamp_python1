import csv

with open('dados_aleatorios.csv', encoding = "utf-8") as csvfile:
    arquivo = csv.DictReader(csvfile, delimiter = ";")
    lista = list()
    for row in arquivo:
        lista.append(row)

lista_filtrada = []

for i in range(0, len(lista)):
    if lista[i]['Cidade'] == "Curitiba":
        lista_filtrada.append(lista[i]) 

print(lista_filtrada)
        