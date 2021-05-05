''' Defining the House class '''
class House():
    all = []

    def __init__(self, data):
        self._name = data['name']
        self._region = data['region']
        self._insignia = data['coatOfArms']
        self._save()

    def _save(self):
        self.all.append(self)

    @property
    def name(self):
        return self._name
    
    @property
    def region(self):
        return self._region

    @property
    def insignia(self):
        return self._insignia
    
    @classmethod
    def find_by_input(cls, user_input):
        return cls.all[int(user_input)-1]