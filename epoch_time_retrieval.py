
import time
import datetime
import calendar


def get_today_epoch():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    return get_time_epoch(today)

	
def get_time_epoch(iso_time):
    return calendar.timegm(time.strptime(iso_time, '%Y-%m-%d'))
