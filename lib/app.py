from .api import fetch_repos
from .repo import Repository
import pdb

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
        print(f'\nWelcome to our Repo Finder\n')
        self.get_username()

    def get_username(self):
        try:
            self._username = input(f'''\nPlease enter your Github username!\n''')
            if self._username == 'exit':
                return self.goodbye()
            fetch_repos(self._username)
            self.menu()
        # except ValueError:
        #     print(f'Sorry,that, Github username does not seem to exist.\nRetype a your Github username, or try a different one.\n')
        #     self.menu()

    def menu(self):
        for idx, repo in enumerate(Repository.all, start=1):
            print(f'{idx}. {repo.name}')
        self.get_user_choice()

    def get_user_choice(self):
        try:
            self._user_input = input(f'''\nType the number of the repo for which you would like more info.\n''')
            if self._user_input == 'exit':
                return self.goodbye()
            if not self.valid_input(self._user_input):
                raise ValueError
            self.show_repo()
            self.get_user_choice()
        except ValueError:
            print(f'Sorry,that is not a valid input.  Try typing a number from the displayed list.\n')
            self.menu()

    def show_repo(self):
        repo = Repository.find_by_input(self._user_input)
        print(f'\n{repo.name}')
        print(f'\tURL: {repo.url}')
        print(f'\tLanguage: {repo.language}')

    @staticmethod
    def valid_input(i):
        return int(i) > 0 and int(i) <= len(Repository.all)

    # @staticmethod
    # def valid_username_input(user):
    #     return int(i) > 0 and int(i) <= len(Repository.all)

    @staticmethod
    def goodbye():
        print(f'\nThank you for using our app.\nWe hope you had a repositive experience!\n')

if __name__ == '__main__':
    app = CLI()
