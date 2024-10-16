class Estado:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.proximo = None


class TabelaHash:
    def __init__(self):
        self.tamanho = 10
        self.tabela = [None] * self.tamanho

    def hash_function(self, sigla):
        if sigla == 'DF':
            return 7
        else:
            # Calcula o valor ASCII das duas letras e aplica a função de hash
            ascii_sum = ord(sigla[0]) + ord(sigla[1])
            return ascii_sum % self.tamanho

    def inserir(self, estado):
        posicao = self.hash_function(estado.sigla)
        novo_estado = Estado(estado.sigla, estado.nome)
        novo_estado.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo_estado

    def imprimir_tabela(self):
        for i in range(self.tamanho):
            if self.tabela[i] is None:
                print(f"Posição {i}: None")
            else:
                print(f"Posição {i}: ", end="")
                atual = self.tabela[i]
                while atual:
                    print(f"{atual.sigla}", end=" -> ")
                    atual = atual.proximo
                print("None")


# Criação dos estados
estados = [
    Estado("AC", "Acre"), Estado("AL", "Alagoas"), Estado("AP", "Amapá"),
    Estado("AM", "Amazonas"), Estado("BA", "Bahia"), Estado("CE", "Ceará"),
    Estado("ES", "Espírito Santo"), Estado("GO", "Goiás"), Estado("MA", "Maranhão"),
    Estado("MT", "Mato Grosso"), Estado("MS", "Mato Grosso do Sul"), Estado("MG", "Minas Gerais"),
    Estado("PA", "Pará"), Estado("PB", "Paraíba"), Estado("PR", "Paraná"),
    Estado("PE", "Pernambuco"), Estado("PI", "Piauí"), Estado("RJ", "Rio de Janeiro"),
    Estado("RN", "Rio Grande do Norte"), Estado("RS", "Rio Grande do Sul"),
    Estado("RO", "Rondônia"), Estado("RR", "Roraima"), Estado("SC", "Santa Catarina"),
    Estado("SP", "São Paulo"), Estado("SE", "Sergipe"), Estado("TO", "Tocantins"),
    Estado("DF", "Distrito Federal")
]

# Inicializar a tabela hash
tabela_hash = TabelaHash()

# Imprimir a tabela hash antes de inserir qualquer informação
print("Tabela Hash antes da inserção:")
tabela_hash.imprimir_tabela()
print()


def inserir_estados_na_tabela(tabela, estados):
    for estado in estados:
        tabela.inserir(estado)


inserir_estados_na_tabela(tabela_hash, estados)

print("Tabela Hash após inserir os 26 estados e o Distrito Federal - DF:")
tabela_hash.imprimir_tabela()
print()

estado_ficticio = Estado("FM", "Felipe Melo")
tabela_hash.inserir(estado_ficticio)

print("Tabela Hash após inserir os 26 estados, DF e o estado fictício:")
tabela_hash.imprimir_tabela()
