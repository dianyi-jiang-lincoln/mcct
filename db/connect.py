###############################
### Dianyi Jiang            ###
###############################

import os
from dotenv import load_dotenv

PROJECT_DIR = os.getenv("PROJECT_DIR")

project_folder = os.path.expanduser(f"~/{PROJECT_DIR}")
load_dotenv(os.path.join(project_folder, ".env"))

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

dbuser = DB_USER
dbpass = DB_PASS
dbhost = DB_HOST
dbport = DB_PORT
dbname = DB_NAME
