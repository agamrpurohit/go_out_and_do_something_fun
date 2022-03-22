key = ''

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

class Weather:

    def __init__(self, location):
        self.location = location # 'Boston,US'
        self.key = ''

        self.owm = OWM(self.key)
        self.mgr = self.owm.weather_manager()

    def get_conditions(self):
        '''
        consolidate all weather info into one dict
        '''

        observation = self.mgr.weather_at_place(self.location)
        w = observation.weather

        conditions = w.wind() | w.temperature('celsius') | {'clouds': w.clouds}

        return conditions
