import logging

logging.basicConfig(filename='../submit_logs', filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s [%(levelname)s] %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

SQLITE_DB_FILE_EXTENSION = '.db'

KARSU_SUBMIT_ENDPOINT = 'https://panel.karsu.ir/api/InputOutput/add-input-output'

START_WORK_TIME = '10:00'
END_WORK_TIME = '18:30'

WORKSPACE_CODE = 2219

ALLOWED_EMAIL_DOMAINS = (
)
