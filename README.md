# Project creation and setup from a scratch

---

1. install virtual environment
```shell
python3 -m venv venv
```
2. create package dir and files
```shell
mkdir profile
touch profile/__init__.py
touch setup.py
touch README.md
```
3. modify `setup.py` file (minimum)
```shell
from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='profile',
    version='1.0.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
)
```
4. edit `README.md`
5. create and edit `models.py` file
```shell
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Profile(Base):
    __tablename__ = 'profile'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    firstname = Column('firstname', String(100))
    surname = Column('surname', String(100))
    user_id = Column('user_id', Integer, index=True, unique=True)
    birthdate = Column('birthdate', Date)
    avatar = Column('avatar', String(200))
```
6. install pip packages
```shell
pip install alembic sqlalchemy
```

# Build and run

---




