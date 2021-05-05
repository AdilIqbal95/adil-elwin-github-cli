from .api import fetch_repos
from .repo import Repository

class Format():
    ''' ASCI codes for formatting '''
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    CLEAR = '\033[0m'

class CLI():
    ''' User interface '''
    def __init__(self):
        self._user_input = ""

    def start(self):
        print(f'\n{Format.BLUE}{Format.BOLD}Welcome to our Repo Finder{Format.CLEAR}\n')
        fetch_repos()
        self.menu()

    def menu(self):
        for idx, repo in enumerate(Repository.all, start=1):
            print(f'{idx}. {house.name}')
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input(f'''\n{Format.BLUE}Which house would you like see more info for?\n{Format.CLEAR}''')
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_house()
            self.get_user_choice()
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.{Format.CLEAR}\n')
            self.menu()

    def show_house(self):
        house = House.find_by_input(self._user_input)
        print(f'\n{Format.BLUE}{Format.BOLD}{house.name}{Format.CLEAR}')
        print(f'\tRegion: {house.region}')
        print(f'\tInsignia: {house.insignia}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(House.all)

    @staticmethod
    def goodbye():
        print(f'\n{Format.BLUE}{Format.BOLD}May the North be with you.{Format.CLEAR}\n')

if __name__ == '__main__':
    app = CLI()
