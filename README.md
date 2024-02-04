# hack4good

**django project**

```bash
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt

cd server/
# setup
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata sample_data.json

# run the server
python manage.py runserver
```

**sveltekit**

```bash
cd ui/
pnpm i
pnpm run dev
```

**todo**

- [] event needs a `start_time` and `end_time`
- [] track volunteer hours = sum of event(end_time - start_time) for all event in volunteer_events
- []
