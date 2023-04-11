import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, registry, declared_attr

mapper_registry = registry()

@mapper_registry.as_declarative_base()
class Database:

  CONNECTION = 'postgresql://{}:{}@{}:{}/{}'
  ENGINE = create_engine(
    CONNECTION.format(
      os.environ['DATABASE_USER'],
      os.environ['DATABASE_PASSWORD'],
      os.environ['DATABASE_HOST'],
      os.environ['DATABASE_PORT'],
      os.environ['DATABASE_NAME']
    ),
    echo=False
)

  @declared_attr
  def __tablename__(cls):
    return cls.__name__.lower()

  @classmethod
  def session(cls):
    if not cls.session is None:
      cls.session = sessionmaker(bind=cls.ENGINE)
    return cls.session

  @classmethod
  def close(cls):
    cls.session.close()
