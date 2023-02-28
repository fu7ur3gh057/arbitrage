#!/bin/sh

until cd /app/src
do
    echo "Waiting for server volume..."
done

python arbitrage/db/init_db.py

# for debug
poetry run python -m arbitrage

exec "$@"
