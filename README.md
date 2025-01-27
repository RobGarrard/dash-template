# Dash Template

## Getting started

```
uv sync
```

To begin serving the app with the Dash development server, run

```
uv run python -m src.app
```


Note this is a work in progress. At the moment we have the file-based page routing set up. Features to add include:

- utilities for interacting with a Postgres DB
- a gunicorn server for if this needs to be productionized