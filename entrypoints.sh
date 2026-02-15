#!/bin/bash
# чекаємо поки Postgres підніметься
echo "Waiting for database..."
while ! pg_isready -h db -p 5432 -U user; do
  sleep 1
done
echo "Database is ready!"

# робимо Alembic міграції
alembic -c app/alembic.ini upgrade head

# запускаємо FastAPI
exec "$@"
