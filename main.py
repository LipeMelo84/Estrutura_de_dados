class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


class ListaEncadeada:
    def __init__(self):
        self.head = None

    def inserirSemPrioridade(self, nodo):
        if not self.head:
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = nodo

    def inserirComPrioridade(self, nodo):
        if not self.head or (self.head.cor == "V" and nodo.cor == "A") or \
                (self.head.cor == nodo.cor and self.head.numero > nodo.numero):
            nodo.proximo = self.head
            self.head = nodo
        else:
            atual = self.head
            while atual.proximo and (atual.proximo.cor == "A" or (atual.proximo.cor == nodo.cor and atual.proximo.numero <= nodo.numero)):
                atual = atual.proximo
            nodo.proximo = atual.proximo
            atual.proximo = nodo

    def inserir(self):
        cor = input("Digite a cor do cartão (A ou V): ").upper()
        numero = int(input("Digite o número do cartão: "))

        if cor == "A":
            numero += 200

        nodo = Nodo(numero, cor)

        if not self.head:
            self.head = nodo
        elif cor == "V":
            self.inserirSemPrioridade(nodo)
        elif cor == "A":
            self.inserirComPrioridade(nodo)

    def imprimirListaEspera(self):
        atual = self.head
        lista_espera = []
        while atual:
            lista_espera.append(f"[{atual.cor}, {atual.numero}]")
            atual = atual.proximo
        print(", ".join(lista_espera))

    def atenderPaciente(self):
        if not self.head:
            print("Nenhum paciente na fila.")
        else:
            print(f"Chamando paciente com cartão {self.head.cor} {self.head.numero} para atendimento.")
            self.head = self.head.proximo


def menu():
    lista = ListaEncadeada()
    while True:
        print("\nMenu:")
        print("1 – Adicionar paciente à fila")
        print("2 – Mostrar pacientes na fila")
        print("3 – Chamar paciente")
        print("4 – Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            lista.inserir()
        elif opcao == "2":
            lista.imprimirListaEspera()
        elif opcao == "3":
            lista.atenderPaciente()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
