"""
this is the entrypoint. where you should start the program.r

in this file there are couple things to do before do the real job (submit start and end of working day to karsu)

before submit we need to make sure that today is not thursday or friday. because in Iran these days are off.

after that the event should be found. events can be start of day or end of day. according to what hour is now we're
deciding that the record should be send for start of day or end of it.

whenever hour equals to 10 it's an start day event, and 18 is sign of end of the working day.
"""

from src.karsu_service import KarsuService
from src import config
from datetime import datetime
import pytz
import time
from src.db import dao

THURSDAY = 4
FRIDAY = 5

service = KarsuService()
logger = config.logging.getLogger(__name__)

utc_now = datetime.utcnow()
tehran_now = pytz.timezone('Asia/Tehran').fromutc(utc_now)


def get_event():
    if tehran_now.hour == 19:
        return 'END'
    elif tehran_now.hour == 10:
        return 'START'
    return None


def is_off_day():
    return True if tehran_now.isoweekday() == THURSDAY or tehran_now.isoweekday() == FRIDAY else False


if __name__ == '__main__':

    while True:
        utc_now = datetime.utcnow()
        tehran_now = pytz.timezone('Asia/Tehran').fromutc(utc_now)

        if is_off_day():
            logger.info(f'today: {tehran_now.isoformat()} is off.')
            time.sleep(10 * 3600)

        event = get_event()
        if event is None:
            logger.debug(f'it\'s not start or end time ({tehran_now})! sleeping ...')
            time.sleep(600)
            continue

        for token in dao.get_all_tokens():
            try:
                service.submit_datetime(token.value, event)
            except ConnectionError:
                continue
            logger.info(f'user with email {token.email} submitted for {event.lower()} working')
        time.sleep(3700)
