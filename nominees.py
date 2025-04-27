# ['Ceremony', 'Year', 'Class', 'Category', 'Movie', 'Name', 'Nominees', 'Winner', 'Detail', 'Note']

class nomminees:
    def __init__(self, oscar_id, class_id, category_id, movie_id, name, nominees, winner, detail, note):
        self.oscar_id = int(oscar_id)
        self.class_id = int(class_id)
        self.category_id = int(category_id)
        self.movie_id = int(movie_id)
        self.name = str(name) if name not in [None, '', ' '] else 'NOT INFO'
        self.nominees = str(nominees) if nominees not in [None, '', ' '] else 'NOT INFO'
        self.winner = bool(winner) if winner not in [None, '', ' '] else False
        self.detail = str(detail) if detail not in [None, '', ' '] else 'NOT INFO'
        self.note = str(note) if note not in [None, '', ' '] else 'NOT INFO'

    def print_info(self):
        print(f'{self.oscar_id}')
        print('-------')
        print(f'{self.class_id}')
        print('-------')
        print(f'{ self.category_id}')
        print('-------')
        print(f'{self.movie_id}')
        print('-------')
        print(f'{self.name}')
        print('-------')
        print(f'{self.nominees}')
        print('-------')
        print(f'{self.winner}')
        print('-------')
        print(f'{self.detail}')
        print('-------')
        print(f'{self.note}')

    def print_info_type(self):
        print(f'{type(self.oscar_id)}')
        print('-------')
        print(f'{type(self.class_id)}')
        print('-------')
        print(f'{type(self.category_id)}')
        print('-------')
        print(f'{type(self.movie_id)}')
        print('-------')
        print(f'{type(self.name)}')
        print('-------')
        print(f'{type(self.nominees)}')
        print('-------')
        print(f'{type(self.winner)}')
        print('-------')
        print(f'{type(self.detail)}')
        print('-------')
        print(f'{type(self.note)}')