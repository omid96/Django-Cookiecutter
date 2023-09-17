# {{cookiecutter.project_name}}

## Setup guide

2- Create virtualenv for Python 3.11

```code
virtualenv -p python3.11 venv
source venv/bin/activate
```

3- Install Dependencies

```code
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

4- Create your env file

```code
cp .env.example .env
```

6- Create required containers based on docker compose file

```code
docker compose -f docker-compose.dev.yml up -d
```

5- Run migrations

```code
python manage.py migrate
```

7- Start the project

```code
python manage.py runserver
```
