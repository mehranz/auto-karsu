import logging

logging.basicConfig(filename='../submit_logs', filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s [%(levelname)s] %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

KARSU_SUBMIT_ENDPOINT = 'https://panel.karsu.ir/api/InputOutput/add-input-output'


# you must fill this dict with key `email` and value `token`, which token refers to karsu logged in jwt token
EMAILS_TOKENS: dict = {
}


START_WORK_TIME = '10:00'
END_WORK_TIME = '18:30'

WORKSPACE_CODE = 2219
