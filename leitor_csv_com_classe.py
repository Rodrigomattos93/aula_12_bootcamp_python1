import csv

class LeitorCSV():
    def __init__(self, caminho_csv: str):
        self.caminho_csv = caminho_csv
    
    def carregar_csv(self) -> list[dict]:
        with open(self.caminho_csv, encoding = "utf-8") as csvfile:
            arquivo = csv.DictReader(csvfile, delimiter = ";")
            self.lista = list()
            for row in arquivo:
                self.lista.append(row)
            return self.lista
    
    def filtrar_lista_carregada(self, coluna: str, valor_coluna: str) -> list[dict]:
        lista_filtrada = []
        for i in range(0, len(self.lista)):
            if self.lista[i][coluna] == valor_coluna:
                lista_filtrada.append(self.lista[i])
        return lista_filtrada


dados_aleatorios = LeitorCSV("dados_aleatorios.csv")
dados_aleatorios.carregar_csv()
dados_aleatorios_filtrados = dados_aleatorios.filtrar_lista_carregada(coluna = "Cidade", valor_coluna = "Curitiba")
print(dados_aleatorios_filtrados)
