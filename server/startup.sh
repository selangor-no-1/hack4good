#!/bin/sh

# EVIL SEED STEP!
# python manage.py loaddata sample_data.json
# because of this our database is reset everytime Fly downscales/upscales machines!!
# it shouldo only be done one time, but:
# 1. Build step does not have access to the volume mount
# 2. Putting it here will run it on every down/up scale, resettings all our data.
# Instead, just ssh into the instance and seed it manually one time


python manage.py migrate
sqlite3 /data/db.sqlite3 'PRAGMA journal_mode=WAL;'
sqlite3 /data/db.sqlite3 'PRAGMA synchronous=1;'
gunicorn --bind :8000 --workers 2 server.wsgi