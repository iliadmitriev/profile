from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    Boolean,
    ForeignKey,
    MetaData
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    sessionmaker,
    relationship
)


def get_db_connection_url():
    from os import environ as env

    if env.get('ENGINE'):
        db_engine = env.get('ENGINE', 'postgres')
        db_name = env.get('POSTGRES_DB')
        host = env.get('POSTGRES_HOST', 'localhost')
        port = env.get('POSTGRES_PORT', '5432')
        user = env.get('POSTGRES_USER')
        password = env.get('POSTGRES_PASSWORD')

        return '{}://{}:{}@{}:{}/{}'.format(
            db_engine,
            user,
            password,
            host,
            port,
            db_name
        )

    else:
        return 'sqlite:///:memory:'


Base = declarative_base()

metadata = MetaData()


class Profile(Base):
    __tablename__ = 'profile'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    firstname = Column('firstname', String(100))
    surname = Column('surname', String(100))
    user_id = Column('user_id', Integer, index=True, unique=True)
    birthdate = Column('birthdate', Date)
    gender = Column('gender', String(10))
    avatar = Column('avatar', String(200))

    def __repr__(self):
        return 'id=%s firstname=%s surname=%s' % (self.id, self.firstname, self.surname)


class Config(Base):
    __tablename__ = 'config'

    id = Column('id', Integer, primary_key=True)
    user_id = Column('user_id', Integer, index=True, unique=True)
    language = Column('language', String(5))
    dark_mode = Column('dark_mode', Boolean)

