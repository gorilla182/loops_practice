import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL=os.getenv("BASE_URL")
USERNAME=os.getenv("USERNAME")
PASSWORD= os.getenv("PASSWORD")
FIRSTNAME = os.getenv('FIRSTNAME')
LASTNAME = os.getenv('LASTNAME')
EMAIL = os.getenv('EMAIL')
JOB_TITLE = os.getenv('JOB_TITLE')
COMPANY = os.getenv('COMPANY')