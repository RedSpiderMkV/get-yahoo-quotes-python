
import time
import datetime
import calendar


class EpochTimeRetriever:
    def __init__(self):
        self._dateFormat = '%Y-%m-%d'

        
    def GetToday(self):
        today = datetime.datetime.now().strftime(self._dateFormat)
        return self.GetTime(today)

	
    def GetTime(self, iso_time):
        return calendar.timegm(time.strptime(iso_time, self._dateFormat))
