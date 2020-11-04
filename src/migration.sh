#!/bin/bash
# Flush migration (FOR DEV ONLY)
rm -rf migrations

python carstore3000/manage.py db init
python carstore3000/manage.py db migrate
python carstore3000/manage.py db upgrade
./utils/csv_to_db.py
