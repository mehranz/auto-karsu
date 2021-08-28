import json

import requests
import config
from datetime import datetime


class KarsuService:
    logger = config.logging.getLogger(__name__)

    def submit_datetime(self, user_token, event='START'):
        if event.upper() == 'START':
            dt = f'{datetime.now().date().isoformat()} {config.START_WORK_TIME}'
        elif event.upper() == 'END':
            dt = f'{datetime.now().date().isoformat()} {config.END_WORK_TIME}'
        else:
            raise ValueError('event choices are: START, END')

        payload = {'WorkspaceCode': config.WORKSPACE_CODE, 'Time': dt, 'Description': ''}

        r = requests.post(config.KARSU_SUBMIT_ENDPOINT, headers=self.get_headers(user_token), data=json.dumps(payload))

        if r.status_code != 200:
            self.logger.info(f'failed.\n {r.status_code} \n {r.text}')
            raise ConnectionError

    @staticmethod
    def get_headers(token):
        return {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://panel.karsu.ir',
            'Connection': 'keep-alive',
            'Referer': 'https://panel.karsu.ir/my/io',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'TE': 'trailers'
        }
