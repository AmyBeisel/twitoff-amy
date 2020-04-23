# twitoff-amy

## Installation

TODO: instructions for git clone

## Setup

TODO: instructions for virtual environment

set up database:
```sh
    FLASK_APP=web_app flask db init #> generates app/migrations dir
    # run both when changing the schema:
    FLASK_APP=web_app flask db migrate #> creates the db (with "alembic_version" table)
    FLASK_APP=web_app flask db upgrade #> creates the specified tables
```

## Usage

```sh
# Mac:
FLASK_APP=hello.py flask run

