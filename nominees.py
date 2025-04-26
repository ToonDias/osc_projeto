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