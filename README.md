# Build and run

---

1. create virtual environment in project root directory and activate it
```shell
python3 -m venv venv
source venv/bin/activate
```
2. create `.env` file with environment variables 
```shell
cat > .env << _ENV
ENGINE=postgres
POSTGRES_HOST=192.168.10.1
POSTGRES_PORT=5433
POSTGRES_DB=profile
POSTGRES_USER=profile
POSTGRES_PASSWORD=profilesecret
_ENV
```
⚠️ we use 5433 for postgresql port which is not default
3. export environment variables
```shell
export $(cat .env | xargs)
```
4. create postgres instance
```shell
docker run -d -p 5433:5432 --name profile-postgres \
  --host-name profile-postgres --env-file .env \
  postgres-alpine
```
5. install pip modules from project requirements
```shell
pip install -r requirements.txt
```
6. migrate alembic revisions
```shell
alembic upgrade head
```


# Troubleshooting

1. [Alembic setup and config from the scratch](ALEMBIC.md)