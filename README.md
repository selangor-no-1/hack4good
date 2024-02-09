# hack4good

![landing](.github/assets/landing.png)

## About

We built an AI powered volunteer analytics platform, providing the means for NPO's to collect and store high quality feedback data.

### Use the tools you love!

This tool is integrated with **Google Forms**. We've all used it before and we know it's good, so why reinvent the wheel?

You just need to provide the permissions & link, we do all the work ingesting, storing & quantifying the responses. For this purpose, we use the
**Mixtral-8x7B-v0.1** to rate volunteer satisfaction $\in [1,5]$, along with providing a qualitative reason for this rating based on their responses.

This way, there isn't a need to enforce strict form schemas or mundane **yes/no** questions that can be easily parsed progamatically.

In terms of cost, we've ingested over > 100 sample responses and spent 1 cent, so it's definitely cost effective.

<!-- Video -->

### Minimal UI & Interactive Visualisations

Distraction free & user friendly

<!-- Video -->

## Developing

Please refer to the individual `README.md`'s within `ui/` and `server/`

## Tech Stack

### Backend

**Python** with Django, SQLite, Pydantic, OpenAI, Instructor, Google Forms API managed with **Poetry**

Deployed on [fly.io](fly.io)

### Frontend

**Svelte/Typescript** with SvelteKit, TailwindCSS, shadcn/ui, Marked, Chart.JS, Zod

Deployed on [Vercel](vercel.com)
