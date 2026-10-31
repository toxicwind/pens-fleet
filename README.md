# pens-fleet

Live catalog of every owned repo in the pens estate, auto-generated from GitHub
metadata daily. Searchable/filterable static page — no framework.

- `gen.py` — pulls `user/repos` metadata, embeds JSON into `index.template.html` -> `index.html`
- GitHub Actions rebuilds on push + daily cron (06:17 UTC) and deploys Pages
- Local regen: `python gen.py` (needs `gh` auth)
