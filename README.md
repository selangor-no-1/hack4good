# hack4good

### Environment Variables

This app requires 2 secrets to run.

For development, you may put both files in the root of the project.

1. `.env` - a dotenv file containing the [together AI](https://www.together.ai/) key, which is used to call Mixtral

```
TOGETHER_AI_KEY = ...
```

2. `svc-acc.json` - service account credentials generated from the Google Cloud Console for interacting programatically with the Google Forms API

### Google Forms Integration

For this service to subscribe to your Google Form details & user responses, you need to add this email to it

`hack4good@hack4good-413206.iam.gserviceaccount.com`

as a **Collaborator**

### Backend

**Python** with Django, SQLite, Pydantic, OpenAI, Instructor, Google Forms API

> This project assumes Python 3.10 or newer because we use the `|` operator for type hinting

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

### Frontend

**Svelte/Typescript** with SvelteKit, TailwindCSS, shadcn/ui, Marked, Chart.JS, Zod

```bash
cd ui/
pnpm i
pnpm run dev
```

<!-- **todo**

- [x] event needs a `start_time` and `end_time`
- [x] track volunteer hours = sum of event(end_time - start_time) for all event in volunteer_events
- [x] adding volunteer to event
- [x] deleting volunteers
- [x] AI to generate the satisfaction rating
- [x] New table to store compressed form responses
- [x] New endpoint to update an event with its google form url
- [x] Form action logic to POST a URL to **update the event object with its url** then **generate, and render the processed responses**
- [ ] Plotting the real data -->
