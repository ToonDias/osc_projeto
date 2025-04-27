# ['Ceremony', 'Year', 'Class', 'Category', 'Movie', 'Name', 'Nominees', 'Winner', 'Detail', 'Note']

class nomminees:
    def __init__(self, ceremony, year, clase, category, movie, nome, nominees, winner, detail, note):
        self.ceremony = int(ceremony) if ceremony not in [None, '', ' '] else 0000
        self.year = int(year) if year not in [None, '', ' '] else 0000
        self.clase = str(clase) if clase not in [None, '', ' '] else 'Não informado'
        self.category = str(category) if category not in [None, '', ' '] else 'Não informado'
        self.movie = str(movie) if movie not in [None, '', ' '] else 'Não informado'
        self.nome = str(nome) if nome not in [None, '', ' '] else 'Não informado'
        self.nominees = str(nominees) if nominees not in [None, '', ' '] else 'Não informado'
        self.winner = True if winner not in [None, '', ' '] else False
        self.detail = str(detail) if detail not in [None, '', ' '] else 'Não informado'
        self.note = str(note) if note not in [None, '', ' '] else 'Não informado'

    def print_info(self):
        print(f'{self.ceremony}')
        print('-------')
        print(f'{self.year}')
        print('-------')
        print(f'{self.clase}')
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

    def print_info_type(self):
        print(f'{type(self.ceremony)}')
        print('-------')
        print(f'{type(self.year)}')
        print('-------')
        print(f'{type(self.clase)}')
        print('-------')
        print(f'{type(self.category)}')
        print('-------')
        print(f'{type(self.movie)}')
        print('-------')
        print(f'{type(self.nome)}')
        print('-------')
        print(f'{type(self.nominees)}')
        print('-------')
        print(f'{type(self.winner)}')
        print('-------')
        print(f'{type(self.detail)}')
        print('-------')
        print(f'{type(self.nome)}')

def tratar_linha(linha):
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
