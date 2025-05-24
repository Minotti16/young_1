class AgendaComContados():
    def __init__(self):
        self.contados = []

    def adicionar_contado(self, nome):
        self.contados.append(nome)
        print(f'Contado {nome} adicionado com sucesso.')

    def remover_contado(self, nome):
        if nome in self.contados:
            self.contados.remove(nome)
            print(f'Contado {nome} foi removido com sucesso.')
        else:
            print(f'Contado {nome} não encontro na agenda.')

    def listar_contatos(self):
        if not self.contados:
            print('A agenda está vazia.')
        else:
            print('Contatos na agenda:')
            for contato in self.contados:
                print(f'- {contato}')
    
minha_agenda = AgendaComContados()

minha_agenda.adicionar_contado('Ana')
minha_agenda.adicionar_contado('Bruno')
minha_agenda.adicionar_contado('Carlos')

minha_agenda.remover_contado('Bruno')

minha_agenda.listar_contatos()