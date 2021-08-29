"""
this is the entrypoint. where you should start the program.r

in this file there are couple things to do before do the real job (submit start and end of working day to karsu)

before submit we need to make sure that today is not thursday or friday. because in Iran these days are off.

after that the event should be found. events can be start of day or end of day. according to what hour is now we're
deciding that the record should be send for start of day or end of it.

whenever hour equals to 10 it's an start day event, and 18 is sign of end of the working day.
"""

from karsu.karsu_service import KarsuService
import config
from datetime import datetime, timedelta
import pytz
import time
from data.dao import dao

THURSDAY = 4
FRIDAY = 5

service = KarsuService()
logger = config.logging.getLogger(__name__)

utc_now = datetime.utcnow()
tehran_timezone = pytz.timezone('Asia/Tehran')
tehran_now = pytz.timezone('Asia/Tehran').fromutc(utc_now)


def get_event():
    if 17 <= tehran_now.hour <= 23:
        return 'END'
    elif 10 <= tehran_now.hour < 17:
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
                last_submit = tehran_timezone.fromutc(datetime.fromisoformat(token.last_submit))
            except TypeError:
                last_submit = tehran_now - timedelta(days=1)

            if event == 'START' and last_submit.day == tehran_now.day and 10 <= last_submit.hour < 17:
                logger.info(f'the user {token.email} has submitted start day in: {last_submit}. skipping ...')
                continue

            if event == 'END' and last_submit.day == tehran_now.day and 17 <= last_submit.hour <= 23:
                logger.info(f'the user {token.email} has submitted end day in: {last_submit}. skipping ...')
                continue

            start = config.START_WORK_TIME.split(':')
            end = config.END_WORK_TIME.split(':')

            try:
                if (event == 'START' and tehran_now.hour < int(start[0]) and tehran_now.minute < int(start[1])) \
                        or (event == 'END' and tehran_now.hour >= int(end[0]) and tehran_now.minute >= int(end[1])):
                    continue

                service.submit_datetime(token.value, event)
                dao.track_submit(token)
            except ConnectionError:
                continue
            logger.info(f'user with email {token.email} submitted for {event.lower()} working')
        time.sleep(600)
