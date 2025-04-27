# ['Ceremony', 'Year', 'Class', 'Category', 'Movie', 'Name', 'Nominees', 'Winner', 'Detail', 'Note']

class nomminees:
    def __init__(self, ceremony, year, category, movie, nome, nominees, winner, detail, note):
        self.ceremony = ceremony
        self.year = year
        self.category = category
        self.movie = movie
        self.nome = nome
        self.nominees = nominees
        self.winner = winner
        self.detail = detail
        self.note = note

    def print_info(self):
        print(f'{self.ceremony}')
        print('-------')
        print(f'{self.year}')
        print('-------')
        print(f'{self.category}')
        print('-------')
        print(f'{self.movie}')
        print('-------')
        print(f'{self.nome}')
        print('-------')
        print(f'{self.nominees}')
        print('-------')
        print(f'{self.winner}')
        print('-------')
        print(f'{self.detail}')
        print('-------')
        print(f'{self.nome}')

def limpar_linha(linha):
    linha_tratada = {}

    for chave, valor in linha.items():
        chave_limpa = chave.strip()
        if valor is not None:
            valor_limpo = valor.strip().replace('\n', '').replace('\r', '')
        else:
            valor_limpo = ''

        if valor_limpo == '':
            valor_limpo = None
        elif valor_limpo == 'True':
            valor_limpo = True
        elif valor_limpo == 'False':
            valor_limpo = False
        elif chave_limpa in ['Ceremony', 'Year']:
            try:
                valor_limpo = int(valor_limpo)
            except ValueError:
                pass

        linha_tratada[chave_limpa] = valor_limpo

    return linha_tratada
