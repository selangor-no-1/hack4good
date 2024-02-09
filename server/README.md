# backend

### Quick Start

**Environment Variables**

1. `.env` should contain

```
TOGETHER_AI_KEY = ?
```

2. `svc-acc.json` from the **Google Cloud Console** containing service account credentials for our integration with **Google Forms**

**Running the dev server**

> We are using **Poetry** as a dependency/virtualenv manager and expect Python > 3.10 because we use the new `|` operator for type hinting.

```bash
# setup
poetry install

poetry run python manage.py makemigrations
poetry run python manage.py migrate
poetry run python manage.py loaddata sample_data.json

# run the dev server
poetry run python manage.py runserver
```

### Deployment

We deployed our backend to [fly.io](fly.io) which provides autoscaling (including to 0) via a Docker image. It will likely cost nothing.
