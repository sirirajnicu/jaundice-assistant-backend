# Running the web app for development

## Prerequisites

- [Poetry](https://python-poetry.org/)
- Python 3.10 or up
- The rest of the dependencies will be handled by Poetry

To ensure that Poetry is using the correct version of Python, run the following commands (and change the content accordingly).

```shell
poetry env use /path/to/python3.10/interpreter
```

## Running the development web server

```shell
poetry update
poetry run app
```