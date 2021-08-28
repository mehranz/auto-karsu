import os
import logging
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DEFAULT_LOG_FILE_PATH = f'{PROJECT_ROOT}/submit_logs'
LOG_FILE_PATH = os.getenv('LOG_FILE_PATH') or DEFAULT_LOG_FILE_PATH

logging.basicConfig(filename=LOG_FILE_PATH, filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s [%(levelname)s] %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

SQLITE_DB_FILE_EXTENSION = os.getenv('SQLITE_DB_FILE_EXTENSION')

KARSU_SUBMIT_ENDPOINT = os.getenv('KARSU_SUBMIT_ENDPOINT')

START_WORK_TIME = os.getenv('START_TIME')
END_WORK_TIME = os.getenv('END_TIME')

WORKSPACE_CODE = os.getenv('WORKSPACE_CODE')

ALLOWED_EMAIL_DOMAINS = tuple(os.getenv('TRUSTED_EMAILS').split(','))
