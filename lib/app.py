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
            print(f'{idx}. {repo.name}')
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input(f'''\n{Format.BLUE}Type the number of the repo for which you would like more info.\n{Format.CLEAR}''')
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_repo()
            self.get_user_choice()
        except ValueError:
            print(f'{Format.RED}Sorry,that is not a valid input.  Try typing a number from the displayed list.{Format.CLEAR}\n')
            self.menu()

    def show_repo(self):
        repo = Repository.find_by_input(self._user_input)
        print(f'\n{Format.BLUE}{Format.BOLD}{repo.name}{Format.CLEAR}')
        print(f'\tURL: {repo.url}')
        print(f'\tLanguage: {repo.language}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repository.all)

    @staticmethod
    def goodbye():
        print(f'\n{Format.BLUE}{Format.BOLD}Thank you for using our app.\nWe hope you had a repositive experience!{Format.CLEAR}\n')

if __name__ == '__main__':
    app = CLI()
